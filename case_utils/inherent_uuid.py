#!/usr/bin/env python3

# Portions of this file contributed by NIST are governed by the following
# statement:
#
# This software was developed at the National Institute of Standards
# and Technology by employees of the Federal Government in the course
# of their official duties. Pursuant to Title 17 Section 105 of the
# United States Code, this software is not subject to copyright
# protection within the United States. NIST assumes no responsibility
# whatsoever for its use by other parties, and makes no guarantees,
# expressed or implied, about its quality, reliability, or any other
# characteristic.
#
# We would appreciate acknowledgement if the software is used.

"""
This library provides supporting constants and functions for generating deterministic UUIDs (version 5) for UCO Hash and Facet nodes.

There are two general patterns implemented:

1. Some objects are "wholly specified" by their properties.  The leading example of this is uco-types:Hash, which has only the properties hashMethod and hashValue, and both are required to be provided in order to be conformant with UCO.  The function `hash_method_value_uuid` implements a scheme to generate UUIDs for uco-types:Hash nodes based on this pattern.
2. A pattern based on inherence generates UUIDv5s based on how an inherent object (a.k.a. UcoInherentCharacterizationThing) structurally relates to the object in which it inheres.  For instance, a Facet is understood to only relate to its UcoObject by linking with the uco-core:hasFacet property.  So, a Facet's UUID is determined uniquely by (1) the "UUID namespace" of its corresponding UcoObject, and (2) its OWL Class.
   A. The term "UUID namespace" is described in RFC 4122 Section 4.3 [#rfc4122s43]_ , and is not intended be confused with `rdflib.term.Namespace`.  For any uco-core:UcoThing (or even owl:Thing), the function `inherence_uuid` defines the procedure for either extracting or generating a UUID for use as a namespace.

This module is independent of, and complements, `cdo_local_uuid.local_uuid`, which provides deterministic UUIDs based on calling process's environment.

References
==========

.. [#rfc4122s43] https://datatracker.ietf.org/doc/html/rfc4122#section-4.3


Examples
========

A knowledge base ontology currently uses a prefix 'kb:', expanding to 'http://example.org/kb/'.  This knowledge base has a node kb:File-ac6b44cf-dc6b-4f2c-a09d-c9beb0a345a9. What is the IRI of its FileFacet?

>>> from case_utils.namespace import NS_UCO_OBSERVABLE
>>> ns_kb = Namespace("http://example.org/kb/")
>>> n_file = ns_kb["File-ac6b44cf-dc6b-4f2c-a09d-c9beb0a345a9"]
>>> n_file_facet = get_facet_uriref(n_file, NS_UCO_OBSERVABLE.FileFacet, namespace=ns_kb)
>>> n_file_facet
rdflib.term.URIRef('http://example.org/kb/FileFacet-01d292e3-0f38-5974-868d-006ef07f5186')

A documentation policy change has been enacted, and now all knowledge base individuals need to use the URN example form.  What is the FileFacet IRI now?

>>> ns_kb_2 = Namespace("urn:example:kb:")
>>> file_iri_2: str = "urn:example:kb:File-ac6b44cf-dc6b-4f2c-a09d-c9beb0a345a9"
>>> n_file_2 = URIRef(file_iri_2)
>>> n_file_facet_2 = get_facet_uriref(n_file_2, NS_UCO_OBSERVABLE.FileFacet, namespace=ns_kb_2)
>>> n_file_facet_2
rdflib.term.URIRef('urn:example:kb:FileFacet-01d292e3-0f38-5974-868d-006ef07f5186')

The two IRIs end with the same UUID.

>>> assert str(n_file_facet)[-36:] == str(n_file_facet_2)[-36:]
"""

__version__ = "0.1.2"

import binascii
import re
import uuid
from typing import Any, Dict, Optional, Tuple

from rdflib import Literal, Namespace, URIRef

from case_utils.namespace import NS_UCO_CORE, NS_UCO_VOCABULARY, NS_XSD

