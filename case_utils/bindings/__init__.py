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


class NodeConstructor(object):
    def __init__(self, node_iri: typing.Optional[str] = None, *args, **kwargs) -> None:
        super().__init__()
        self._node: typing.Union[None, rdflib.BNode, rdflib.URIRef] = None
        self._node_iri = node_iri
        self._type_iris: typing.Set[str] = set()

    @property
    def node(self) -> typing.Union[rdflib.BNode, rdflib.URIRef]:
        """
        Set on first access.
        """
        if self._node is None:
            if self.node_iri is None:
                self._node = rdflib.BNode()
            else:
                self._node = rdflib.URIRef(self.node_iri)
        return self._node

    @property
    def node_iri(self) -> typing.Optional[str]:
        return self._node_iri

    @node_iri.setter
    def node_iri(self, value: typing.Optional[str]) -> None:
        assert value is None or isinstance(value, str)
        self._node_iri = value

    @property
    def type_iris(self) -> typing.Set[str]:
        return self._type_iris

    def add_to_graph(self, graph: rdflib.Graph) -> None:
        for type_iri in sorted(self.type_iris):
            graph.add((self.node_iri, rdflib.RDF.type, rdflib.URIRef(type_iri)))


class case_API(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#API'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ARPCache(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#ARPCache'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ARPCacheEntry(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#ARPCacheEntry'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Account(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#Account'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_AccountAuthenticationFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#AccountAuthenticationFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_AccountFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#AccountFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Action(case_UcoObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/action#Action'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ActionArgumentFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/action#ActionArgumentFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ActionEstimationFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/action#ActionEstimationFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ActionFrequencyFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/action#ActionFrequencyFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ActionLifecycle(case_Action):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/action#ActionLifecycle'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ActionPattern(case_Action, case_Pattern):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/action#ActionPattern'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ActionReferencesFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/action#ActionReferencesFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Address(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#Address'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_AddressFacet(case_IdentityFacet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/identity#AddressFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_AffiliationFacet(case_IdentityFacet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/identity#AffiliationFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_AlternateDataStream(NodeConstructor):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#AlternateDataStream'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_AnalyticTool(case_Tool):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/tool#AnalyticTool'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Annotation(case_Assertion):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/core#Annotation'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Appliance(case_Device):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#Appliance'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Application(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#Application'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ApplicationAccount(case_DigitalAccount):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#ApplicationAccount'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ApplicationAccountFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#ApplicationAccountFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ApplicationFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#ApplicationFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ArchiveFile(case_File):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#ArchiveFile'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ArchiveFileFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#ArchiveFileFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ArrayOfAction(NodeConstructor):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/action#ArrayOfAction'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Assertion(case_UcoObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/core#Assertion'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_AttachmentFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#AttachmentFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_AttributedName(case_UcoObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/core#AttributedName'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Audio(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#Audio'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_AudioFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#AudioFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_AutonomousSystem(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#AutonomousSystem'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_AutonomousSystemFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#AutonomousSystemFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_BenevolentRole(case_Role):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/role#BenevolentRole'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_BirthInformationFacet(case_IdentityFacet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/identity#BirthInformationFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_BlockDeviceNode(case_FileSystemObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#BlockDeviceNode'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_BluetoothAddress(case_MACAddress):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#BluetoothAddress'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_BluetoothAddressFacet(case_MACAddressFacet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#BluetoothAddressFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_BotConfiguration(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#BotConfiguration'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_BrowserBookmark(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#BrowserBookmark'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_BrowserBookmarkFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#BrowserBookmarkFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_BrowserCookie(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#BrowserCookie'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_BrowserCookieFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#BrowserCookieFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_BuildConfigurationType(NodeConstructor):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/tool#BuildConfigurationType'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_BuildFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/tool#BuildFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_BuildInformationType(NodeConstructor):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/tool#BuildInformationType'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_BuildUtilityType(NodeConstructor):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/tool#BuildUtilityType'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Bundle(case_EnclosingCompilation):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/core#Bundle'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Calendar(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#Calendar'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_CalendarEntry(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#CalendarEntry'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_CalendarEntryFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#CalendarEntryFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_CalendarFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#CalendarFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_CharacterDeviceNode(case_FileSystemObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#CharacterDeviceNode'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Code(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#Code'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Compilation(case_UcoObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/core#Compilation'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_CompilerType(NodeConstructor):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/tool#CompilerType'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_CompressedStreamFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#CompressedStreamFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ComputerSpecification(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#ComputerSpecification'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ComputerSpecificationFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#ComputerSpecificationFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ConfidenceFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/core#ConfidenceFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ConfigurationSettingType(NodeConstructor):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/tool#ConfigurationSettingType'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Contact(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#Contact'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ContactAddress(NodeConstructor):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#ContactAddress'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ContactAffiliation(NodeConstructor):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#ContactAffiliation'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ContactEmail(NodeConstructor):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#ContactEmail'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ContactFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#ContactFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ContactList(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#ContactList'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ContactListFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#ContactListFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ContactMessaging(NodeConstructor):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#ContactMessaging'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ContactPhone(NodeConstructor):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#ContactPhone'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ContactProfile(NodeConstructor):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#ContactProfile'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ContactSIP(NodeConstructor):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#ContactSIP'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ContactURL(NodeConstructor):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#ContactURL'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ContentData(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#ContentData'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ContentDataFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#ContentDataFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ContextualCompilation(case_Compilation):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/core#ContextualCompilation'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ControlledDictionary(NodeConstructor):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/types#ControlledDictionary'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ControlledDictionaryEntry(NodeConstructor):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/types#ControlledDictionaryEntry'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ControlledVocabulary(case_UcoObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/core#ControlledVocabulary'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_CookieHistory(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#CookieHistory'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_CountryOfResidenceFacet(case_IdentityFacet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/identity#CountryOfResidenceFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Credential(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#Credential'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_CredentialDump(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#CredentialDump'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_DNSCache(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#DNSCache'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_DNSRecord(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#DNSRecord'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_DataRangeFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#DataRangeFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_DefensiveTool(case_Tool):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/tool#DefensiveTool'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_DefinedEffectFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#DefinedEffectFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_DependencyType(NodeConstructor):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/tool#DependencyType'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Device(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#Device'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_DeviceFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#DeviceFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Dictionary(NodeConstructor):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/types#Dictionary'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_DictionaryEntry(NodeConstructor):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/types#DictionaryEntry'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_DigitalAccount(case_Account):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#DigitalAccount'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_DigitalAccountFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#DigitalAccountFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_DigitalAddress(case_Address):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#DigitalAddress'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_DigitalAddressFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#DigitalAddressFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_DigitalSignatureInfo(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#DigitalSignatureInfo'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_DigitalSignatureInfoFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#DigitalSignatureInfoFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Directory(case_FileSystemObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#Directory'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Disk(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#Disk'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_DiskFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#DiskFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_DiskPartition(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#DiskPartition'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_DiskPartitionFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#DiskPartitionFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_DomainName(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#DomainName'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_DomainNameFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#DomainNameFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_EXIFFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#EXIFFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_EmailAccount(case_DigitalAccount):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#EmailAccount'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_EmailAccountFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#EmailAccountFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_EmailAddress(case_DigitalAddress):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#EmailAddress'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_EmailAddressFacet(case_DigitalAddressFacet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#EmailAddressFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_EmailMessage(case_Message):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#EmailMessage'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_EmailMessageFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#EmailMessageFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_EnclosingCompilation(case_Compilation):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/core#EnclosingCompilation'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_EncodedStreamFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#EncodedStreamFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_EncryptedStreamFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#EncryptedStreamFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_EnvironmentVariable(NodeConstructor):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#EnvironmentVariable'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Event(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#Event'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_EventFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#EventFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_EventLog(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#EventLog'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_EventsFacet(case_IdentityFacet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/identity#EventsFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ExtInodeFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#ExtInodeFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ExternalReference(NodeConstructor):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/core#ExternalReference'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ExtractedString(NodeConstructor):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#ExtractedString'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ExtractedStringsFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#ExtractedStringsFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Facet(NodeConstructor):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/core#Facet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_File(case_FileSystemObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#File'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_FileFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#FileFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_FilePermissionsFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#FilePermissionsFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_FileSystem(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#FileSystem'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_FileSystemFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#FileSystemFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_FileSystemObject(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#FileSystemObject'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ForumPost(case_Message):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#ForumPost'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ForumPrivateMessage(case_Message):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#ForumPrivateMessage'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_FragmentFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#FragmentFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_GPSCoordinatesFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/location#GPSCoordinatesFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_GUI(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#GUI'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_GenericObservableObject(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#GenericObservableObject'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_GeoLocationEntry(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#GeoLocationEntry'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_GeoLocationEntryFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#GeoLocationEntryFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_GeoLocationLog(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#GeoLocationLog'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_GeoLocationLogFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#GeoLocationLogFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_GeoLocationTrack(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#GeoLocationTrack'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_GeoLocationTrackFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#GeoLocationTrackFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_GlobalFlagType(NodeConstructor):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#GlobalFlagType'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_GranularMarking(NodeConstructor):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/marking#GranularMarking'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Grouping(case_ContextualCompilation):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/core#Grouping'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_HTTPConnection(case_NetworkConnection):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#HTTPConnection'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_HTTPConnectionFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#HTTPConnectionFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Hash(NodeConstructor):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/types#Hash'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Hostname(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#Hostname'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ICMPConnection(case_NetworkConnection):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#ICMPConnection'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ICMPConnectionFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#ICMPConnectionFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_IComHandlerActionType(NodeConstructor):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#IComHandlerActionType'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_IExecActionType(NodeConstructor):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#IExecActionType'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_IPAddress(case_DigitalAddress):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#IPAddress'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_IPAddressFacet(case_DigitalAddressFacet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#IPAddressFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_IPNetmask(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#IPNetmask'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_IPv4Address(case_IPAddress):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#IPv4Address'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_IPv4AddressFacet(case_IPAddressFacet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#IPv4AddressFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_IPv6Address(case_IPAddress):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#IPv6Address'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_IPv6AddressFacet(case_IPAddressFacet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#IPv6AddressFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_IShowMessageActionType(NodeConstructor):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#IShowMessageActionType'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_IdentifierFacet(case_IdentityFacet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/identity#IdentifierFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Identity(case_IdentityAbstraction):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/identity#Identity'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_IdentityAbstraction(case_UcoObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/core#IdentityAbstraction'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_IdentityFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/identity#IdentityFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Image(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#Image'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ImageFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#ImageFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_InstantMessagingAddress(case_DigitalAddress):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#InstantMessagingAddress'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_InstantMessagingAddressFacet(case_DigitalAddressFacet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#InstantMessagingAddressFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Item(case_UcoObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/core#Item'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Junction(case_FileSystemObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#Junction'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_LanguagesFacet(case_IdentityFacet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/identity#LanguagesFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_LatLongCoordinatesFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/location#LatLongCoordinatesFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Library(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#Library'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_LibraryFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#LibraryFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_LibraryType(NodeConstructor):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/tool#LibraryType'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_LicenseMarking(case_MarkingModel):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/marking#LicenseMarking'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Location(case_UcoObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/location#Location'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_LogicalPattern(case_Pattern):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/pattern#LogicalPattern'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_MACAddress(case_DigitalAddress):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#MACAddress'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_MACAddressFacet(case_DigitalAddressFacet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#MACAddressFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_MaliciousRole(case_Role):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/role#MaliciousRole'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_MaliciousTool(case_Tool):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/tool#MaliciousTool'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_MarkingDefinition(case_MarkingDefinitionAbstraction):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/marking#MarkingDefinition'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_MarkingDefinitionAbstraction(case_UcoObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/core#MarkingDefinitionAbstraction'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_MarkingModel(NodeConstructor):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/marking#MarkingModel'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Memory(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#Memory'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_MemoryFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#MemoryFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Message(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#Message'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_MessageFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#MessageFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_MessageThread(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#MessageThread'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_MessageThreadFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#MessageThreadFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_MftRecordFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#MftRecordFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_MimePartType(NodeConstructor):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#MimePartType'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_MobileAccount(case_DigitalAccount):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#MobileAccount'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_MobileAccountFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#MobileAccountFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_MobileDevice(case_Device):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#MobileDevice'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_MobileDeviceFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#MobileDeviceFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ModusOperandi(case_UcoObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/core#ModusOperandi'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Mutex(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#Mutex'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_MutexFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#MutexFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_NTFSFile(case_File):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#NTFSFile'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_NTFSFileFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#NTFSFileFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_NTFSFilePermissionsFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#NTFSFilePermissionsFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_NamedPipe(case_FileSystemObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#NamedPipe'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_NationalityFacet(case_IdentityFacet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/identity#NationalityFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_NetworkAppliance(case_Appliance):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#NetworkAppliance'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_NetworkConnection(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#NetworkConnection'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_NetworkConnectionFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#NetworkConnectionFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_NetworkFlow(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#NetworkFlow'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_NetworkFlowFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#NetworkFlowFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_NetworkInterface(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#NetworkInterface'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_NetworkInterfaceFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#NetworkInterfaceFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_NetworkProtocol(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#NetworkProtocol'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_NetworkRoute(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#NetworkRoute'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_NetworkSubnet(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#NetworkSubnet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_NeutralRole(case_Role):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/role#NeutralRole'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Note(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#Note'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_NoteFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#NoteFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Observable(case_UcoObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#Observable'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ObservableAction(case_Action, case_Observable):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#ObservableAction'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ObservableObject(case_Item, case_Observable):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#ObservableObject'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ObservablePattern(case_Observable):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#ObservablePattern'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ObservableRelationship(case_Observable, case_Relationship):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#ObservableRelationship'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Observation(case_Action):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#Observation'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_OccupationFacet(case_IdentityFacet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/identity#OccupationFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_OnlineService(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#OnlineService'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_OnlineServiceFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#OnlineServiceFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_OperatingSystem(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#OperatingSystem'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_OperatingSystemFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#OperatingSystemFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Organization(case_Identity):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/identity#Organization'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_OrganizationDetailsFacet(case_IdentityFacet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/identity#OrganizationDetailsFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_PDFFile(case_File):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#PDFFile'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_PDFFileFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#PDFFileFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_PathRelationFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#PathRelationFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Pattern(case_UcoObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/pattern#Pattern'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_PatternExpression(NodeConstructor):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/pattern#PatternExpression'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_PaymentCard(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#PaymentCard'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Person(case_Identity):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/identity#Person'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_PersonalDetailsFacet(case_IdentityFacet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/identity#PersonalDetailsFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_PhoneAccount(case_DigitalAccount):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#PhoneAccount'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_PhoneAccountFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#PhoneAccountFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_PhoneCall(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#PhoneCall'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_PhoneCallFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#PhoneCallFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_PhysicalInfoFacet(case_IdentityFacet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/identity#PhysicalInfoFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Pipe(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#Pipe'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Post(case_Message):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#Post'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Process(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#Process'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ProcessFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#ProcessFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Profile(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#Profile'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ProfileFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#ProfileFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_PropertiesEnumeratedEffectFacet(case_DefinedEffectFacet, case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#PropertiesEnumeratedEffectFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_PropertyReadEffectFacet(case_DefinedEffectFacet, case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#PropertyReadEffectFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_QualificationFacet(case_IdentityFacet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/identity#QualificationFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_RasterPicture(case_File):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#RasterPicture'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_RasterPictureFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#RasterPictureFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_RelatedIdentityFacet(case_IdentityFacet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/identity#RelatedIdentityFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Relationship(case_UcoObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/core#Relationship'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ReleaseToMarking(case_MarkingModel):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/marking#ReleaseToMarking'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ReparsePoint(case_FileSystemObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#ReparsePoint'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Role(case_UcoObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/role#Role'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_SIMCard(case_Device):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#SIMCard'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_SIMCardFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#SIMCardFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_SIPAddress(case_DigitalAddress):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#SIPAddress'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_SIPAddressFacet(case_DigitalAddressFacet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#SIPAddressFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_SMSMessage(case_Message):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#SMSMessage'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_SMSMessageFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#SMSMessageFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_SQLiteBlob(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#SQLiteBlob'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_SQLiteBlobFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#SQLiteBlobFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_SecurityAppliance(case_Appliance):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#SecurityAppliance'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Semaphore(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#Semaphore'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_SendControlCodeEffectFacet(case_DefinedEffectFacet, case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#SendControlCodeEffectFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ShopListing(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#ShopListing'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_SimpleAddressFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/location#SimpleAddressFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_SimpleNameFacet(case_IdentityFacet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/identity#SimpleNameFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Snapshot(case_FileSystemObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#Snapshot'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Socket(case_FileSystemObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#Socket'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_SocketAddress(case_Address):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#SocketAddress'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Software(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#Software'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_SoftwareFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#SoftwareFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_StateChangeEffectFacet(case_DefinedEffectFacet, case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#StateChangeEffectFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_StatementMarking(case_MarkingModel):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/marking#StatementMarking'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_SymbolicLink(case_FileSystemObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#SymbolicLink'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_SymbolicLinkFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#SymbolicLinkFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_TCPConnection(case_NetworkConnection):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#TCPConnection'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_TCPConnectionFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#TCPConnectionFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_TaskActionType(NodeConstructor):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#TaskActionType'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_TermsOfUseMarking(case_MarkingModel):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/marking#TermsOfUseMarking'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Thread(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#Thread'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Tool(case_UcoObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/tool#Tool'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ToolConfigurationTypeFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/tool#ToolConfigurationTypeFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_TriggerType(NodeConstructor):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#TriggerType'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Tweet(case_Message):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#Tweet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_TwitterProfileFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#TwitterProfileFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_UNIXAccount(case_DigitalAccount):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#UNIXAccount'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_UNIXAccountFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#UNIXAccountFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_UNIXFile(case_File):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#UNIXFile'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_UNIXFilePermissionsFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#UNIXFilePermissionsFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_UNIXProcess(case_Process):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#UNIXProcess'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_UNIXProcessFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#UNIXProcessFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_UNIXVolumeFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#UNIXVolumeFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_URL(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#URL'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_URLFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#URLFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_URLHistory(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#URLHistory'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_URLHistoryEntry(NodeConstructor):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#URLHistoryEntry'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_URLHistoryFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#URLHistoryFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_URLVisit(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#URLVisit'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_URLVisitFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#URLVisitFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_UcoObject(NodeConstructor):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/core#UcoObject'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_UserAccount(case_DigitalAccount):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#UserAccount'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_UserAccountFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#UserAccountFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_UserSession(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#UserSession'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_UserSessionFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#UserSessionFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_ValuesEnumeratedEffectFacet(case_DefinedEffectFacet, case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#ValuesEnumeratedEffectFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Victim(case_NeutralRole):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/victim#Victim'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_VictimTargeting(case_Victim):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/victim#VictimTargeting'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_VisaFacet(case_IdentityFacet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/identity#VisaFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Volume(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#Volume'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_VolumeFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#VolumeFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WebPage(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WebPage'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WhoIs(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WhoIs'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WhoIsFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WhoIsFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WhoisContactFacet(case_ContactFacet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WhoisContactFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WhoisRegistrarInfoType(NodeConstructor):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WhoisRegistrarInfoType'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WifiAddress(case_MACAddress):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WifiAddress'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WifiAddressFacet(case_MACAddressFacet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WifiAddressFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_Wiki(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#Wiki'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WikiArticle(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WikiArticle'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WindowsAccount(case_DigitalAccount):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WindowsAccount'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WindowsAccountFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WindowsAccountFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WindowsActiveDirectoryAccount(case_DigitalAccount):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WindowsActiveDirectoryAccount'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WindowsActiveDirectoryAccountFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WindowsActiveDirectoryAccountFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WindowsComputerSpecification(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WindowsComputerSpecification'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WindowsComputerSpecificationFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WindowsComputerSpecificationFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WindowsCriticalSection(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WindowsCriticalSection'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WindowsEvent(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WindowsEvent'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WindowsFilemapping(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WindowsFilemapping'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WindowsHandle(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WindowsHandle'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WindowsHook(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WindowsHook'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WindowsMailslot(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WindowsMailslot'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WindowsNetworkShare(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WindowsNetworkShare'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WindowsPEBinaryFile(case_File):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WindowsPEBinaryFile'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WindowsPEBinaryFileFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WindowsPEBinaryFileFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WindowsPEFileHeader(NodeConstructor):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WindowsPEFileHeader'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WindowsPEOptionalHeader(NodeConstructor):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WindowsPEOptionalHeader'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WindowsPESection(NodeConstructor):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WindowsPESection'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WindowsPrefetch(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WindowsPrefetch'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WindowsPrefetchFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WindowsPrefetchFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WindowsProcess(case_Process):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WindowsProcess'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WindowsProcessFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WindowsProcessFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WindowsRegistryHive(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WindowsRegistryHive'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WindowsRegistryHiveFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WindowsRegistryHiveFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WindowsRegistryKey(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WindowsRegistryKey'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WindowsRegistryKeyFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WindowsRegistryKeyFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WindowsRegistryValue(NodeConstructor):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WindowsRegistryValue'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WindowsService(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WindowsService'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WindowsServiceFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WindowsServiceFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WindowsSystemRestore(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WindowsSystemRestore'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WindowsTask(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WindowsTask'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WindowsTaskFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WindowsTaskFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WindowsThread(case_Thread):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WindowsThread'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WindowsThreadFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WindowsThreadFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WindowsVolumeFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WindowsVolumeFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WindowsWaitableTime(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WindowsWaitableTime'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WirelessNetworkConnection(case_NetworkConnection):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WirelessNetworkConnection'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_WirelessNetworkConnectionFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#WirelessNetworkConnectionFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_X509Certificate(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#X509Certificate'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_X509CertificateFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#X509CertificateFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_X509V3Certificate(case_ObservableObject):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#X509V3Certificate'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class case_X509V3ExtensionsFacet(case_Facet):
    """
    Based on class with IRI 'https://unifiedcyberontology.org/ontology/uco/observable#X509V3ExtensionsFacet'.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
