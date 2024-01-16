#!/usr/bin/env python3

# This software was developed at the National Institute of Standards
# and Technology by employees of the Federal Government in the course
# of their official duties. Pursuant to title 17 Section 105 of the
# United States Code this software is not subject to copyright
# protection and is in the public domain. NIST assumes no
# responsibility whatsoever for its use by other parties, and makes
# no guarantees, expressed or implied, about its quality,
# reliability, or any other characteristic.
#
# We would appreciate acknowledgement if the software is used.

###########################################################
#
#
# AUTOMATICALLY GENERATED FILE.  MANUAL EDITS WILL BE LOST.
#
#
###########################################################

from __future__ import annotations

import typing

import rdflib

NS_RDF = rdflib.RDF
NS_UCO_CORE = rdflib.Namespace("https://ontology.unifiedcyberontology.org/uco/core/")
NS_UCO_OBSERVABLE = rdflib.Namespace(
    "https://ontology.unifiedcyberontology.org/uco/observable/"
)


class NodeConstructor(object):
    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        super().__init__()
        self._graph: rdflib.Graph = graph
        self._node: typing.Optional[rdflib.URIRef] = None
        self._node_iri = node_iri
        self._type_iris: typing.Set[str] = type_iris
        for type_iri in sorted(self.type_iris):
            self.graph.add((self.node, NS_RDF.type, rdflib.URIRef(type_iri)))

    def add_type_iri(self, type_iri: str) -> None:
        """
        Add additional RDF type to graph node.
        """
        self.type_iris.add(type_iri)
        self.graph.add((self.node, NS_RDF.type, rdflib.URIRef(type_iri)))

    @property
    def graph(self) -> rdflib.Graph:
        return self._graph

    @property
    def node(self) -> rdflib.URIRef:
        """
        Set on first access.
        """
        if self._node is None:
            self._node = rdflib.URIRef(self.node_iri)
        return self._node

    @property
    def node_iri(self) -> str:
        return self._node_iri

    @node_iri.setter
    def node_iri(self, value: str) -> None:
        assert isinstance(value, str)
        self._node_iri = value

    @property
    def type_iris(self) -> typing.Set[str]:
        return self._type_iris

    def add_to_graph(self, graph: rdflib.Graph) -> None:
        for type_iri in sorted(self.type_iris):
            graph.add((self.node, rdflib.RDF.type, rdflib.URIRef(type_iri)))


class UCO_UcoThing(NodeConstructor):
    """
    UcoThing is the top-level class within UCO.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/core/UcoThing'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {"https://ontology.unifiedcyberontology.org/uco/core/UcoThing"}
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_UcoObject(UCO_UcoThing):
    """
    A UCO object is a representation of a fundamental concept either directly inherent to the cyber domain or indirectly related to the cyber domain and necessary for contextually characterizing cyber domain concepts and relationships. Within the Unified Cyber Ontology (UCO) structure this is the base class acting as a consistent, unifying and interoperable foundation for all explicit and inter-relatable content objects.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/core/UcoObject'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/core/UcoObject"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)
        self._facets: typing.List[UCO_Facet] = []

    def add_facet(self, facet: UCO_Facet) -> None:
        self.facets.append(facet)
        self.graph.add((self.node, NS_UCO_CORE.hasFacet, facet.node))

    @property
    def facets(self) -> typing.List[UCO_Facet]:
        return self._facets