L_MD5 = Literal("MD5", datatype=NS_UCO_VOCABULARY.HashNameVocab)
L_SHA1 = Literal("SHA1", datatype=NS_UCO_VOCABULARY.HashNameVocab)
L_SHA256 = Literal("SHA256", datatype=NS_UCO_VOCABULARY.HashNameVocab)
L_SHA3_256 = Literal("SHA3-256", datatype=NS_UCO_VOCABULARY.HashNameVocab)
L_SHA3_512 = Literal("SHA3-512", datatype=NS_UCO_VOCABULARY.HashNameVocab)
L_SHA384 = Literal("SHA384", datatype=NS_UCO_VOCABULARY.HashNameVocab)
L_SHA512 = Literal("SHA512", datatype=NS_UCO_VOCABULARY.HashNameVocab)
L_SSDEEP = Literal("SSDEEP", datatype=NS_UCO_VOCABULARY.HashNameVocab)

# Key: hashMethod literal.
# Value: Tuple.
#   * Lowercase spelling
HASH_METHOD_CASTINGS: Dict[Literal, Tuple[str, Optional[int]]] = {
    L_MD5: ("md5", 32),
    L_SHA1: ("sha1", 40),
    L_SHA256: ("sha256", 64),
    L_SHA3_256: ("sha3-256", 64),
    L_SHA3_512: ("sha3-512", 128),
    L_SHA384: ("sha384", 96),
    L_SHA512: ("sha512", 128),
    L_SSDEEP: ("ssdeep", None),
}

RX_UUID = re.compile(
    "[0-9a-f]{8}-[0-9a-f]{4}-[0-5][0-9a-f]{3}-[0-9a-f]{4}-[0-9a-f]{12}$", re.IGNORECASE
)


def inherence_uuid(n_thing: URIRef, *args: Any, **kwargs: Any) -> uuid.UUID:
    """
    This function returns a UUIDv5 for any OWL Thing, that can be used as a UUID Namespace in further `uuid.uuidv5` calls.

    In the case that the Thing is a UcoThing that ends with a UUID, that UUID string will be returned wrapped in a UUID object.  In all other cases, a UUID version 5 object will be returned for the Thing as a name under the URL namespace [#rfc4122ac]_.

    References
    ==========

    .. [#rfc4122ac] https://datatracker.ietf.org/doc/html/rfc4122#appendix-C

    Examples
    ========

    A File node will need its FileFacet IRI determined.  What will be the base UUID namespace for determining this IRI as well as other inherent graph objects?

    >>> file_iri: str = "http://example.org/kb/File-ac6b44cf-dc6b-4f2c-a09d-c9beb0a345a9"
    >>> n_file = URIRef(file_iri)
    >>> file_uuid_namespace: uuid.UUID = inherence_uuid(n_file)
    >>> file_uuid_namespace
    UUID('ac6b44cf-dc6b-4f2c-a09d-c9beb0a345a9')

    The CASE homepage is being treated as an OWL NamedIndividual in this knowledge base, with its URL as its IRI.  What is its base UUID namespace?

    >>> case_homepage_url: str = "https://caseontology.org/"
    >>> n_case_homepage = URIRef(case_homepage_url)
    >>> case_homepage_uuid_namespace = inherence_uuid(n_case_homepage)
    >>> case_homepage_uuid_namespace
    UUID('2c6406b7-3396-5fdd-b9bf-c6e21273e40a')
    """
    node_iri = str(n_thing)
    if len(node_iri) < 40 or RX_UUID.search(node_iri) is None:
        # <40 -> Too short to have a UUID and scheme.
        return uuid.uuid5(uuid.NAMESPACE_URL, node_iri)
    else:
        return uuid.UUID(node_iri[-36:])


def facet_inherence_uuid(
    uco_object_inherence_uuid: uuid.UUID,
    n_facet_class: URIRef,
    *args: Any,
    **kwargs: Any
) -> uuid.UUID:
    """
    :param n_facet_class: This node is expected to be the `rdflib.term.URIRef` for an OWL Class that is either in UCO or extends a class in UCO, such as `case_utils.namespace.NS_UCO_OBSERVABLE.FileFacet`.  The Facet class SHOULD be a 'leaf' class - that is, it should have no OWL subclasses.  (This 'SHOULD' might become a more stringent requirement in the future.  uco-core:Facet MUST not be used.  There is some question on how this rule should apply for uco-observable:WifiAddressFacet and its parent class uco-observable:MACAddressFacet.)
    :type n_facet_class: rdflib.term.URIRef
    """

    if n_facet_class == NS_UCO_CORE.Facet:
        raise ValueError("Requested Facet class is not a leaf Facet class.")
    # NOTE: Further reviewing whether n_facet_class pertains to a Facet subclass is not done in this library.  Both a set of all such known classes, as well as an extension mechanism for non-standard Facet subclasses (probably either a Set or Graph as an extra parameter), would need to be implemented.

    return uuid.uuid5(uco_object_inherence_uuid, str(n_facet_class))


def get_facet_uriref(
    n_uco_object: URIRef,
    n_facet_class: URIRef,
    *args: Any,
    namespace: Namespace,
    **kwargs: Any
) -> URIRef:
    """
    :param namespace: An RDFLib Namespace object to use for prefixing the Facet IRI with a knowledge base prefix IRI.
    :type namespace rdflib.Namespace:

    Examples
    ========

    What is the URLFacet pertaining to the Nitroba University Scenario's PCAP file, when being interpreted as a Simple Storage Service (S3) object?

    >>> from case_utils.namespace import NS_UCO_OBSERVABLE
    >>> pcap_url: str = "s3://digitalcorpora/corpora/scenarios/2008-nitroba/nitroba.pcap"
    >>> n_pcap = URIRef(pcap_url)
    >>> ns_kb = Namespace("http://example.org/kb/")
    >>> n_pcap_url_facet = get_facet_uriref(n_pcap, NS_UCO_OBSERVABLE.URLFacet, namespace=ns_kb)
    >>> n_pcap_url_facet
    rdflib.term.URIRef('http://example.org/kb/URLFacet-4b6023da-dbc4-5e1e-9a2f-aca2a6f6405c')
    """
    uco_object_uuid_namespace: uuid.UUID = inherence_uuid(n_uco_object)
    facet_uuid = facet_inherence_uuid(uco_object_uuid_namespace, n_facet_class)

    # NOTE: This encodes an assumption that Facets (including extension Facets) use the "Slash" IRI style.
    facet_class_local_name = str(n_facet_class).rsplit("/")[-1]

    return namespace[facet_class_local_name + "-" + str(facet_uuid)]


def hash_method_value_uuid(l_hash_method: Literal, l_hash_value: Literal) -> uuid.UUID:
    """
    This function generates a UUID for a UCO Hash object, solely based on its two required properties: uco-types:hashMethod and uco-types:hashValue.

    The UUIDv5 seed data for Hash nodes is a URN following the scheme in this draft IETF memo:

    https://datatracker.ietf.org/doc/html/draft-thiemann-hash-urn-01

    Note that at the time of this writing, that memo was expired (expiration date 2004-03-04) and did not have a linked superseding document.
    """

    if l_hash_value.datatype != NS_XSD.hexBinary:
        raise ValueError("Expected hexBinary datatype for l_hash_value.")
    hash_value_str: str = binascii.hexlify(l_hash_value.toPython()).decode().lower()

    hash_method_str = HASH_METHOD_CASTINGS[l_hash_method][0]

    urn_template = "urn:hash::%s:%s"
    urn_populated = urn_template % (hash_method_str, hash_value_str)

    return uuid.uuid5(uuid.NAMESPACE_URL, urn_populated)