class UCO_Observable(UCO_UcoObject):
    """
    An observable is a characterizable item or action within the digital domain.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/Observable'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/Observable"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Item(UCO_UcoObject):
    """
    An item is a distinct article or unit.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/core/Item'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {"https://ontology.unifiedcyberontology.org/uco/core/Item"}
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ObservableObject(UCO_Item, UCO_Observable):
    """
    An observable object is a grouping of characteristics unique to a distinct article or unit within the digital domain.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/ObservableObject'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/ObservableObject"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_UcoInherentCharacterizationThing(UCO_UcoThing):
    """
    A UCO inherent characterization thing is a grouping of characteristics unique to a particular inherent aspect of a UCO domain object.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/core/UcoInherentCharacterizationThing'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/core/UcoInherentCharacterizationThing"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Device(UCO_ObservableObject):
    """
    A device is a piece of equipment or a mechanism designed to serve a special purpose or perform a special function. [based on https://www.merriam-webster.com/dictionary/device]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/Device'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/Device"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Role(UCO_UcoObject):
    """
    A role is a usual or customary function based on contextual perspective.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/role/Role'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {"https://ontology.unifiedcyberontology.org/uco/role/Role"}
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Facet(UCO_UcoInherentCharacterizationThing):
    """
    A facet is a grouping of characteristics singularly unique to a particular inherent aspect of a UCO domain object.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/core/Facet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {"https://ontology.unifiedcyberontology.org/uco/core/Facet"}
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Address(UCO_ObservableObject):
    """
    An address is an identifier assigned to enable routing and management of information.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/Address'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/Address"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_MobileDevice(UCO_Device):
    """
    A mobile device is a portable computing device. [based on https://www.lexico.com.definition/mobile_device]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/MobileDevice'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/MobileDevice"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_NeutralRole(UCO_Role):
    """
    A neutral role is a role with impartial intent.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/role/NeutralRole'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/role/NeutralRole"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class CO_Collection(NodeConstructor):
    """
    A group of objects that can be considered as a whole.

    Based on class with IRI 'http://purl.org/co/Collection'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {"http://purl.org/co/Collection"}
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_FileSystemObject(UCO_ObservableObject):
    """
    A file system object is an informational object represented and managed within a file system.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/FileSystemObject'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/FileSystemObject"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Account(UCO_ObservableObject):
    """
    An account is an arrangement with an entity to enable and control the provision of some capability or service.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/Account'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/Account"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_DigitalAddressFacet(UCO_Facet):
    """
    A digital address facet is a grouping of characteristics unique to an identifier assigned to enable routing and management of digital communication.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/DigitalAddressFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/DigitalAddressFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_DigitalAddress(UCO_Address):
    """
    A digital address is an identifier assigned to enable routing and management of digital communication.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/DigitalAddress'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/DigitalAddress"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_SmartDevice(UCO_Device):
    """
    A smart device is a microprocessor IoT device that is expected to be connected directly to cloud-based networks or via smartphone

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/SmartDevice'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/SmartDevice"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_MobilePhone(UCO_MobileDevice):
    """
    A mobile phone is a portable telephone that at least can make and receive calls over a radio frequency link while the user is moving within a telephone service area. This category encompasses all types of mobiles, simple and smart and satellite ones all together.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/MobilePhone'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/MobilePhone"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Computer(UCO_Device):
    """
    A computer is an electronic device for storing and processing data, typically in binary, according to instructions given to it in a variable program. [based on 'Computer.' Oxford English Dictionary, Oxford University Press, 2022.]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/Computer'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/Computer"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_IdentityAbstraction(UCO_UcoObject):
    """
    An identity abstraction is a grouping of identifying characteristics unique to an individual or organization. This class is an ontological structural abstraction for this concept. Implementations of this concept should utilize the identity:Identity class.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/core/IdentityAbstraction'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/core/IdentityAbstraction"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Compilation(UCO_UcoObject):
    """
    A compilation is a grouping of things.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/core/Compilation'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/core/Compilation"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Action(UCO_UcoObject):
    """
    An action is something that may be done or performed.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/action/Action'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {"https://ontology.unifiedcyberontology.org/uco/action/Action"}
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Victim(UCO_NeutralRole):
    """
    A victim is a role played by a person or organization that is/was the target of some malicious action.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/victim/Victim'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {"https://ontology.unifiedcyberontology.org/uco/victim/Victim"}
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class CO_Item(NodeConstructor):
    """
    Element belonging to a bag

    Based on class with IRI 'http://purl.org/co/Item'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {"http://purl.org/co/Item"}
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class CO_Bag(CO_Collection):
    """
    Collection that can have a number of copies of each object

    Based on class with IRI 'http://purl.org/co/Bag'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {"http://purl.org/co/Bag"}
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_DictionaryEntry(UCO_UcoInherentCharacterizationThing):
    """
    A dictionary entry is a single (term/key, value) pair.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/types/DictionaryEntry'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/types/DictionaryEntry"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Dictionary(UCO_UcoInherentCharacterizationThing):
    """
    A dictionary is list of (term/key, value) pairs with each term/key existing no more than once.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/types/Dictionary'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/types/Dictionary"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Tool(UCO_UcoObject):
    """
    A tool is an element of hardware and/or software utilized to carry out a particular function.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/tool/Tool'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {"https://ontology.unifiedcyberontology.org/uco/tool/Tool"}
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Pattern(UCO_UcoObject):
    """
    A pattern is a combination of properties, acts, tendencies, etc., forming a consistent or characteristic arrangement.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/pattern/Pattern'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/pattern/Pattern"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_NetworkConnection(UCO_ObservableObject):
    """
    A network connection is a connection (completed or attempted) across a digital network (a group of two or more computer systems linked together). [based on https://www.webopedia.com/TERM/N/network.html]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/NetworkConnection'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/NetworkConnection"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ProcessThread(UCO_ObservableObject):
    """
    A process thread is the smallest sequence of programmed instructions that can be managed independently by a scheduler on a computer, which is typically a part of the operating system. It is a component of a process. Multiple threads can exist within one process, executing concurrently and sharing resources such as memory, while different processes do not share these resources. In particular, the threads of a process share its executable code and the values of its dynamically allocated variables and non-thread-local global variables at any given time. [based on https://en.wikipedia.org/wiki/Thread_(computing)]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/ProcessThread'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/ProcessThread"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Process(UCO_ObservableObject):
    """
    A process is an instance of a computer program executed on an operating system.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/Process'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/Process"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_File(UCO_FileSystemObject):
    """
    A file is a computer resource for recording data discretely on a computer storage device.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/File'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/File"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_DigitalAccount(UCO_Account):
    """
    A digital account is an arrangement with an entity to enable and control the provision of some capability or service within the digital domain.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/DigitalAccount'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/DigitalAccount"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_MACAddressFacet(UCO_DigitalAddressFacet):
    """
    A MAC address facet is a grouping of characteristics unique to a media access control standards conformant identifier assigned to a network interface to enable routing and management of communications at the data link layer of a network segment.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/MACAddressFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/MACAddressFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_MACAddress(UCO_DigitalAddress):
    """
    A MAC address is a media access control standards conformant identifier assigned to a network interface to enable routing and management of communications at the data link layer of a network segment.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/MACAddress'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/MACAddress"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ContactFacet(UCO_Facet):
    """
    A contact facet is a grouping of characteristics unique to a set of identification and communication related details for a single entity.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/ContactFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/ContactFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_DefinedEffectFacet(UCO_Facet):
    """
    A defined effect facet is a grouping of characteristics unique to the effect of an observable action in relation to one or more observable objects.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/DefinedEffectFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/DefinedEffectFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Message(UCO_ObservableObject):
    """
    A message is a discrete unit of electronic communication intended by the source for consumption by some recipient or group of recipients. [based on https://en.wikipedia.org/wiki/Message]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/Message'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/Message"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Appliance(UCO_Device):
    """
    An appliance is a purpose-built computer with software or firmware that is designed to provide a specific computing capability or resource. [based on https://en.wikipedia.org/wiki/Computer_appliance]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/Appliance'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/Appliance"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Relationship(UCO_UcoObject):
    """
    A relationship is a grouping of characteristics unique to an assertion that one or more objects are related to another object in some way.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/core/Relationship'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/core/Relationship"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_IPAddressFacet(UCO_DigitalAddressFacet):
    """
    An IP address facet is a grouping of characteristics unique to an Internet Protocol (IP) standards conformant identifier assigned to a device to enable routing and management of IP standards conformant communication to or from that device.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/IPAddressFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/IPAddressFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_IPAddress(UCO_DigitalAddress):
    """
    An IP address is an Internet Protocol (IP) standards conformant identifier assigned to a device to enable routing and management of IP standards conformant communication to or from that device.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/IPAddress'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/IPAddress"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_SmartPhone(UCO_Computer, UCO_MobilePhone, UCO_SmartDevice):
    """
    A smartphone is a portable device that combines mobile telephone and computing functions into one unit.  Examples include iPhone, Samsung Galaxy, Huawei, Blackberry. (Inferred by model and OperatingSystemFacet)

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/SmartPhone'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/SmartPhone"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_AppleDevice(UCO_Device):
    """
    An apple device is a smart device that applies either the MacOS or iOS operating system.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/AppleDevice'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/AppleDevice"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Software(UCO_ObservableObject):
    """
    Software is a definitely scoped instance of a collection of data or computer instructions that tell the computer how to work. [based on https://en.wikipedia.org/wiki/Software]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/Software'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/Software"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_AndroidDevice(UCO_Device):
    """
    An Android device is a device running the Android operating system. [based on https://en.wikipedia.org/wiki/Android_(operating_system)]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/AndroidDevice'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/AndroidDevice"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_MarkingModel(UCO_UcoInherentCharacterizationThing):
    """
    A marking model is a grouping of characteristics unique to the expression of a particular form of data marking definitions (restrictions, permissions, and other guidance for how data can be used and shared).

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/marking/MarkingModel'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/marking/MarkingModel"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_MarkingDefinitionAbstraction(UCO_UcoObject):
    """
    A marking definition abstraction is a grouping of characteristics unique to the expression of a specific data marking conveying restrictions, permissions, and other guidance for how marked data can be used and shared. This class is an ontological structural abstraction for this concept. Implementations of this concept should utilize the marking:MarkingDefinition class.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/core/MarkingDefinitionAbstraction'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/core/MarkingDefinitionAbstraction"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_IdentityFacet(UCO_Facet):
    """
    An identity facet is a grouping of characteristics unique to a particular aspect of an identity.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/identity/IdentityFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/identity/IdentityFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Identity(UCO_IdentityAbstraction):
    """
    An identity is a grouping of identifying characteristics unique to an individual or organization.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/identity/Identity'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/identity/Identity"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ContextualCompilation(UCO_Compilation):
    """
    A contextual compilation is a grouping of things sharing some context (e.g., a set of network connections observed on a given day, all accounts associated with a given person).

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/core/ContextualCompilation'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/core/ContextualCompilation"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_EnclosingCompilation(UCO_Compilation):
    """
    An enclosing compilation is a container for a grouping of things.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/core/EnclosingCompilation'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/core/EnclosingCompilation"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Assertion(UCO_UcoObject):
    """
    An assertion is a statement declared to be true.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/core/Assertion'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/core/Assertion"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_AnalyticResultFacet(UCO_Facet):
    """
    An analytic result facet is a grouping of characteristics unique to the results of an analysis action.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/analysis/AnalyticResultFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/analysis/AnalyticResultFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ActionLifecycle(UCO_Action):
    """
    An action lifecycle is an action pattern consisting of an ordered set of multiple actions or subordinate action lifecycles.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/action/ActionLifecycle'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/action/ActionLifecycle"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_VictimTargeting(UCO_Victim):
    """
    A victim targeting is a grouping of characteristics unique to people or organizations that are the target of some malicious activity.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/victim/VictimTargeting'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/victim/VictimTargeting"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ThreadItem(CO_Item, UCO_UcoThing):
    """
    A ThreadItem is a member of a thread.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/types/ThreadItem'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/types/ThreadItem"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Thread(CO_Bag, UCO_UcoThing):
    """
    A semi-ordered array of items, that can be present in multiple copies.  Implemetation of a UCO Thread is similar to a Collections Ontology List, except a Thread may fork and merge - that is, one of its members may have two or more direct successors, and two or more direct predecessors.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/types/Thread'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {"https://ontology.unifiedcyberontology.org/uco/types/Thread"}
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Hash(UCO_UcoInherentCharacterizationThing):
    """
    A hash is a grouping of characteristics unique to the result of applying a mathematical algorithm that maps data of arbitrary size to a bit string (the 'hash') and is a one-way function, that is, a function which is practically infeasible to invert. This is commonly used for integrity checking of data. [based on https://en.wikipedia.org/wiki/Cryptographic_hash_function]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/types/Hash'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {"https://ontology.unifiedcyberontology.org/uco/types/Hash"}
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ControlledDictionaryEntry(UCO_DictionaryEntry):
    """
    A controlled dictionary entry is a single (term/key, value) pair where the term/key is constrained to an explicitly defined set of values.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/types/ControlledDictionaryEntry'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/types/ControlledDictionaryEntry"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ControlledDictionary(UCO_Dictionary):
    """
    A controlled dictionary is a list of (term/key, value) pairs where each term/key exists no more than once and is constrained to an explicitly defined set of values.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/types/ControlledDictionary'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/types/ControlledDictionary"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_MaliciousTool(UCO_Tool):
    """
    A malicious tool is an artifact of hardware and/or software utilized to accomplish a malevolent task or purpose.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/tool/MaliciousTool'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/tool/MaliciousTool"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_LibraryType(UCO_UcoInherentCharacterizationThing):
    """
    A library type is a grouping of characteristics unique to a collection of resources incorporated into the build of a software.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/tool/LibraryType'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/tool/LibraryType"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_DefensiveTool(UCO_Tool):
    """
    A defensive tool is an artifact of hardware and/or software utilized to accomplish a task or purpose of guarding.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/tool/DefensiveTool'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/tool/DefensiveTool"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ConfiguredTool(UCO_Tool):
    """
    A ConfiguredTool is a Tool that is known to be configured to run in a more specified manner than some unconfigured or less-configured Tool.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/tool/ConfiguredTool'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/tool/ConfiguredTool"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_CompilerType(UCO_UcoInherentCharacterizationThing):
    """
    A compiler type is a grouping of characteristics unique to a specific program that translates computer code written in one programming language (the source language) into another language (the target language). Typically a program that translates source code from a high-level programming language to a lower-level language (e.g., assembly language, object code, or machine code) to create an executable program. [based on https://en.wikipedia.org/wiki/Compiler]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/tool/CompilerType'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/tool/CompilerType"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_BuildUtilityType(UCO_UcoInherentCharacterizationThing):
    """
    A build utility type characterizes the tool used to convert from source code to executable code for a particular version of software.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/tool/BuildUtilityType'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/tool/BuildUtilityType"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_BuildInformationType(UCO_UcoInherentCharacterizationThing):
    """
    A build information type is a grouping of characteristics that describe how a particular version of software was converted from source code to executable code.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/tool/BuildInformationType'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/tool/BuildInformationType"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_BuildFacet(UCO_Facet):
    """
    A build facet is a grouping of characteristics unique to a particular version of a software.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/tool/BuildFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/tool/BuildFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_AnalyticTool(UCO_Tool):
    """
    An analytic tool is an artifact of hardware and/or software utilized to accomplish a task or purpose of explanation, interpretation or logical reasoning.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/tool/AnalyticTool'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/tool/AnalyticTool"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_MaliciousRole(UCO_Role):
    """
    A malicious role is a role with malevolent intent.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/role/MaliciousRole'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/role/MaliciousRole"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_BenevolentRole(UCO_Role):
    """
    A benevolent role is a role with positive and/or beneficial intent.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/role/BenevolentRole'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/role/BenevolentRole"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_PatternExpression(UCO_UcoInherentCharacterizationThing):
    """
    A pattern expression is a grouping of characteristics unique to an explicit logical expression defining a pattern (e.g., regular expression, SQL Select expression, etc.).

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/pattern/PatternExpression'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/pattern/PatternExpression"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_LogicalPattern(UCO_Pattern):
    """
    A logical pattern is a grouping of characteristics unique to an informational pattern expressed via a structured pattern expression following the rules of logic.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/pattern/LogicalPattern'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/pattern/LogicalPattern"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_X509V3ExtensionsFacet(UCO_Facet):
    """
    An X.509 v3 certificate extensions facet is a grouping of characteristics unique to a public key digital identity certificate conformant to the X.509 v3 PKI (Public Key Infrastructure) standard.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/X509V3ExtensionsFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/X509V3ExtensionsFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_X509V3Certificate(UCO_ObservableObject):
    """
    An X.509 v3 certificate is a public key digital identity certificate conformant to the X.509 v3 PKI (Public Key Infrastructure) standard.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/X509V3Certificate'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/X509V3Certificate"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_X509CertificateFacet(UCO_Facet):
    """
    A X.509 certificate facet is a grouping of characteristics unique to a public key digital identity certificate conformant to the X.509 PKI (Public Key Infrastructure) standard.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/X509CertificateFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/X509CertificateFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_X509Certificate(UCO_ObservableObject):
    """
    A X.509 certificate is a public key digital identity certificate conformant to the X.509 PKI (Public Key Infrastructure) standard.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/X509Certificate'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/X509Certificate"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WriteBlocker(UCO_Device):
    """
    A write blocker is a device that allows read-only access to storage mediums in order to preserve the integrity of the data being analyzed. Examples include Tableau, Cellibrite, Talon, etc.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WriteBlocker'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WriteBlocker"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WirelessNetworkConnectionFacet(UCO_Facet):
    """
    A wireless network connection facet is a grouping of characteristics unique to a connection (completed or attempted) across an IEEE 802.11 standards-conformant digital network (a group of two or more computer systems linked together). [based on https://www.webopedia.com/TERM/N/network.html]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WirelessNetworkConnectionFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WirelessNetworkConnectionFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WirelessNetworkConnection(UCO_NetworkConnection):
    """
    A wireless network connection is a connection (completed or attempted) across an IEEE 802.11 standards-confromant digital network (a group of two or more computer systems linked together). [based on https://www.webopedia.com/TERM/N/network.html]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WirelessNetworkConnection'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WirelessNetworkConnection"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WindowsWaitableTime(UCO_ObservableObject):
    """
    A Windows waitable timer is a synchronization object within the Windows operating system whose state is set to signaled when a specified due time arrives. There are two types of waitable timers that can be created: manual-reset and synchronization. A timer of either type can also be a periodic timer. [based on https://docs.microsoft.com/en-us/windows/win32/sync/waitable-timer-objects]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WindowsWaitableTime'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WindowsWaitableTime"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WindowsVolumeFacet(UCO_Facet):
    """
    A Windows volume facet is a grouping of characteristics unique to a single accessible storage area (volume) with a single Windows file system. [based on https://en.wikipedia.org/wiki/Volume_(computing)]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WindowsVolumeFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WindowsVolumeFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WindowsThreadFacet(UCO_Facet):
    """
    A Windows thread facet is a grouping os characteristics unique to a single thread of execution within a Windows process.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WindowsThreadFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WindowsThreadFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WindowsThread(UCO_ProcessThread):
    """
    A Windows thread is a single thread of execution within a Windows process.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WindowsThread'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WindowsThread"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WindowsTaskFacet(UCO_Facet):
    """
    A Windows Task facet is a grouping of characteristics unique to a Windows Task (a process that is scheduled to execute on a Windows operating system by the Windows Task Scheduler). [based on http://msdn.microsoft.com/en-us/library/windows/desktop/aa381311(v=vs.85).aspx]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WindowsTaskFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WindowsTaskFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WindowsTask(UCO_ObservableObject):
    """
    A Windows task is a process that is scheduled to execute on a Windows operating system by the Windows Task Scheduler. [based on http://msdn.microsoft.com/en-us/library/windows/desktop/aa381311(v=vs.85).aspx]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WindowsTask'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WindowsTask"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WindowsSystemRestore(UCO_ObservableObject):
    """
    A Windows system restore is a capture of a Windows computer's state (including system files, installed applications, Windows Registry, and system settings) at a particular point in time such that the computer can be reverted to that state in the event of system malfunctions or other problems. [based on https://en.wikipedia.org/wiki/System_Restore]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WindowsSystemRestore'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WindowsSystemRestore"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WindowsServiceFacet(UCO_Facet):
    """
    A Windows service facet is a grouping of characteristics unique to a specific Windows service (a computer program that operates in the background of a Windows operating system, similar to the way a UNIX daemon runs on UNIX). [based on https://en.wikipedia.org/wiki/Windows_service]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WindowsServiceFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WindowsServiceFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WindowsService(UCO_ObservableObject):
    """
    A Windows service is a specific Windows service (a computer program that operates in the background of a Windows operating system, similar to the way a UNIX daemon runs on UNIX). [based on https://en.wikipedia.org/wiki/Windows_service]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WindowsService'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WindowsService"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WindowsRegistryValue(UCO_UcoInherentCharacterizationThing):
    """
    A Windows registry value is a grouping of characteristics unique to a particular value within a Windows registry (a hierarchical database that stores low-level settings for the Microsoft Windows operating system and for applications that opt to use the registry. [based on https://en.wikipedia.org/wiki/Windows_Registry]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WindowsRegistryValue'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WindowsRegistryValue"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WindowsRegistryKeyFacet(UCO_Facet):
    """
    A Windows registry key facet is a grouping of characteristics unique to a particular key within a Windows registry (A hierarchical database that stores low-level settings for the Microsoft Windows operating system and for applications that opt to use the registry). [based on https://en.wikipedia.org/wiki/Windows_Registry]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WindowsRegistryKeyFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WindowsRegistryKeyFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WindowsRegistryKey(UCO_ObservableObject):
    """
    A Windows registry key is a particular key within a Windows registry (a hierarchical database that stores low-level settings for the Microsoft Windows operating system and for applications that opt to use the registry). [based on https://en.wikipedia.org/wiki/Windows_Registry]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WindowsRegistryKey'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WindowsRegistryKey"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WindowsRegistryHiveFacet(UCO_Facet):
    """
    A Windows registry hive facet is a grouping of characteristics unique to a particular logical group of keys, subkeys, and values in a Windows registry (a hierarchical database that stores low-level settings for the Microsoft Windows operating system and for applications that opt to use the registry). [based on https://en.wikipedia.org/wiki/Windows_Registry]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WindowsRegistryHiveFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WindowsRegistryHiveFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WindowsRegistryHive(UCO_ObservableObject):
    """
    The Windows registry hive is a particular logical group of keys, subkeys, and values in a Windows registry (a hierarchical database that stores low-level settings for the Microsoft Windows operating system and for applications that opt to use the registry). [based on https://en.wikipedia.org/wiki/Windows_Registry]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WindowsRegistryHive'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WindowsRegistryHive"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WindowsProcessFacet(UCO_Facet):
    """
    A Windows process facet is a grouping of characteristics unique to a program running on a Windows operating system.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WindowsProcessFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WindowsProcessFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WindowsProcess(UCO_Process):
    """
    A Windows process is a program running on a Windows operating system.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WindowsProcess'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WindowsProcess"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WindowsPrefetchFacet(UCO_Facet):
    """
    A Windows prefetch facet is a grouping of characteristics unique to entries in the Windows prefetch file (used to speed up application startup starting with Windows XP).

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WindowsPrefetchFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WindowsPrefetchFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WindowsPrefetch(UCO_ObservableObject):
    """
    The Windows prefetch contains entries in a Windows prefetch file (used to speed up application startup starting with Windows XP).

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WindowsPrefetch'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WindowsPrefetch"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WindowsPESection(UCO_UcoInherentCharacterizationThing):
    """
    A Windows PE section is a grouping of characteristics unique to a specific default or custom-defined region of a Windows PE (Portable Executable) file, consisting of an individual portion of the actual executable content of the file delineated according to unique purpose and memory protection requirements.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WindowsPESection'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WindowsPESection"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WindowsPEOptionalHeader(UCO_UcoInherentCharacterizationThing):
    """
    A Windows PE optional header is a grouping of characteristics unique to the 'optional header' of a Windows PE (Portable Executable) file, consisting of a collection of metadata about the executable code structure of the file.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WindowsPEOptionalHeader'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WindowsPEOptionalHeader"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WindowsPEFileHeader(UCO_UcoInherentCharacterizationThing):
    """
    A Windows PE file header is a grouping of characteristics unique to the 'header' of a Windows PE (Portable Executable) file, consisting of a collection of metadata about the overall nature and structure of the file.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WindowsPEFileHeader'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WindowsPEFileHeader"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WindowsPEBinaryFileFacet(UCO_Facet):
    """
    A Windows PE binary file facet is a grouping of characteristics unique to a Windows portable executable (PE) file.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WindowsPEBinaryFileFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WindowsPEBinaryFileFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WindowsPEBinaryFile(UCO_File):
    """
    A Windows PE binary file is a Windows portable executable (PE) file.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WindowsPEBinaryFile'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WindowsPEBinaryFile"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WindowsNetworkShare(UCO_ObservableObject):
    """
    A Windows network share is a Windows computer resource made available from one host to other hosts on a computer network. It is a device or piece of information on a computer that can be remotely accessed from another computer transparently as if it were a resource in the local machine. Network sharing is made possible by inter-process communication over the network. [based on https://en.wikipedia.org/wiki/Shared_resource]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WindowsNetworkShare'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WindowsNetworkShare"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WindowsMailslot(UCO_ObservableObject):
    """
    A Windows mailslot is is a pseudofile that resides in memory, and may be accessed using standard file functions. The data in a mailslot message can be in any form, but cannot be larger than 424 bytes when sent between computers. Unlike disk files, mailslots are temporary. When all handles to a mailslot are closed, the mailslot and all the data it contains are deleted. [based on https://docs.microsoft.com/en-us/windows/win32/ipc/about-mailslots]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WindowsMailslot'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WindowsMailslot"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WindowsHook(UCO_ObservableObject):
    """
    A Windows hook is a mechanism by which an application can intercept events, such as messages, mouse actions, and keystrokes within the Windows operating system. A function that intercepts a particular type of event is known as a hook procedure. A hook procedure can act on each event it receives, and then modify or discard the event. [based on https://docs.microsoft.com/en-us/windows/win32/winmsg/about-hooks]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WindowsHook'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WindowsHook"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WindowsHandle(UCO_ObservableObject):
    """
    A Windows handle is an abstract reference to a resource within the Windows operating system, such as a window, memory, an open file or a pipe. It is the mechanism by which applications interact with such resources in the Windows operating system.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WindowsHandle'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WindowsHandle"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WindowsFilemapping(UCO_ObservableObject):
    """
    A Windows file mapping is the association of a file's contents with a portion of the virtual address space of a process within a Windows operating system. The system creates a file mapping object (also known as a section object) to maintain this association. A file view is the portion of virtual address space that a process uses to access the file's contents. File mapping allows the process to use both random input and output (I/O) and sequential I/O. It also allows the process to work efficiently with a large data file, such as a database, without having to map the whole file into memory. Multiple processes can also use memory-mapped files to share data. Processes read from and write to the file view using pointers, just as they would with dynamically allocated memory. The use of file mapping improves efficiency because the file resides on disk, but the file view resides in memory.[based on https://docs.microsoft.com/en-us/windows/win32/memory/file-mapping]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WindowsFilemapping'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WindowsFilemapping"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WindowsEvent(UCO_ObservableObject):
    """
    A Windows event is a notification record of an occurance of interest (system, security, application, etc.) on a Windows operating system.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WindowsEvent'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WindowsEvent"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WindowsCriticalSection(UCO_ObservableObject):
    """
    A Windows critical section is a Windows object that provides synchronization similar to that provided by a mutex object, except that a critical section can be used only by the threads of a single process. Critical section objects cannot be shared across processes. Event, mutex, and semaphore objects can also be used in a single-process application, but critical section objects provide a slightly faster, more efficient mechanism for mutual-exclusion synchronization (a processor-specific test and set instruction). Like a mutex object, a critical section object can be owned by only one thread at a time, which makes it useful for protecting a shared resource from simultaneous access. Unlike a mutex object, there is no way to tell whether a critical section has been abandoned. [based on https://docs.microsoft.com/en-us/windows/win32/sync/critical-section-objects]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WindowsCriticalSection'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WindowsCriticalSection"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WindowsComputerSpecificationFacet(UCO_Facet):
    """
    A Windows computer specification facet is a grouping of characteristics unique to the hardware and software of a programmable electronic device that can store, retrieve, and process data running a Microsoft Windows operating system. [based on merriam-webster.com/dictionary/computer]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WindowsComputerSpecificationFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WindowsComputerSpecificationFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WindowsComputerSpecification(UCO_ObservableObject):
    """
    A Windows computer specification is the hardware ans software of a programmable electronic device that can store, retrieve, and process data running a Microsoft Windows operating system. [based on merriam-webster.com/dictionary/computer]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WindowsComputerSpecification'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WindowsComputerSpecification"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WindowsActiveDirectoryAccountFacet(UCO_Facet):
    """
    A Windows Active Directory account facet is a grouping of characteristics unique to an account managed by directory-based identity-related services of a Windows operating system.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WindowsActiveDirectoryAccountFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WindowsActiveDirectoryAccountFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WindowsActiveDirectoryAccount(UCO_DigitalAccount):
    """
    A Windows Active Directory account is an account managed by directory-based identity-related services of a Windows operating system.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WindowsActiveDirectoryAccount'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WindowsActiveDirectoryAccount"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WindowsAccountFacet(UCO_Facet):
    """
    A Windows account facet is a grouping of characteristics unique to a user account on a Windows operating system.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WindowsAccountFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WindowsAccountFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WindowsAccount(UCO_DigitalAccount):
    """
    A Windows account is a user account on a Windows operating system.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WindowsAccount'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WindowsAccount"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WikiArticle(UCO_ObservableObject):
    """
    A wiki article is one or more pages in a wiki focused on characterizing a particular topic.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WikiArticle'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WikiArticle"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Wiki(UCO_ObservableObject):
    """
    A wiki is an online hypertext publication collaboratively edited and managed by its own audience directly using a web browser. A typical wiki contains multiple pages/articles for the subjects or scope of the project and could be either open to the public or limited to use within an organization for maintaining its internal knowledge base. [based on https://en.wikipedia.org/wiki/Wiki]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/Wiki'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/Wiki"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WifiAddressFacet(UCO_MACAddressFacet):
    """
    A Wi-Fi address facet is a grouping of characteristics unique to a media access control (MAC) standards conformant identifier assigned to a device network interface to enable routing and management of IEEE 802.11 standards-conformant communications to and from that device.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WifiAddressFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WifiAddressFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WifiAddress(UCO_MACAddress):
    """
    A Wi-Fi address is a media access control (MAC) standards-conformant identifier assigned to a device network interface to enable routing and management of IEEE 802.11 standards-conformant communications to and from that device.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WifiAddress'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WifiAddress"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WhoisRegistrarInfoType(UCO_UcoInherentCharacterizationThing):
    """
    A Whois registrar info type is a grouping of characteristics unique to registrar-related information present in a response record conformant to the WHOIS protocol standard (RFC 3912). [based on https://en.wikipedia.org/wiki/WHOIS]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WhoisRegistrarInfoType'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WhoisRegistrarInfoType"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WhoisContactFacet(UCO_ContactFacet):
    """
    A Whois contact type is a grouping of characteristics unique to contact-related information present in a response record conformant to the WHOIS protocol standard (RFC 3912). [based on https://en.wikipedia.org/wiki/WHOIS]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WhoisContactFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WhoisContactFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WhoIsFacet(UCO_Facet):
    """
    A whois facet is a grouping of characteristics unique to a response record conformant to the WHOIS protocol standard (RFC 3912). [based on https://en.wikipedia.org/wiki/WHOIS]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WhoIsFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WhoIsFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WhoIs(UCO_ObservableObject):
    """
    WhoIs is a response record conformant to the WHOIS protocol standard (RFC 3912). [based on https://en.wikipedia.org/wiki/WHOIS]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WhoIs'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WhoIs"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WebPage(UCO_ObservableObject):
    """
    A web page is a specific collection of information provided by a website and displayed to a user in a web browser. A website typically consists of many web pages linked together in a coherent fashion. [based on https://en.wikipedia.org/wiki/Web_page]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WebPage'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WebPage"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_WearableDevice(UCO_SmartDevice):
    """
    A wearable device is an electronic device that is designed to be worn on a person's body.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/WearableDevice'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/WearableDevice"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_VolumeFacet(UCO_Facet):
    """
    A volume facet is a grouping of characteristics unique to a single accessible storage area (volume) with a single file system. [based on https://en.wikipedia.org/wiki/Volume_(computing)]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/VolumeFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/VolumeFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Volume(UCO_ObservableObject):
    """
    A volume is a single accessible storage area (volume) with a single file system. [based on https://en.wikipedia.org/wiki/Volume_(computing)]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/Volume'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/Volume"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ValuesEnumeratedEffectFacet(UCO_DefinedEffectFacet):
    """
    A values enumerated effect facet is a grouping of characteristics unique to the effects of actions upon observable objects where a value of the observable object is enumerated. An example of this would be the values of a registry key.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/ValuesEnumeratedEffectFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/ValuesEnumeratedEffectFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_UserSessionFacet(UCO_Facet):
    """
    A user session facet is a grouping of characteristics unique to a temporary and interactive information interchange between two or more communicating devices within the managed scope of a single user. [based on https://en.wikipedia.org/wiki/Session_(computer_science)]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/UserSessionFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/UserSessionFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_UserSession(UCO_ObservableObject):
    """
    A user session is a temporary and interactive information interchange between two or more communicating devices within the managed scope of a single user. [based on https://en.wikipedia.org/wiki/Session_(computer_science)]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/UserSession'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/UserSession"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_UserAccountFacet(UCO_Facet):
    """
    A user account facet is a grouping of characteristics unique to an account controlling a user's access to a network, system, or platform.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/UserAccountFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/UserAccountFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_UserAccount(UCO_DigitalAccount):
    """
    A user account is an account controlling a user's access to a network, system or platform.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/UserAccount'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/UserAccount"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_URLVisitFacet(UCO_Facet):
    """
    A URL visit facet is a grouping of characteristics unique to the properties of a visit of a URL within a particular browser.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/URLVisitFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/URLVisitFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_URLVisit(UCO_ObservableObject):
    """
    A URL visit characterizes the properties of a visit of a URL within a particular browser.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/URLVisit'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/URLVisit"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_URLHistoryFacet(UCO_Facet):
    """
    A URL history facet is a grouping of characteristics unique to the stored URL history for a particular web browser

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/URLHistoryFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/URLHistoryFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_URLHistoryEntry(UCO_UcoInherentCharacterizationThing):
    """
    A URL history entry is a grouping of characteristics unique to the properties of a single URL history entry for a particular browser.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/URLHistoryEntry'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/URLHistoryEntry"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_URLHistory(UCO_ObservableObject):
    """
    A URL history characterizes the stored URL history for a particular web browser

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/URLHistory'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/URLHistory"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_URLFacet(UCO_Facet):
    """
    A URL facet is a grouping of characteristics unique to a uniform resource locator (URL) acting as a resolvable address to a particular WWW (World Wide Web) accessible resource.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/URLFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/URLFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_URL(UCO_ObservableObject):
    """
    A URL is a uniform resource locator (URL) acting as a resolvable address to a particular WWW (World Wide Web) accessible resource.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/URL'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/URL"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_UNIXVolumeFacet(UCO_Facet):
    """
    A UNIX volume facet is a grouping of characteristics unique to a single accessible storage area (volume) with a single UNIX file system. [based on https://en.wikipedia.org/wiki/Volume_(computing)]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/UNIXVolumeFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/UNIXVolumeFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_UNIXProcessFacet(UCO_Facet):
    """
    A UNIX process facet is a grouping of characteristics unique to an instance of a computer program executed on a UNIX operating system.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/UNIXProcessFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/UNIXProcessFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_UNIXProcess(UCO_Process):
    """
    A UNIX process is an instance of a computer program executed on a UNIX operating system.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/UNIXProcess'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/UNIXProcess"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_UNIXFilePermissionsFacet(UCO_Facet):
    """
    A UNIX file permissions facet is a grouping of characteristics unique to the access rights (e.g., view, change, navigate, execute) of a file on a UNIX file system.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/UNIXFilePermissionsFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/UNIXFilePermissionsFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_UNIXFile(UCO_File):
    """
    A UNIX file is a file pertaining to the UNIX operating system.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/UNIXFile'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/UNIXFile"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_UNIXAccountFacet(UCO_Facet):
    """
    A UNIX account facet is a grouping of characteristics unique to an account on a UNIX operating system.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/UNIXAccountFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/UNIXAccountFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_UNIXAccount(UCO_DigitalAccount):
    """
    A UNIX account is an account on a UNIX operating system.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/UNIXAccount'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/UNIXAccount"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_TwitterProfileFacet(UCO_Facet):
    """
    A twitter profile facet is a grouping of characteristics unique to an explicit digital representation of identity and characteristics of the owner of a single Twitter user account. [based on https://en.wikipedia.org/wiki/User_profile]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/TwitterProfileFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/TwitterProfileFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Tweet(UCO_Message):
    """
    A tweet is message submitted by a Twitter user account to the Twitter microblogging platform.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/Tweet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/Tweet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_TriggerType(UCO_UcoInherentCharacterizationThing):
    """
    A trigger type is a grouping of characterizes unique to a set of criteria that, when met, starts the execution of a task within a Windows operating system. [based on https://docs.microsoft.com/en-us/windows/win32/taskschd/task-triggers]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/TriggerType'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/TriggerType"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_TaskActionType(UCO_UcoInherentCharacterizationThing):
    """
    A task action type is a grouping of characteristics for a scheduled action to be completed.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/TaskActionType'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/TaskActionType"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Tablet(UCO_Computer, UCO_MobileDevice, UCO_SmartDevice):
    """
    A tablet is a mobile computer that is primarily operated by touching the screen. (Devices categorized by their manufacturer as a Tablet)

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/Tablet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/Tablet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_TableFieldFacet(UCO_Facet):
    """
    A database record facet contains properties associated with a specific table record value from a database.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/TableFieldFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/TableFieldFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_TableField(UCO_ObservableObject):
    """
    A database table field and its associated value contained within a relational database.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/TableField'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/TableField"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_TCPConnectionFacet(UCO_Facet):
    """
    A TCP connection facet is a grouping of characteristics unique to portions of a network connection that are conformant to the Transmission Control Protocl (TCP) standard.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/TCPConnectionFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/TCPConnectionFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_TCPConnection(UCO_NetworkConnection):
    """
    A TCP connection is a network connection that is conformant to the Transfer

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/TCPConnection'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/TCPConnection"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_SymbolicLinkFacet(UCO_Facet):
    """
    A symbolic link facet is a grouping of characteristics unique to a file that contains a reference to another file or directory in the form of an absolute or relative path and that affects pathname resolution. [based on https://en.wikipedia.org/wiki/Symbolic_link]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/SymbolicLinkFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/SymbolicLinkFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_SymbolicLink(UCO_FileSystemObject):
    """
    A symbolic link is a file that contains a reference to another file or directory in the form of an absolute or relative path and that affects pathname resolution. [based on https://en.wikipedia.org/wiki/Symbolic_link]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/SymbolicLink'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/SymbolicLink"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_StorageMediumFacet(UCO_Facet):
    """
    A storage medium facet is a grouping of characteristics unique to a the storage capabilities of a piece of equipment or a mechanism designed to serve a special purpose or perform a special function.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/StorageMediumFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/StorageMediumFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_StorageMedium(UCO_Device):
    """
    A storage medium is any digital storage device that applies electromagnetic or optical surfaces, or depends solely on electronic circuits as solid state storage, for storing digital data. Examples include HDD (PATA), SATA, SSD, Optical, Memory_Card, Tape, etc

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/StorageMedium'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/StorageMedium"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_StateChangeEffectFacet(UCO_DefinedEffectFacet):
    """
    A state change effect facet is a grouping of characteristics unique to the effects of actions upon observable objects where a state of the observable object is changed.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/StateChangeEffectFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/StateChangeEffectFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_SoftwareFacet(UCO_Facet):
    """
    A software facet is a grouping of characteristics unique to a software program (a definitively scoped instance of a collection of data or computer instructions that tell the computer how to work). [based on https://en.wikipedia.org/wiki/Software]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/SoftwareFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/SoftwareFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_SocketAddress(UCO_Address):
    """
    A socket address (combining and IP address and a port number) is a composite identifier for a network socket endpoint supporting internet protocol communications.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/SocketAddress'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/SocketAddress"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Socket(UCO_FileSystemObject):
    """
    A socket is a special file used for inter-process communication, which enables communication between two processes. In addition to sending data, processes can send file descriptors across a Unix domain socket connection using the sendmsg() and recvmsg() system calls. Unlike named pipes which allow only unidirectional data flow, sockets are fully duplex-capable. [based on https://en.wikipedia.org/wiki/Unix_file_types]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/Socket'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/Socket"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Snapshot(UCO_FileSystemObject):
    """
    A snapshot is a file system object representing a snapshot of the contents of a part of a file system at a point in time.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/Snapshot'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/Snapshot"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ShopListing(UCO_ObservableObject):
    """
    A shop listing is a listing of offered products on an online marketplace/shop.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/ShopListing'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/ShopListing"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Server(UCO_Computer):
    """
    A server is a server rack-mount based computer, minicomputer, supercomputer, etc.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/Server'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/Server"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_SendControlCodeEffectFacet(UCO_DefinedEffectFacet):
    """
    A send control code effect facet is a grouping of characteristics unique to the effects of actions upon observable objects where a control code, or other control-oriented communication signal, is sent to the observable object. An example of this would be an action sending a control code changing the running state of a process.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/SendControlCodeEffectFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/SendControlCodeEffectFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Semaphore(UCO_ObservableObject):
    """
    A semaphore is a variable or abstract data type used to control access to a common resource by multiple processes and avoid critical section problems in a concurrent system such as a multitasking operating system. [based on https://en.wikipedia.org/wiki/Semaphore_(programming)]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/Semaphore'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/Semaphore"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_SecurityAppliance(UCO_Appliance):
    """
    A security appliance is a purpose-built computer with software or firmware that is designed to provide a specific security function to protect computer networks.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/SecurityAppliance'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/SecurityAppliance"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_SQLiteBlobFacet(UCO_Facet):
    """
    An SQLite blob facet is a grouping of characteristics unique to a blob (binary large object) of data within an SQLite database. [based on https://en.wikipedia.org/wiki/SQLite]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/SQLiteBlobFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/SQLiteBlobFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_SQLiteBlob(UCO_ObservableObject):
    """
    An SQLite blob is a blob (binary large object) of data within an SQLite database. [based on https://en.wikipedia.org/wiki/SQLite]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/SQLiteBlob'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/SQLiteBlob"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_SMSMessageFacet(UCO_Facet):
    """
    A SMS message facet is a grouping of characteristics unique to a message conformant to the short message service (SMS) communication protocol standards.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/SMSMessageFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/SMSMessageFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_SMSMessage(UCO_Message):
    """
    An SMS message is a message conformant to the short message service (SMS) communication protocol standards.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/SMSMessage'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/SMSMessage"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_SIPAddressFacet(UCO_DigitalAddressFacet):
    """
    A SIP address facet is a grouping of characteristics unique to a Session Initiation Protocol (SIP) standards conformant identifier assigned to a user to enable routing and management of SIP standards conformant communication to or from that user loosely coupled from any particular devices.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/SIPAddressFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/SIPAddressFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_SIPAddress(UCO_DigitalAddress):
    """
    A SIP address is an identifier for Session Initiation Protocol (SIP) communication.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/SIPAddress'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/SIPAddress"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_SIMCardFacet(UCO_Facet):
    """
    A SIM card facet is a grouping of characteristics unique to a subscriber identification module card intended to securely store the international mobile subscriber identity (IMSI) number and its related key, which are used to identify and authenticate subscribers on mobile telephony devices (such as mobile phones and computers). [based on https://en.wikipedia.org/wiki/SIM_card]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/SIMCardFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/SIMCardFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_SIMCard(UCO_Device):
    """
    A SIM card is a subscriber identification module card intended to securely store the international mobile subscriber identity (IMSI) number and its related key, which are used to identify and authenticate subscribers on mobile telephony. [based on https://en.wikipedia.org/wiki/SIM_card]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/SIMCard'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/SIMCard"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ReparsePoint(UCO_FileSystemObject):
    """
    A reparse point is a type of NTFS (New Technology File System) object which is an optional attribute of files and directories meant to define some sort of preprocessing before accessing the said file or directory. For instance reparse points can be used to redirect access to files which have been moved to long term storage so that some application would retrieve them and make them directly accessible. A reparse point contains a reparse tag and data that are interpreted by a filesystem filter identified by the tag. [based on https://jp-andre.pagesperso-orange.fr/junctions.html ; https://en.wikipedia.org/wiki/NTFS_reparse_point]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/ReparsePoint'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/ReparsePoint"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_RecoveredObjectFacet(UCO_Facet):
    """
    Recoverability status of name, metadata, and content.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/RecoveredObjectFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/RecoveredObjectFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_RecoveredObject(UCO_ObservableObject):
    """
    An observable object that was the result of a recovery operation.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/RecoveredObject'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/RecoveredObject"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_RasterPictureFacet(UCO_Facet):
    """
    A raster picture facet is a grouping of characteristics unique to a raster (or bitmap) image.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/RasterPictureFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/RasterPictureFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_RasterPicture(UCO_File):
    """
    A raster picture is a raster (or bitmap) image.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/RasterPicture'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/RasterPicture"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ProtocolConverter(UCO_Device):
    """
    A protocol converter is a device that converts from one protocol to another (e.g. SD to USB, SATA to USB, etc.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/ProtocolConverter'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/ProtocolConverter"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_PropertyReadEffectFacet(UCO_DefinedEffectFacet):
    """
    A properties read effect facet is a grouping of characteristics unique to the effects of actions upon observable objects where a characteristic is read from an observable object. An example of this would be the current running state of a process.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/PropertyReadEffectFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/PropertyReadEffectFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_PropertiesEnumeratedEffectFacet(UCO_DefinedEffectFacet, UCO_Facet):
    """
    A properties enumerated effect facet is a grouping of characteristics unique to the effects of actions upon observable objects where a characteristic of the observable object is enumerated. An example of this would be startup parameters for a process.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/PropertiesEnumeratedEffectFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/PropertiesEnumeratedEffectFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ProfileFacet(UCO_Facet):
    """
    A profile facet is a grouping of characteristics unique to an explicit digital representation of identity and characteristics of the owner of a single user account associated with an online service or application. [based on https://en.wikipedia.org/wiki/User_profile]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/ProfileFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/ProfileFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Profile(UCO_ObservableObject):
    """
    A profile is an explicit digital representation of identity and characteristics of the owner of a single user account associated with an online service or application. [based on https://en.wikipedia.org/wiki/User_profile]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/Profile'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/Profile"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ProcessFacet(UCO_Facet):
    """
    A process facet is a grouping of characteristics unique to an instance of a computer program executed on an operating system.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/ProcessFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/ProcessFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Post(UCO_Message):
    """
    A post is message submitted to an online discussion/publishing site (forum, blog, etc.).

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/Post'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/Post"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Pipe(UCO_ObservableObject):
    """
    A pipe is a mechanism for one-way inter-process communication using message passing where data written by one process is buffered by the operating system until it is read by the next process, and this uni-directional channel disappears when the processes are completed. [based on https://en.wikipedia.org/wiki/Pipeline_(Unix) ; https://en.wikipedia.org/wiki/Anonymous_pipe]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/Pipe'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/Pipe"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_PhoneAccountFacet(UCO_Facet):
    """
    A phone account facet is a grouping of characteristics unique to an arrangement with an entity to enable and control the provision of a telephony capability or service.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/PhoneAccountFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/PhoneAccountFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_PhoneAccount(UCO_DigitalAccount):
    """
    A phone account is an arrangement with an entity to enable and control the provision of a telephony capability or service.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/PhoneAccount'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/PhoneAccount"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_PaymentCard(UCO_ObservableObject):
    """
    A payment card is a physical token that is part of a payment system issued by financial institutions, such as a bank, to a customer that enables its owner (the cardholder) to access the funds in the customer's designated bank accounts, or through a credit account and make payments by electronic funds transfer and access automated teller machines (ATMs). [based on https://en.wikipedia.org/wiki/Payment_card]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/PaymentCard'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/PaymentCard"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_PathRelationFacet(UCO_Facet):
    """
    A path relation facet is a grouping of characteristics unique to the location of one object within another containing object.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/PathRelationFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/PathRelationFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_PDFFileFacet(UCO_Facet):
    """
    A PDF file facet is a grouping of characteristics unique to a PDF (Portable Document Format) file.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/PDFFileFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/PDFFileFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_PDFFile(UCO_File):
    """
    A PDF file is a Portable Document Format (PDF) file.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/PDFFile'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/PDFFile"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_OperatingSystemFacet(UCO_Facet):
    """
    An operating system facet is a grouping of characteristics unique to the software that manages computer hardware, software resources, and provides common services for computer programs. [based on https://en.wikipedia.org/wiki/Operating_system]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/OperatingSystemFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/OperatingSystemFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_OperatingSystem(UCO_ObservableObject):
    """
    An operating system is the software that manages computer hardware, software resources, and provides common services for computer programs. [based on https://en.wikipedia.org/wiki/Operating_system]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/OperatingSystem'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/OperatingSystem"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_OnlineServiceFacet(UCO_Facet):
    """
    An online service facet is a grouping of characteristics unique to a particular provision mechanism of information access, distribution or manipulation over the Internet.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/OnlineServiceFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/OnlineServiceFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_OnlineService(UCO_ObservableObject):
    """
    An online service is a particular provision mechanism of information access, distribution or manipulation over the Internet.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/OnlineService'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/OnlineService"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Observation(UCO_Action):
    """
    An observation is a temporal perception of an observable.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/Observation'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/Observation"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ObservableRelationship(UCO_Observable, UCO_Relationship):
    """
    An observable relationship is a grouping of characteristics unique to an assertion of an association between two observable objects.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/ObservableRelationship'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/ObservableRelationship"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ObservablePattern(UCO_Observable):
    """
    An observable pattern is a grouping of characteristics unique to a logical pattern composed of observable object and observable action properties.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/ObservablePattern'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/ObservablePattern"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ObservableAction(UCO_Action, UCO_Observable):
    """
    An observable action is a grouping of characteristics unique to something that may be done or performed within the digital domain.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/ObservableAction'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/ObservableAction"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_NoteFacet(UCO_Facet):
    """
    A note facet is a grouping of characteristics unique to a brief textual record.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/NoteFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/NoteFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Note(UCO_ObservableObject):
    """
    A note is a brief textual record.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/Note'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/Note"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_NetworkSubnet(UCO_ObservableObject):
    """
    A network subnet is a logical subdivision of an IP network. [based on https://en.wikipedia.org/wiki/Subnetwork]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/NetworkSubnet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/NetworkSubnet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_NetworkRoute(UCO_ObservableObject):
    """
    A network route is a specific path (of specific network nodes, connections and protocols) for traffic in a network or between or across multiple networks.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/NetworkRoute'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/NetworkRoute"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_NetworkProtocol(UCO_ObservableObject):
    """
    A network protocol is an established set of structured rules that determine how data is transmitted between different devices in the same network. Essentially, it allows connected devices to communicate with each other, regardless of any differences in their internal processes, structure or design. [based on https://www.comptia.org/content/guides/what-is-a-network-protocol]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/NetworkProtocol'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/NetworkProtocol"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_NetworkInterfaceFacet(UCO_Facet):
    """
    A network interface facet is a grouping of characteristics unique to a software or hardware interface between two pieces of equipment or protocol layers in a computer network.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/NetworkInterfaceFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/NetworkInterfaceFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_NetworkInterface(UCO_ObservableObject):
    """
    A network interface is a software or hardware interface between two pieces of equipment or protocol layers in a computer network.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/NetworkInterface'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/NetworkInterface"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_NetworkFlowFacet(UCO_Facet):
    """
    A network flow facet is a grouping of characteristics unique to a sequence of data transiting one or more digital network (a group of two or more computer systems linked together) connections. [based on https://www.webopedia.com/TERM/N/network.html]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/NetworkFlowFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/NetworkFlowFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_NetworkFlow(UCO_ObservableObject):
    """
    A network flow is a sequence of data transiting one or more digital network (a group or two or more computer systems linked together) connections. [based on https://www.webopedia.com/TERM/N/network.html]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/NetworkFlow'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/NetworkFlow"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_NetworkConnectionFacet(UCO_Facet):
    """
    A network connection facet is a grouping of characteristics unique to a connection (complete or attempted) accross a digital network (a group of two or more computer systems linked together). [based on https://www.webopedia.com/TERM/N/network.html]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/NetworkConnectionFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/NetworkConnectionFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_NetworkAppliance(UCO_Appliance):
    """
    A network appliance is a purpose-built computer with software or firmware that is designed to provide a specific network management function.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/NetworkAppliance'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/NetworkAppliance"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_NamedPipe(UCO_FileSystemObject):
    """
    A named pipe is a mechanism for FIFO (first-in-first-out) inter-process communication. It is persisted as a filesystem object (that can be deleted like any other file), can be written to or read from by any process and exists beyond the lifespan of any process interacting with it (unlike simple anonymous pipes). [based on https://en.wikipedia.org/wiki/Named_pipe]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/NamedPipe'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/NamedPipe"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_NTFSFilePermissionsFacet(UCO_Facet):
    """
    An NTFS file permissions facet is a grouping of characteristics unique to the access rights (e.g., view, change, navigate, execute) of a file on an NTFS (new technology filesystem) file system.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/NTFSFilePermissionsFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/NTFSFilePermissionsFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_NTFSFileFacet(UCO_Facet):
    """
    An NTFS file facet is a grouping of characteristics unique to a file on an NTFS (new technology filesystem) file system.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/NTFSFileFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/NTFSFileFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_NTFSFile(UCO_File):
    """
    An NTFS file is a New Technology File System (NTFS) file.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/NTFSFile'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/NTFSFile"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_MutexFacet(UCO_Facet):
    """
    A mutex facet is a grouping of characteristics unique to a mechanism that enforces limits on access to a resource when there are many threads of execution. A mutex is designed to enforce a mutual exclusion concurrency control policy, and with a variety of possible methods there exists multiple unique implementations for different applications. [based on https://en.wikipedia.org/wiki/Lock_(computer_science)]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/MutexFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/MutexFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Mutex(UCO_ObservableObject):
    """
    A mutex is a mechanism that enforces limits on access to a resource when there are many threads of execution. A mutex is designed to enforce a mutual exclusion concurrency control policy, and with a variety of possible methods there exists multiple unique implementations for different applications. [based on https://en.wikipedia.org/wiki/Lock_(computer_science)]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/Mutex'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/Mutex"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_MobileDeviceFacet(UCO_Facet):
    """
    A mobile device facet is a grouping of characteristics unique to a portable computing device. [based on https://www.lexico.com/definition/mobile_device]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/MobileDeviceFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/MobileDeviceFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_MobileAccountFacet(UCO_Facet):
    """
    A mobile account facet is a grouping of characteristics unique to an arrangement with an entity to enable and control the provision of some capability or service on a portable computing device. [based on https://www.lexico.com/definition/mobile_device]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/MobileAccountFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/MobileAccountFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_MobileAccount(UCO_DigitalAccount):
    """
    A mobile account is an arrangement with an entity to enable and control the provision of some capability or service on a portable computing device. [based on https://www.lexico.com/definition/mobile_device]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/MobileAccount'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/MobileAccount"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_MimePartType(UCO_UcoInherentCharacterizationThing):
    """
    A mime part type is a grouping of characteristics unique to a component of a multi-part email body.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/MimePartType'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/MimePartType"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_MftRecordFacet(UCO_Facet):
    """
    An MFT record facet is a grouping of characteristics unique to the details of a single file as managed in an NTFS (new technology filesystem) master file table (which is a collection of information about all files on an NTFS filesystem). [based on https://docs.microsoft.com/en-us/windows/win32/devnotes/master-file-table]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/MftRecordFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/MftRecordFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_MessageThreadFacet(UCO_Facet):
    """
    A message thread facet is a grouping of characteristics unique to a running commentary of electronic messages pertaining to one topic or question.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/MessageThreadFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/MessageThreadFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_MessageThread(UCO_ObservableObject):
    """
    A message thread is a running commentary of electronic messages pertaining to one topic or question.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/MessageThread'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/MessageThread"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_MessageFacet(UCO_Facet):
    """
    A message facet is a grouping of characteristics unique to a discrete unit of electronic communication intended by the source for consumption by some recipient or group of recipients. [based on https://en.wikipedia.org/wiki/Message]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/MessageFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/MessageFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_MemoryFacet(UCO_Facet):
    """
    A memory facet is a grouping of characteristics unique to a particular region of temporary information storage (e.g., RAM (random access memory), ROM (read only memory)) on a digital device.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/MemoryFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/MemoryFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Memory(UCO_ObservableObject):
    """
    Memory is a particular region of temporary information storage (e.g., RAM (random access memory), ROM (read only memory)) on a digital device.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/Memory'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/Memory"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_LibraryFacet(UCO_Facet):
    """
    A library facet is a grouping of characteristics unique to a suite of data and programming code that is used to develop software programs and applications. [based on https://www.techopedia.com/definition/3828/software-library]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/LibraryFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/LibraryFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Library(UCO_ObservableObject):
    """
    A library is a suite of data and programming code that is used to develop software programs and applications. [based on https://www.techopedia.com/definition/3828/software-library]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/Library'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/Library"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Laptop(UCO_Computer):
    """
    A laptop, laptop computer, or notebook computer is a small, portable personal computer with a screen and alphanumeric keyboard. These typically have a clam shell form factor with the screen mounted on the inside of the upper lid and the keyboard on the inside of the lower lid, although 2-in-1 PCs with a detachable keyboard are often marketed as laptops or as having a laptop mode. (Devices categorized by their manufacturer as a Laptop)

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/Laptop'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/Laptop"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Junction(UCO_FileSystemObject):
    """
    A junction is a specific NTFS (New Technology File System) reparse point to redirect a directory access to another directory which can be on the same volume or another volume. A junction is similar to a directory symbolic link but may differ on whether they are processed on the local system or on the remote file server. [based on https://jp-andre.pagesperso-orange.fr/junctions.html]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/Junction'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/Junction"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_InstantMessagingAddressFacet(UCO_DigitalAddressFacet):
    """
    An instant messaging address facet is a grouping of characteristics unique to an identifier assigned to enable routing and management of instant messaging digital communication.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/InstantMessagingAddressFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/InstantMessagingAddressFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_InstantMessagingAddress(UCO_DigitalAddress):
    """


    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/InstantMessagingAddress'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/InstantMessagingAddress"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ImageFacet(UCO_Facet):
    """
    An image facet is a grouping of characteristics unique to a complete copy of a hard disk, memory, or other digital media.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/ImageFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/ImageFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Image(UCO_ObservableObject):
    """
    An image is a complete copy of a hard disk, memory, or other digital media.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/Image'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/Image"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_IShowMessageActionType(UCO_UcoInherentCharacterizationThing):
    """
    An IShow message action type is a grouping of characteristics unique to an action that shows a message box when a task is activate. [based on https://docs.microsoft.com/en-us/windows/win32/api/taskschd/nn-taskschd-ishowmessageaction?redirectedfrom=MSDN]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/IShowMessageActionType'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/IShowMessageActionType"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_IPv6AddressFacet(UCO_IPAddressFacet):
    """
    An IPv6 (Internet Protocol version 6) address facet is a grouping of characteristics unique to an IPv6 standards conformant identifier assigned to a device to enable routing and management of IPv6 standards conformant communication to or from that device.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/IPv6AddressFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/IPv6AddressFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_IPv6Address(UCO_IPAddress):
    """
    An IPv6 (Internet Protocol version 6) address is an IPv6 standards conformant identifier assigned to a device to enable routing and management of IPv6 standards conformant communication to or from that device.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/IPv6Address'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/IPv6Address"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_IPv4AddressFacet(UCO_IPAddressFacet):
    """
    An IPv4 (Internet Protocol version 4) address facet is a grouping of characteristics unique to an IPv4 standards conformant identifier assigned to a device to enable routing and management of IPv4 standards conformant communication to or from that device.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/IPv4AddressFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/IPv4AddressFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_IPv4Address(UCO_IPAddress):
    """
    An IPv4 (Internet Protocol version 4) address is an IPv4 standards conformant identifier assigned to a device to enable routing and management of IPv4 standards conformant communication to or from that device.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/IPv4Address'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/IPv4Address"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_IPhone(UCO_AppleDevice, UCO_SmartPhone):
    """
    An iPhone is a smart phone that applies the iOS mobile operating system.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/IPhone'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/IPhone"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_IPNetmask(UCO_ObservableObject):
    """
    An IP netmask is a 32-bit 'mask' used to divide an IP address into subnets and specify the network's available hosts.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/IPNetmask'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/IPNetmask"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_IExecActionType(UCO_UcoInherentCharacterizationThing):
    """
    An IExec action type is a grouping of characteristics unique to an action that executes a command-line operation on a Windows operating system. [based on https://docs.microsoft.com/en-us/windows/win32/api/taskschd/nn-taskschd-iexecaction?redirectedfrom=MSDN]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/IExecActionType'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/IExecActionType"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_IComHandlerActionType(UCO_UcoInherentCharacterizationThing):
    """
    An IComHandler action type is a grouping of characteristics unique to a Windows Task-related action that fires a Windows COM handler (smart code in the client address space that can optimize calls between a client and server). [based on https://docs.microsoft.com/en-us/windows/win32/taskschd/comhandleraction]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/IComHandlerActionType'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/IComHandlerActionType"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ICMPConnectionFacet(UCO_Facet):
    """
    An ICMP connection facet is a grouping of characteristics unique to portions of a network connection that are conformant to the Internet Control Message Protocol (ICMP) standard.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/ICMPConnectionFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/ICMPConnectionFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ICMPConnection(UCO_NetworkConnection):
    """
    An ICMP connection is a network connection that is conformant to the Internet Control Message Protocol (ICMP) standard.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/ICMPConnection'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/ICMPConnection"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Hostname(UCO_ObservableObject):
    """
    A hostname is a label that is assigned to a device connected to a computer network and that is used to identify the device in various forms of electronic communication, such as the World Wide Web. A hostname may be a domain name, if it is properly organized into the domain name system. A domain name may be a hostname if it has been assigned to an Internet host and associated with the host's IP address. [based on https://en.wikipedia.org/wiki/Hostname]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/Hostname'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/Hostname"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_HTTPConnectionFacet(UCO_Facet):
    """
    An HTTP connection facet is a grouping of characteristics unique to portions of a network connection that are conformant to the Hypertext Transfer Protocol (HTTP) standard.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/HTTPConnectionFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/HTTPConnectionFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_HTTPConnection(UCO_NetworkConnection):
    """
    An HTTP connection is network connection that is conformant to the Hypertext Transfer Protocol (HTTP) standard.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/HTTPConnection'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/HTTPConnection"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_GlobalFlagType(UCO_UcoInherentCharacterizationThing):
    """
    A global flag type is a grouping of characteristics unique to the Windows systemwide global variable named NtGlobalFlag that enables various internal debugging, tracing, and validation support in the operating system. [based on "Windows Global Flags, Chapter 3: System Mechanisms of Windows Internals by Solomon, Russinovich, and Ionescu]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/GlobalFlagType'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/GlobalFlagType"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_GeoLocationTrackFacet(UCO_Facet):
    """
    A geolocation track facet is a grouping of characteristics unique to a set of contiguous geolocation entries representing a path/track taken.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/GeoLocationTrackFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/GeoLocationTrackFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_GeoLocationTrack(UCO_ObservableObject):
    """
    A geolocation track is a set of contiguous geolocation entries representing a path/track taken.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/GeoLocationTrack'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/GeoLocationTrack"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_GeoLocationLogFacet(UCO_Facet):
    """
    A geolocation log facet is a grouping of characteristics unique to a record containing geolocation tracks and/or geolocation entries.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/GeoLocationLogFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/GeoLocationLogFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_GeoLocationLog(UCO_ObservableObject):
    """
    A geolocation log is a record containing geolocation tracks and/or geolocation entries.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/GeoLocationLog'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/GeoLocationLog"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_GeoLocationEntryFacet(UCO_Facet):
    """
    A geolocation entry facet is a grouping of characteristics unique to a single application-specific geolocation entry.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/GeoLocationEntryFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/GeoLocationEntryFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_GeoLocationEntry(UCO_ObservableObject):
    """
    A geolocation entry is a single application-specific geolocation entry.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/GeoLocationEntry'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/GeoLocationEntry"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_GenericObservableObject(UCO_ObservableObject):
    """
    A generic observable object is an article or unit within the digital domain.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/GenericObservableObject'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/GenericObservableObject"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_GamingConsole(UCO_Device):
    """
    A gaming console (video game console or game console) is an electronic system that connects to a display, typically a TV or computer monitor, for the primary purpose of playing video games.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/GamingConsole'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/GamingConsole"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_GUI(UCO_ObservableObject):
    """
    A GUI is a graphical user interface that allows users to interact with electronic devices through graphical icons and audio indicators such as primary notation, instead of text-based user interfaces, typed command labels or text navigation. [based on https://en.wikipedia.org/wiki/Graphical_user_interface]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/GUI'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/GUI"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_FragmentFacet(UCO_Facet):
    """
    A fragment facet is a grouping of characteristics unique to an individual piece of the content of a file.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/FragmentFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/FragmentFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ForumPrivateMessage(UCO_Message):
    """
    A forum private message (aka PM or DM (direct message)) is a one-to-one message from one specific user account to another specific user account on an online form where transmission is managed by the online forum platform and the message is only viewable by the parties directly involved.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/ForumPrivateMessage'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/ForumPrivateMessage"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ForumPost(UCO_Message):
    """
    A forum post is message submitted by a user account to an online forum where the message content (and typically metadata including who posted it and when) is viewable by any party with viewing permissions on the forum.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/ForumPost'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/ForumPost"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_FileSystemFacet(UCO_Facet):
    """
    A file system facet is a grouping of characteristics unique to the process that manages how and where data on a storage medium is stored, accessed and managed. [based on https://www.techopedia.com/definition/5510/file-system]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/FileSystemFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/FileSystemFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_FileSystem(UCO_ObservableObject):
    """
    A file system is the process that manages how and where data on a storage medium is stored, accessed and managed. [based on https://www.techopedia.com/definition/5510/file-system]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/FileSystem'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/FileSystem"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_FilePermissionsFacet(UCO_Facet):
    """
    A file permissions facet is a grouping of characteristics unique to the access rights (e.g., view, change, navigate, execute) of a file on a file system.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/FilePermissionsFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/FilePermissionsFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_FileFacet(UCO_Facet):
    """
    A file facet is a grouping of characteristics unique to the storage of a file (computer resource for recording data discretely in a computer storage device) on a file system (process that manages how and where data on a storage device is stored, accessed and managed). [based on https://en.wikipedia.org/Computer_file and https://www.techopedia.com/definition/5510/file-system]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/FileFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/FileFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ExtractedStringsFacet(UCO_Facet):
    """
    An extracted strings facet is a grouping of characteristics unique to one or more sequences of characters pulled from an observable object.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/ExtractedStringsFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/ExtractedStringsFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ExtractedString(UCO_UcoInherentCharacterizationThing):
    """
    An extracted string is a grouping of characteristics unique to a series of characters pulled from an observable object.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/ExtractedString'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/ExtractedString"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ExtInodeFacet(UCO_Facet):
    """
    An extInode facet is a grouping of characteristics unique to a file system object (file, directory, etc.) conformant to the extended file system (EXT or related derivations) specification.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/ExtInodeFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/ExtInodeFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_EventRecordFacet(UCO_Facet):
    """
    An event record facet is a grouping of characteristics unique to something that happens in a digital context (e.g., operating system events).

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/EventRecordFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/EventRecordFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_EventRecord(UCO_ObservableObject):
    """
    An event record is something that happens in a digital context (e.g., operating system events).

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/EventRecord'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/EventRecord"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_EventLog(UCO_ObservableObject):
    """
    An event log is a collection of event records.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/EventLog'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/EventLog"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_EnvironmentVariable(UCO_UcoInherentCharacterizationThing):
    """
    An environment variable is a grouping of characteristics unique to a dynamic-named value that can affect the way running processes will behave on a computer. [based on https://en.wikipedia.org/wiki/Environment_variable]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/EnvironmentVariable'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/EnvironmentVariable"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_EncryptedStreamFacet(UCO_Facet):
    """
    An encrypted stream facet is a grouping of characteristics unique to the conversion of a body of data content from one form to another obfuscated form in such a way that reversing the conversion to obtain the original data form can only be accomplished through possession and use of a specific key.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/EncryptedStreamFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/EncryptedStreamFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_EncodedStreamFacet(UCO_Facet):
    """
    An encoded stream facet is a grouping of characteristics unique to the conversion of a body of data content from one form to another form.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/EncodedStreamFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/EncodedStreamFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_EmbeddedDevice(UCO_Device):
    """
    An embedded device is a highly specialized microprocessor device meant for one or very few specific purposes and is usually embedded or included within another object or as part of a larger system. Examples include answer machine, door access logger, card scanner, etc.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/EmbeddedDevice'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/EmbeddedDevice"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_EmailMessageFacet(UCO_Facet):
    """
    An email message facet is a grouping of characteristics unique to a message that is an instance of an electronic mail correspondence conformant to the internet message format described in RFC 5322 and related RFCs.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/EmailMessageFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/EmailMessageFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_EmailMessage(UCO_Message):
    """
    An email message is a message that is an instance of an electronic mail correspondence conformant to the internet message format described in RFC 5322 and related RFCs.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/EmailMessage'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/EmailMessage"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_EmailAddressFacet(UCO_DigitalAddressFacet):
    """
    An email address facet is a grouping of characteristics unique to an identifier for an electronic mailbox to which electronic mail messages (conformant to the Simple Mail Transfer Protocol (SMTP)) are sent from and delivered to.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/EmailAddressFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/EmailAddressFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_EmailAddress(UCO_DigitalAddress):
    """
    An email address is an identifier for an electronic mailbox to which electronic mail messages (conformant to the Simple Mail Transfer Protocol (SMTP)) are sent from and delivered to.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/EmailAddress'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/EmailAddress"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_EmailAccountFacet(UCO_Facet):
    """
    An email account facet is a grouping of characteristics unique to an arrangement with an entity to enable and control the provision of electronic mail (email) capabilities or services.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/EmailAccountFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/EmailAccountFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_EmailAccount(UCO_DigitalAccount):
    """
    An email account is an arrangement with an entity to enable and control the provision of electronic mail (email) capabilities or services.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/EmailAccount'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/EmailAccount"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_EXIFFacet(UCO_Facet):
    """
    An EXIF (exchangeable image file format) facet is a grouping of characteristics unique to the formats for images, sound, and ancillary tags used by digital cameras (including smartphones), scanners and other systems handling image and sound files recorded by digital cameras conformant to JEIDA/JEITA/CIPA specifications. [based on https://en.wikipedia.org/wiki/Exif]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/EXIFFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/EXIFFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Drone(UCO_MobileDevice):
    """
    A drone, unmanned aerial vehicle (UAV), is an aircraft without a human pilot, crew, or passengers that typically involve a ground-based controller and a system for communications with the UAV.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/Drone'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/Drone"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_DomainNameFacet(UCO_Facet):
    """
    A domain name facet is a grouping of characteristics unique to an identification string that defines a realm of administrative autonomy, authority or control within the Internet. [based on https://en.wikipedia.org/wiki/Domain_name]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/DomainNameFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/DomainNameFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_DomainName(UCO_ObservableObject):
    """
    A domain name is an identification string that defines a realm of administrative autonomy, authority or control within the Internet. [based on https://en.wikipedia.org/wiki/Domain_name]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/DomainName'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/DomainName"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_DiskPartitionFacet(UCO_Facet):
    """
    A disk partition facet is a grouping of characteristics unique to a particular managed region on a storage mechanism.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/DiskPartitionFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/DiskPartitionFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_DiskPartition(UCO_ObservableObject):
    """
    A disk partition is a particular managed region on a storage mechanism where data is recorded by various electronic, magnetic, optical, or mechanical changes to a surface layer of one or more rotating disks. [based on https://en.wikipedia.org/wiki/Disk_storage]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/DiskPartition'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/DiskPartition"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_DiskFacet(UCO_Facet):
    """
    A disk facet is a grouping of characteristics unique to a storage mechanism where data is recorded by various electronic, magnetic, optical, or mechanical changes to a surface layer of one or more rotating disks.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/DiskFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/DiskFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Disk(UCO_ObservableObject):
    """
    A disk is a storage mechanism where data is recorded by various electronic, magnetic, optical, or mechanical changes to a surface layer of one or more rotating disks.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/Disk'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/Disk"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Directory(UCO_FileSystemObject):
    """
    A directory is a file system cataloging structure which contains references to other computer files, and possibly other directories. On many computers, directories are known as folders, or drawers, analogous to a workbench or the traditional office filing cabinet. In UNIX a directory is implemented as a special file. [based on https://en.wikipedia.org/wiki/Directory_(computing)]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/Directory'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/Directory"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_DigitalSignatureInfoFacet(UCO_Facet):
    """
    A digital signature info facet is a grouping of characteristics unique to a value calculated via a mathematical scheme for demonstrating the authenticity of an electronic message or document.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/DigitalSignatureInfoFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/DigitalSignatureInfoFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_DigitalSignatureInfo(UCO_ObservableObject):
    """
    A digital signature info is a value calculated via a mathematical scheme for demonstrating the authenticity of an electronic message or document.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/DigitalSignatureInfo'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/DigitalSignatureInfo"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_DigitalCamera(UCO_Device):
    """
    A digital camera is a camera that captures photographs in digital memory as opposed to capturing images on photographic film.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/DigitalCamera'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/DigitalCamera"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_DigitalAccountFacet(UCO_Facet):
    """
    A digital account facet is a grouping of characteristics unique to an arrangement with an entity to enable and control the provision of some capability or service within the digital domain.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/DigitalAccountFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/DigitalAccountFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_DeviceFacet(UCO_Facet):
    """
    A device facet is a grouping of characteristics unique to a piece of equipment or a mechanism designed to serve a special purpose or perform a special function. [based on https://www.merriam-webster.com/dictionary/device]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/DeviceFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/DeviceFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_DataRangeFacet(UCO_Facet):
    """
    A data range facet is a grouping of characteristics unique to a particular contiguous scope within a block of digital data.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/DataRangeFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/DataRangeFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_DNSRecord(UCO_ObservableObject):
    """
    A DNS record is a single Domain Name System (DNS) artifact specifying information of a particular type (routing, authority, responsibility, security, etc.) for a specific Internet domain name.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/DNSRecord'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/DNSRecord"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_DNSCache(UCO_ObservableObject):
    """
    An DNS cache is a temporary locally stored collection of previous Domain Name System (DNS) query results (created when an domain name is resolved to a IP address) for a particular computer.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/DNSCache'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/DNSCache"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_CredentialDump(UCO_ObservableObject):
    """
    A credential dump is a collection (typically forcibly extracted from a system) of specific login and password combinations for authorization of access to a digital account or system.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/CredentialDump'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/CredentialDump"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Credential(UCO_ObservableObject):
    """
    A credential is a single specific login and password combination for authorization of access to a digital account or system.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/Credential'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/Credential"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_CookieHistory(UCO_ObservableObject):
    """
    A cookie history is the stored web cookie history for a particular web browser.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/CookieHistory'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/CookieHistory"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ContentDataFacet(UCO_Facet):
    """
    A content data facet is a grouping of characteristics unique to a block of digital data.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/ContentDataFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/ContentDataFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)
        self._hashes: typing.List[UCO_Hash] = []

    def add_hash(self, hash: UCO_Hash) -> None:
        self.hashes.append(hash)
        self.graph.add((self.node, NS_UCO_OBSERVABLE.hash, hash.node))

    @property
    def hashes(self) -> typing.List[UCO_Hash]:
        return self._hashes


class UCO_ContentData(UCO_ObservableObject):
    """
    Content data is a block of digital data.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/ContentData'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/ContentData"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ContactURL(UCO_UcoInherentCharacterizationThing):
    """
    A contact URL is a grouping of characteristics unique to details for contacting a contact entity by Uniform Resource Locator (URL).

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/ContactURL'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/ContactURL"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ContactSIP(UCO_UcoInherentCharacterizationThing):
    """
    A contact SIP is a grouping of characteristics unique to details for contacting a contact entity by Session Initiation Protocol (SIP).

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/ContactSIP'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/ContactSIP"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ContactProfile(UCO_UcoInherentCharacterizationThing):
    """
    A contact profile is a grouping of characteristics unique to details for contacting a contact entity by online service.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/ContactProfile'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/ContactProfile"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ContactPhone(UCO_UcoInherentCharacterizationThing):
    """
    A contact phone is a grouping of characteristics unique to details for contacting a contact entity by telephone.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/ContactPhone'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/ContactPhone"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ContactMessaging(UCO_UcoInherentCharacterizationThing):
    """
    A contact messaging is a grouping of characteristics unique to details for contacting a contact entity by digital messaging.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/ContactMessaging'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/ContactMessaging"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ContactListFacet(UCO_Facet):
    """
    A contact list facet is a grouping of characteristics unique to a set of multiple individual contacts such as that found in a digital address book.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/ContactListFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/ContactListFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ContactList(UCO_ObservableObject):
    """
    A contact list is a set of multiple individual contacts such as that found in a digital address book.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/ContactList'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/ContactList"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ContactEmail(UCO_UcoInherentCharacterizationThing):
    """
    A contact email is a grouping of characteristics unique to details for contacting a contact entity by email.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/ContactEmail'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/ContactEmail"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ContactAffiliation(UCO_UcoInherentCharacterizationThing):
    """
    A contact affiliation is a grouping of characteristics unique to details of an organizational affiliation for a single contact entity.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/ContactAffiliation'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/ContactAffiliation"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ContactAddress(UCO_UcoInherentCharacterizationThing):
    """
    A contact address is a grouping of characteristics unique to a geolocation address of a contact entity.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/ContactAddress'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/ContactAddress"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Contact(UCO_ObservableObject):
    """
    A contact is a set of identification and communication related details for a single entity.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/Contact'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/Contact"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ConfiguredSoftware(UCO_Software):
    """
    A ConfiguredSoftware is a Software that is known to be configured to run in a more specified manner than some unconfigured or less-configured Software.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/ConfiguredSoftware'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/ConfiguredSoftware"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ComputerSpecificationFacet(UCO_Facet):
    """
    A computer specificaiton facet is a grouping of characteristics unique to the hardware and software of a programmable electronic device that can store, retrieve, and process data. [based on merriam-webster.com/dictionary/computer]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/ComputerSpecificationFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/ComputerSpecificationFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ComputerSpecification(UCO_ObservableObject):
    """
    A computer specification is the hardware and software of a programmable electronic device that can store, retrieve, and process data. {based on merriam-webster.com/dictionary/computer]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/ComputerSpecification'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/ComputerSpecification"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_CompressedStreamFacet(UCO_Facet):
    """
    A compressed stream facet is a grouping of characteristics unique to the application of a size-reduction process to a body of data content.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/CompressedStreamFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/CompressedStreamFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Code(UCO_ObservableObject):
    """
    Code is a direct representation (source, byte or binary) of a collection of computer instructions that form software which tell a computer how to work. [based on https://en.wikipedia.org/wiki/Software]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/Code'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/Code"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_CharacterDeviceNode(UCO_FileSystemObject):
    """
    A character device node is a UNIX filesystem special file that serves as a conduit to communicate with devices, providing only a serial stream of input or accepting a serial stream of output. Character device nodes are used to apply access rights to the devices and to direct operations on the files to the appropriate device drivers. [based on https://en.wikipedia.org/wiki/Unix_file_types]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/CharacterDeviceNode'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/CharacterDeviceNode"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_CellSiteFacet(UCO_Facet):
    """
    A cell site facet contains the metadata surrounding the cell site.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/CellSiteFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/CellSiteFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_CellSite(UCO_ObservableObject):
    """
    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/CellSite'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/CellSite"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_CapturedTelecommunicationsInformationFacet(UCO_Facet):
    """
    A captured telecommunications information facet represents certain information within captured or intercepted telecommunications data.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/CapturedTelecommunicationsInformationFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/CapturedTelecommunicationsInformationFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_CapturedTelecommunicationsInformation(UCO_ObservableObject):
    """
    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/CapturedTelecommunicationsInformation'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/CapturedTelecommunicationsInformation"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_CallFacet(UCO_Facet):
    """
    A call facet is a grouping of characteristics unique to a connection as part of a realtime cyber communication between one or more parties.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/CallFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/CallFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Call(UCO_ObservableObject):
    """
    A call is a connection as part of a realtime cyber communication between one or more parties.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/Call'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/Call"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_CalendarFacet(UCO_Facet):
    """
    A calendar facet is a grouping of characteristics unique to a collection of appointments, meetings, and events.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/CalendarFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/CalendarFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_CalendarEntryFacet(UCO_Facet):
    """
    A calendar entry facet is a grouping of characteristics unique to an appointment, meeting, or event within a collection of appointments, meetings, and events.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/CalendarEntryFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/CalendarEntryFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_CalendarEntry(UCO_ObservableObject):
    """
    A calendar entry is an appointment, meeting or event within a collection of appointments, meetings and events.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/CalendarEntry'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/CalendarEntry"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Calendar(UCO_ObservableObject):
    """
    A calendar is a collection of appointments, meetings, and events.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/Calendar'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/Calendar"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_BrowserCookieFacet(UCO_Facet):
    """
    A browser cookie facet is a grouping of characteristics unique to a piece of data sent from a website and stored on the user's computer by the user's web browser while the user is browsing. [based on https://en.wikipedia.org/wiki/HTTP_cookie]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/BrowserCookieFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/BrowserCookieFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_BrowserCookie(UCO_ObservableObject):
    """
    A browser cookie is a piece of of data sent from a website and stored on the user's computer by the user's web browser while the user is browsing. [based on https://en.wikipedia.org/wiki/HTTP_cookie]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/BrowserCookie'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/BrowserCookie"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_BrowserBookmarkFacet(UCO_Facet):
    """
    A browser bookmark facet is a grouping of characteristics unique to a saved shortcut that directs a WWW (World Wide Web) browser software program to a particular WWW accessible resource. [based on https://techterms.com/definition/bookmark]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/BrowserBookmarkFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/BrowserBookmarkFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_BrowserBookmark(UCO_ObservableObject):
    """
    A browser bookmark is a saved shortcut that directs a WWW (World Wide Web) browser software program to a particular WWW accessible resource. [based on https://techterms.com/definition/bookmark]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/BrowserBookmark'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/BrowserBookmark"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_BotConfiguration(UCO_ObservableObject):
    """
    A bot configuration is a set of contextual settings for a software application that runs automated tasks (scripts) over the Internet at a much higher rate than would be possible for a human alone.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/BotConfiguration'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/BotConfiguration"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_BluetoothAddressFacet(UCO_MACAddressFacet):
    """
    A Bluetooth address facet is a grouping of characteristics unique to a Bluetooth standard conformant identifier assigned to a Bluetooth device to enable routing and management of Bluetooth standards conformant communication to or from that device.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/BluetoothAddressFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/BluetoothAddressFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_BluetoothAddress(UCO_MACAddress):
    """
    A Bluetooth address is a Bluetooth standard conformant identifier assigned to a Bluetooth device to enable routing and management of Bluetooth standards conformant communication to or from that device.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/BluetoothAddress'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/BluetoothAddress"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_BlockDeviceNode(UCO_FileSystemObject):
    """
    A block device node is a UNIX filesystem special file that serves as a conduit to communicate with devices, providing buffered randomly accesible input and output. Block device nodes are used to apply access rights to the devices and to direct operations on the files to the appropriate device drivers. [based on https://en.wikipedia.org/wiki/Unix_file_types]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/BlockDeviceNode'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/BlockDeviceNode"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_BlackberryPhone(UCO_SmartPhone):
    """
    A blackberry phone is a smart phone that applies the Blackberry OS mobile operating system. (Blackberry 10 re-introduces Blackberry OS, prior to that the OS was Android.)

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/BlackberryPhone'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/BlackberryPhone"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_AutonomousSystemFacet(UCO_Facet):
    """
    An autonomous system facet is a grouping of characteristics unique to a collection of connected Internet Protocol (IP) routing prefixes under the control of one or more network operators on behalf of a single administrative entity or domain that presents a common, clearly defined routing policy to the Internet. [based on https://en.wikipedia.org/wiki/Autonomous_system_(Internet)]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/AutonomousSystemFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/AutonomousSystemFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_AutonomousSystem(UCO_ObservableObject):
    """
    An autonomous system is a collection of connected Internet Protocol (IP) routing prefixes under the control of one or more network operators on behalf of a single administrative entity or domain that presents a common, clearly defined routing policy to the Internet. [based on https://en.wikipedia.org/wiki/Autonomous_system_(Internet)]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/AutonomousSystem'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/AutonomousSystem"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_AudioFacet(UCO_Facet):
    """
    An audio facet is a grouping of characteristics unique to a digital representation of sound.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/AudioFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/AudioFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Audio(UCO_ObservableObject):
    """
    Audio is a digital representation of sound.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/Audio'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/Audio"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ArchiveFileFacet(UCO_Facet):
    """
    An archive file facet is a grouping of characteristics unique to a file that is composed of one or more computer files along with metadata.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/ArchiveFileFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/ArchiveFileFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ArchiveFile(UCO_File):
    """
    An archive file is a file that is composed of one or more computer files along with metadata.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/ArchiveFile'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/ArchiveFile"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ApplicationVersion(UCO_UcoInherentCharacterizationThing):
    """
    An application version is a grouping of characteristics unique to a particular software program version.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/ApplicationVersion'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/ApplicationVersion"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ApplicationFacet(UCO_Facet):
    """
    An application facet is a grouping of characteristics unique to a particular software program designed for end users.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/ApplicationFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/ApplicationFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ApplicationAccountFacet(UCO_Facet):
    """
    An application account facet is a grouping of characteristics unique to an account within a particular software program designed for end users.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/ApplicationAccountFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/ApplicationAccountFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ApplicationAccount(UCO_DigitalAccount):
    """
    An application account is an account within a particular software program designed for end users.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/ApplicationAccount'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/ApplicationAccount"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Application(UCO_ObservableObject):
    """
    An application is a particular software program designed for end users.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/Application'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/Application"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_AntennaFacet(UCO_Facet):
    """
    An antenna alignment facet contains the metadata surrounding the cell tower's antenna position.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/AntennaFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/AntennaFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_AndroidPhone(UCO_AndroidDevice, UCO_SmartPhone):
    """
    An android phone is a smart phone that applies the Android mobile operating system.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/AndroidPhone'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/AndroidPhone"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_AndroidDeviceFacet(UCO_Facet):
    """
    An Android device facet is a grouping of characteristics unique to an Android device. [based on https://en.wikipedia.org/wiki/Android_(operating_system)]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/AndroidDeviceFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/AndroidDeviceFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_AlternateDataStreamFacet(UCO_Facet):
    """
    An alternate data stream facet is a grouping of characteristics unique to data content stored within an NTFS file that is independent of the standard content stream of the file and is hidden from access by default NTFS file viewing mechanisms.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/AlternateDataStreamFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/AlternateDataStreamFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_AlternateDataStream(UCO_ObservableObject):
    """
    An alternate data stream is data content stored within an NTFS file that is independent of the standard content stream of the file and is hidden from access by default NTFS file viewing mechanisms.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/AlternateDataStream'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/AlternateDataStream"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Adaptor(UCO_Device):
    """
    An adaptor is a device that physically converts the pin outputs but does not alter the underlying protocol (e.g. uSD to SD, CF to ATA, etc.)

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/Adaptor'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/Adaptor"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_AccountFacet(UCO_Facet):
    """
    An account facet is a grouping of characteristics unique to an arrangement with an entity to enable and control the provision of some capability or service.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/AccountFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/AccountFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_AccountAuthenticationFacet(UCO_Facet):
    """
    An account authentication facet is a grouping of characteristics unique to the mechanism of accessing an account.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/AccountAuthenticationFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/AccountAuthenticationFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ARPCacheEntry(UCO_ObservableObject):
    """
    An ARP cache entry is a single Address Resolution Protocol (ARP) response record that is created when an IP address is resolved to a MAC address (so the computer can effectively communicate with the IP address). [based on https://en.wikipedia.org/wiki/ARP_cache]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/ARPCacheEntry'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/ARPCacheEntry"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ARPCache(UCO_ObservableObject):
    """
    An ARP cache is a collection of Address Resolution Protocol (ARP) entries (mostly dynamic) that are created when an IP address is resolved to a MAC address (so the computer can effectively communicate with the IP address). [based on https://en.wikipedia.org/wiki/ARP_cache]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/ARPCache'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/ARPCache"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_API(UCO_ObservableObject):
    """
    An API (application programming interface) is a computing interface that defines interactions between multiple software or mixed hardware-software intermediaries. It defines the kinds of calls or requests that can be made, how to make them, the data formats that should be used, the conventions to follow, etc. [based on https://en.wikipedia.org/wiki/API]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/observable/API'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/observable/API"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_TermsOfUseMarking(UCO_MarkingModel):
    """
    A terms of use marking is a grouping of characteristics unique to the expression of data marking definitions (restrictions, permissions, and other guidance for how data can be used and shared) to convey details of a textual statement specifying the Terms of Use (that is, the conditions under which the content may be shared, applied, or otherwise used) of the marked content. An example of this would be used to communicate a simple statement, such as 'Acme Inc. is not responsible for the content of this file'.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/marking/TermsOfUseMarking'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/marking/TermsOfUseMarking"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_StatementMarking(UCO_MarkingModel):
    """
    A statement marking is a grouping of characteristics unique to the expression of data marking definitions (restrictions, permissions, and other guidance for how data can be used and shared) to convey details of a textual marking statement, (e.g., copyright) whose semantic meaning should apply to the associated content. Statement markings are generally not machine-readable. An example of this would be a simple marking to apply copyright information, such as 'Copyright 2014 Acme Inc.'.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/marking/StatementMarking'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/marking/StatementMarking"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ReleaseToMarking(UCO_MarkingModel):
    """
    A release-to marking is a grouping of characteristics unique to the expression of data marking definitions (restrictions, permissions, and other guidance for how data can be used and shared) to convey details of authorized persons and/or organizations to which to the associated content may be released. The existence of the Release-To marking restricts access to ONLY those identities explicitly listed, regardless of whether another data marking exists that allows sharing with other members of the community.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/marking/ReleaseToMarking'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/marking/ReleaseToMarking"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_MarkingDefinition(UCO_MarkingDefinitionAbstraction):
    """
    A marking definition is a grouping of characteristics unique to the expression of a specific data marking conveying restrictions, permissions, and other guidance for how marked data can be used and shared.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/marking/MarkingDefinition'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/marking/MarkingDefinition"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_LicenseMarking(UCO_MarkingModel):
    """
    A license marking is a grouping of characteristics unique to the expression of data marking definitions (restrictions, permissions, and other guidance for how data can be used and shared) to convey details of license restrictions that apply to the data.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/marking/LicenseMarking'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/marking/LicenseMarking"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_GranularMarking(UCO_UcoInherentCharacterizationThing):
    """
    A granular marking is a grouping of characteristics unique to specification of marking definitions (restrictions, permissions, and other guidance for how data can be used and shared) that apply to particular portions of a particular UCO object.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/marking/GranularMarking'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/marking/GranularMarking"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_SimpleAddressFacet(UCO_Facet):
    """
    A simple address facet is a grouping of characteristics unique to a geolocation expressed as an administrative address.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/location/SimpleAddressFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/location/SimpleAddressFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Location(UCO_UcoObject):
    """
    A location is a geospatial place, site, or position.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/location/Location'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/location/Location"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_LatLongCoordinatesFacet(UCO_Facet):
    """
    A lat long coordinates facet is a grouping of characteristics unique to the expression of a geolocation as the intersection of specific latitude, longitude, and altitude values.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/location/LatLongCoordinatesFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/location/LatLongCoordinatesFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_GPSCoordinatesFacet(UCO_Facet):
    """
    A GPS coordinates facet is a grouping of characteristics unique to the expression of quantified dilution of precision (DOP) for an asserted set of geolocation coordinates typically associated with satellite navigation such as the Global Positioning System (GPS).

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/location/GPSCoordinatesFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/location/GPSCoordinatesFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_VisaFacet(UCO_IdentityFacet):
    """
    Visa is a grouping of characteristics unique to information related to a person's ability to enter, leave, or stay for a specified period of time in a country.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/identity/VisaFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/identity/VisaFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_SimpleNameFacet(UCO_IdentityFacet):
    """
    A simple name facet is a grouping of characteristics unique to the personal name (e.g., Dr. John Smith Jr.) held by an identity.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/identity/SimpleNameFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/identity/SimpleNameFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_RelatedIdentityFacet(UCO_IdentityFacet):
    """
    <Needs fleshed out from CIQ>

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/identity/RelatedIdentityFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/identity/RelatedIdentityFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_QualificationFacet(UCO_IdentityFacet):
    """
    Qualification is a grouping of characteristics unique to particular skills, capabilities or their related achievements (educational, professional, etc.) of an entity.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/identity/QualificationFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/identity/QualificationFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_PhysicalInfoFacet(UCO_IdentityFacet):
    """
    Physical info is a grouping of characteristics unique to the outwardly observable nature of an individual person.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/identity/PhysicalInfoFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/identity/PhysicalInfoFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_PersonalDetailsFacet(UCO_IdentityFacet):
    """
    Personal details is a grouping of characteristics unique to an identity representing an individual person.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/identity/PersonalDetailsFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/identity/PersonalDetailsFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Person(UCO_Identity):
    """
    A person is a grouping of identifying characteristics unique to a human being regarded as an individual. [based on https://www.lexico.com/en/definition/person]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/identity/Person'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/identity/Person"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_OrganizationDetailsFacet(UCO_IdentityFacet):
    """
    Organization details is a grouping of characteristics unique to an identity representing an administrative and functional structure.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/identity/OrganizationDetailsFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/identity/OrganizationDetailsFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Organization(UCO_Identity):
    """
    An organization is a grouping of identifying characteristics unique to a group of people who work together in an organized way for a shared purpose. [based on https://dictionary.cambridge.org/us/dictionary/english/organization]

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/identity/Organization'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/identity/Organization"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_OccupationFacet(UCO_IdentityFacet):
    """
    Occupation is a grouping of characteristics unique to the job or profession of an entity.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/identity/OccupationFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/identity/OccupationFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_NationalityFacet(UCO_IdentityFacet):
    """
    Nationality is a grouping of characteristics unique to the condition of an entity belonging to a particular nation.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/identity/NationalityFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/identity/NationalityFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_LanguagesFacet(UCO_IdentityFacet):
    """
    Languages is a grouping of characteristics unique to specific syntactically and grammatically standardized forms of communication (human or computer) in which an entity has proficiency (comprehends, speaks, reads, or writes).

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/identity/LanguagesFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/identity/LanguagesFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_IdentifierFacet(UCO_IdentityFacet):
    """
    Identifier is a grouping of characteristics unique to information that uniquely and specifically identities an entity.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/identity/IdentifierFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/identity/IdentifierFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_EventsFacet(UCO_IdentityFacet):
    """
    Events is a grouping of characteristics unique to information related to specific relevant things that happen in the lifetime of an entity.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/identity/EventsFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/identity/EventsFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_CountryOfResidenceFacet(UCO_IdentityFacet):
    """
    Country of residence is a grouping of characteristics unique to information related to the country, or countries, where an entity resides.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/identity/CountryOfResidenceFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/identity/CountryOfResidenceFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_BirthInformationFacet(UCO_IdentityFacet):
    """
    Birth information is a grouping of characteristics unique to information pertaining to the birth of an entity.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/identity/BirthInformationFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/identity/BirthInformationFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_AffiliationFacet(UCO_IdentityFacet):
    """
    An affiliation is a grouping of characteristics unique to the established affiliations of an entity.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/identity/AffiliationFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/identity/AffiliationFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_AddressFacet(UCO_IdentityFacet):
    """
    An address facet is a grouping of characteristics unique to an administrative identifier for a geolocation associated with a specific identity.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/identity/AddressFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/identity/AddressFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ModusOperandi(UCO_UcoObject):
    """
    A modus operandi is a particular method of operation (how a particular entity behaves or the resources they use).

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/core/ModusOperandi'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/core/ModusOperandi"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Grouping(UCO_ContextualCompilation):
    """
    A grouping is a compilation of referenced UCO content with a shared context.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/core/Grouping'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {"https://ontology.unifiedcyberontology.org/uco/core/Grouping"}
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ExternalReference(UCO_UcoInherentCharacterizationThing):
    """
    Characteristics of a reference to a resource outside of the UCO.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/core/ExternalReference'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/core/ExternalReference"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ControlledVocabulary(UCO_UcoObject):
    """
    A controlled vocabulary is an explicitly constrained set of string values.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/core/ControlledVocabulary'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/core/ControlledVocabulary"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ConfidenceFacet(UCO_Facet):
    """
    A confidence is a grouping of characteristics unique to an asserted level of certainty in the accuracy of some information.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/core/ConfidenceFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/core/ConfidenceFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Bundle(UCO_EnclosingCompilation):
    """
    A bundle is a container for a grouping of UCO content with no presumption of shared context.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/core/Bundle'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {"https://ontology.unifiedcyberontology.org/uco/core/Bundle"}
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_AttributedName(UCO_UcoObject):
    """
    An attributed name is a name of an entity issued by some attributed naming authority.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/core/AttributedName'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/core/AttributedName"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Annotation(UCO_Assertion):
    """
    An annotation is an assertion made in relation to one or more objects.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/core/Annotation'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/core/Annotation"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Dependency(UCO_UcoInherentCharacterizationThing):
    """
    A dependency is a grouping of characteristics unique to something that a tool or other software relies on to function as intended.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/configuration/Dependency'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/configuration/Dependency"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ConfigurationEntry(UCO_UcoInherentCharacterizationThing):
    """
    A configuration entry is a grouping of characteristics unique to a particular parameter or initial setting for the use of a tool, application, software, or other cyber object.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/configuration/ConfigurationEntry'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/configuration/ConfigurationEntry"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Configuration(UCO_UcoObject):
    """
    A configuration is a grouping of characteristics unique to a set of parameters or initial settings for the use of a tool, application, software, or other cyber object.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/configuration/Configuration'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/configuration/Configuration"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ArtifactClassificationResultFacet(UCO_AnalyticResultFacet):
    """
    An artifact classification result facet is a grouping of characteristics unique to the results of an artifact classification analysis action.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/analysis/ArtifactClassificationResultFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/analysis/ArtifactClassificationResultFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ArtifactClassification(UCO_UcoInherentCharacterizationThing):
    """
    An artifact classification is a single specific assertion that a particular class of a classification taxonomy applies to something.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/analysis/ArtifactClassification'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/analysis/ArtifactClassification"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_AnalyticResult(UCO_Assertion):
    """
    An analytic result is a characterization of the understanding resulting from an analysis action.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/analysis/AnalyticResult'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/analysis/AnalyticResult"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_Analysis(UCO_Action):
    """
    An analysis is an action of detailed examination of something in order to understand its nature, context or essential features.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/analysis/Analysis'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/analysis/Analysis"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ArrayOfAction(UCO_UcoInherentCharacterizationThing):
    """
    An array of action is an ordered list of references to things that may be done or performed.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/action/ArrayOfAction'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/action/ArrayOfAction"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ActionPattern(UCO_Action, UCO_Pattern):
    """
    An action pattern is a grouping of characteristics unique to a combination of actions forming a consistent or characteristic arrangement.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/action/ActionPattern'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/action/ActionPattern"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ActionFrequencyFacet(UCO_Facet):
    """
    An action frequency facet is a grouping of characteristics unique to the frequency of occurrence for an action.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/action/ActionFrequencyFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/action/ActionFrequencyFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ActionEstimationFacet(UCO_Facet):
    """
    An action estimation facet is a grouping of characteristics unique to decision-focused approximation aspects for an action that may potentially be performed.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/action/ActionEstimationFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/action/ActionEstimationFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class UCO_ActionArgumentFacet(UCO_Facet):
    """
    An action argument facet is a grouping of characteristics unique to a single parameter of an action.

    Based on class with IRI 'https://ontology.unifiedcyberontology.org/uco/action/ActionArgumentFacet'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.unifiedcyberontology.org/uco/action/ActionArgumentFacet"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class CASE_VictimActionLifecycle(UCO_ActionLifecycle):
    """
    A victim action lifecycle is an action pattern consisting of an ordered set of multiple actions or subordinate action-lifecycles performed by an entity acting in a role characterized by its potential to be harmed as a result of a crime, accident, or other event or action.

    Based on class with IRI 'https://ontology.caseontology.org/case/investigation/VictimActionLifecycle'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.caseontology.org/case/investigation/VictimActionLifecycle"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class CASE_SubjectActionLifecycle(UCO_ActionLifecycle):
    """
    A subject action lifecycle is an action pattern consisting of an ordered set of multiple actions or subordinate action-lifecycles performed by an entity acting in a role whose conduct may be within the scope of an investigation.

    Based on class with IRI 'https://ontology.caseontology.org/case/investigation/SubjectActionLifecycle'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.caseontology.org/case/investigation/SubjectActionLifecycle"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class CASE_Subject(UCO_Role):
    """
    Subject is a role whose conduct is within the scope of an investigation.

    Based on class with IRI 'https://ontology.caseontology.org/case/investigation/Subject'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.caseontology.org/case/investigation/Subject"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class CASE_ProvenanceRecord(UCO_ContextualCompilation):
    """
    A provenance record is a grouping of characteristics unique to the provenantial (chronology of the ownership, custody or location) connection between an investigative action and a set of observations (items and/or actions) or interpretations that result from it.

    Based on class with IRI 'https://ontology.caseontology.org/case/investigation/ProvenanceRecord'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.caseontology.org/case/investigation/ProvenanceRecord"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class CASE_Investigator(UCO_Role):
    """
    Investigator is a role involved in coordinating an investigation.

    Based on class with IRI 'https://ontology.caseontology.org/case/investigation/Investigator'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.caseontology.org/case/investigation/Investigator"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class CASE_InvestigativeAction(UCO_Action):
    """
    An investigative action is something that may be done or performed within the context of an investigation, typically to examine or analyze evidence or other data.

    Based on class with IRI 'https://ontology.caseontology.org/case/investigation/InvestigativeAction'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.caseontology.org/case/investigation/InvestigativeAction"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class CASE_Investigation(UCO_ContextualCompilation):
    """
    An investigation is a grouping of characteristics unique to an exploration of the facts involved in a cyber-relevant set of suspicious activity.

    Based on class with IRI 'https://ontology.caseontology.org/case/investigation/Investigation'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.caseontology.org/case/investigation/Investigation"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class CASE_ExaminerActionLifecycle(UCO_ActionLifecycle):
    """
    An examiner action lifecycle is an action pattern consisting of an ordered set of actions or subordinate action-lifecycles performed by an entity acting in a role involved in providing scientific evaluations of evidence that is used to aid law enforcement investigations and court cases.

    Based on class with IRI 'https://ontology.caseontology.org/case/investigation/ExaminerActionLifecycle'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.caseontology.org/case/investigation/ExaminerActionLifecycle"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class CASE_Examiner(UCO_Role):
    """
    Examiner is a role involved in providing scientific evaluations of evidence that are used to aid law enforcement investigations and court cases.

    Based on class with IRI 'https://ontology.caseontology.org/case/investigation/Examiner'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.caseontology.org/case/investigation/Examiner"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class CASE_Authorization(UCO_UcoObject):
    """
    An authorization is a grouping of characteristics unique to some form of authoritative permission identified for investigative action.

    Based on class with IRI 'https://ontology.caseontology.org/case/investigation/Authorization'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.caseontology.org/case/investigation/Authorization"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class CASE_Attorney(UCO_Role):
    """
    Attorney is a role involved in preparing, interpreting, and applying law.

    Based on class with IRI 'https://ontology.caseontology.org/case/investigation/Attorney'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {
                "https://ontology.caseontology.org/case/investigation/Attorney"
            }
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class CO_Set(CO_Collection):
    """
    A collection that cannot contain duplicate elements.

    Based on class with IRI 'http://purl.org/co/Set'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {"http://purl.org/co/Set"}
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)


class CO_ListItem(CO_Item):
    """
    element belonging to a list

    Based on class with IRI 'http://purl.org/co/ListItem'.
    """

    def __init__(
        self,
        graph: rdflib.Graph,
        node_iri: str,
        *args: typing.Any,
        type_iris: typing.Set[str] = set(),
        **kwargs: typing.Any,
    ) -> None:
        if len(type_iris) == 0:
            _type_iris = {"http://purl.org/co/ListItem"}
        else:
            _type_iris = type_iris
        super().__init__(graph, node_iri, *args, type_iris=_type_iris, **kwargs)
