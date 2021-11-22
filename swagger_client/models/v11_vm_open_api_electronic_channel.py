# coding: utf-8

"""
    PTV Open Api version 11

    Here you can see listed all the PTV Open Api methods.  # noqa: E501

    OpenAPI spec version: v11
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class V11VmOpenApiElectronicChannel(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'source_id': 'str',
        'service_channel_descriptions': 'list[VmOpenApiLocalizedListItem]',
        'area_type': 'str',
        'support_phones': 'list[V4VmOpenApiPhone]',
        'support_emails': 'list[VmOpenApiLanguageItem]',
        'languages': 'list[str]',
        'web_pages': 'list[V9VmOpenApiWebPage]',
        'service_hours': 'list[V11VmOpenApiServiceHour]',
        'channel_id': 'str',
        'version_id': 'str',
        'service_channel_type': 'str',
        'organization_id': 'str',
        'service_channel_names': 'list[VmOpenApiLocalizedListItem]',
        'areas': 'list[VmOpenApiArea]',
        'services': 'list[V11VmOpenApiServiceChannelService]',
        'service_collections': 'list[VmOpenApiServiceServiceCollection]',
        'publishing_status': 'str',
        'modified': 'datetime',
        'responsible_sote_organization': 'str',
        'ontology_terms': 'list[V4VmOpenApiOntologyTerm]',
        'area_municipalities': 'list[VmOpenApiMunicipality]',
        'is_visible_for_all': 'bool',
        'security': 'ISecurityOwnOrganization',
        'available_languages': 'list[str]',
        'signature_quantity': 'int',
        'requires_signature': 'bool',
        'requires_authentication': 'bool',
        'attachments': 'list[VmOpenApiAttachmentWithType]',
        'accessibility_classification': 'list[VmOpenApiAccessibilityClassification]'
    }

    attribute_map = {
        'id': 'id',
        'source_id': 'sourceId',
        'service_channel_descriptions': 'serviceChannelDescriptions',
        'area_type': 'areaType',
        'support_phones': 'supportPhones',
        'support_emails': 'supportEmails',
        'languages': 'languages',
        'web_pages': 'webPages',
        'service_hours': 'serviceHours',
        'channel_id': 'channelId',
        'version_id': 'versionId',
        'service_channel_type': 'serviceChannelType',
        'organization_id': 'organizationId',
        'service_channel_names': 'serviceChannelNames',
        'areas': 'areas',
        'services': 'services',
        'service_collections': 'serviceCollections',
        'publishing_status': 'publishingStatus',
        'modified': 'modified',
        'responsible_sote_organization': 'responsibleSoteOrganization',
        'ontology_terms': 'ontologyTerms',
        'area_municipalities': 'areaMunicipalities',
        'is_visible_for_all': 'isVisibleForAll',
        'security': 'security',
        'available_languages': 'availableLanguages',
        'signature_quantity': 'signatureQuantity',
        'requires_signature': 'requiresSignature',
        'requires_authentication': 'requiresAuthentication',
        'attachments': 'attachments',
        'accessibility_classification': 'accessibilityClassification'
    }

    def __init__(self, id=None, source_id=None, service_channel_descriptions=None, area_type=None, support_phones=None, support_emails=None, languages=None, web_pages=None, service_hours=None, channel_id=None, version_id=None, service_channel_type=None, organization_id=None, service_channel_names=None, areas=None, services=None, service_collections=None, publishing_status=None, modified=None, responsible_sote_organization=None, ontology_terms=None, area_municipalities=None, is_visible_for_all=None, security=None, available_languages=None, signature_quantity=None, requires_signature=None, requires_authentication=None, attachments=None, accessibility_classification=None):  # noqa: E501
        """V11VmOpenApiElectronicChannel - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._source_id = None
        self._service_channel_descriptions = None
        self._area_type = None
        self._support_phones = None
        self._support_emails = None
        self._languages = None
        self._web_pages = None
        self._service_hours = None
        self._channel_id = None
        self._version_id = None
        self._service_channel_type = None
        self._organization_id = None
        self._service_channel_names = None
        self._areas = None
        self._services = None
        self._service_collections = None
        self._publishing_status = None
        self._modified = None
        self._responsible_sote_organization = None
        self._ontology_terms = None
        self._area_municipalities = None
        self._is_visible_for_all = None
        self._security = None
        self._available_languages = None
        self._signature_quantity = None
        self._requires_signature = None
        self._requires_authentication = None
        self._attachments = None
        self._accessibility_classification = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if source_id is not None:
            self.source_id = source_id
        if service_channel_descriptions is not None:
            self.service_channel_descriptions = service_channel_descriptions
        if area_type is not None:
            self.area_type = area_type
        if support_phones is not None:
            self.support_phones = support_phones
        if support_emails is not None:
            self.support_emails = support_emails
        if languages is not None:
            self.languages = languages
        if web_pages is not None:
            self.web_pages = web_pages
        if service_hours is not None:
            self.service_hours = service_hours
        if channel_id is not None:
            self.channel_id = channel_id
        if version_id is not None:
            self.version_id = version_id
        if service_channel_type is not None:
            self.service_channel_type = service_channel_type
        if organization_id is not None:
            self.organization_id = organization_id
        if service_channel_names is not None:
            self.service_channel_names = service_channel_names
        if areas is not None:
            self.areas = areas
        if services is not None:
            self.services = services
        if service_collections is not None:
            self.service_collections = service_collections
        if publishing_status is not None:
            self.publishing_status = publishing_status
        if modified is not None:
            self.modified = modified
        if responsible_sote_organization is not None:
            self.responsible_sote_organization = responsible_sote_organization
        if ontology_terms is not None:
            self.ontology_terms = ontology_terms
        if area_municipalities is not None:
            self.area_municipalities = area_municipalities
        if is_visible_for_all is not None:
            self.is_visible_for_all = is_visible_for_all
        if security is not None:
            self.security = security
        if available_languages is not None:
            self.available_languages = available_languages
        if signature_quantity is not None:
            self.signature_quantity = signature_quantity
        if requires_signature is not None:
            self.requires_signature = requires_signature
        if requires_authentication is not None:
            self.requires_authentication = requires_authentication
        if attachments is not None:
            self.attachments = attachments
        if accessibility_classification is not None:
            self.accessibility_classification = accessibility_classification

    @property
    def id(self):
        """Gets the id of this V11VmOpenApiElectronicChannel.  # noqa: E501

        PTV identifier for the service channel.  # noqa: E501

        :return: The id of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V11VmOpenApiElectronicChannel.

        PTV identifier for the service channel.  # noqa: E501

        :param id: The id of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def source_id(self):
        """Gets the source_id of this V11VmOpenApiElectronicChannel.  # noqa: E501

        External system identifier for this service channel. User needs to be logged in to be able to get/set value.  # noqa: E501

        :return: The source_id of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this V11VmOpenApiElectronicChannel.

        External system identifier for this service channel. User needs to be logged in to be able to get/set value.  # noqa: E501

        :param source_id: The source_id of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :type: str
        """

        self._source_id = source_id

    @property
    def service_channel_descriptions(self):
        """Gets the service_channel_descriptions of this V11VmOpenApiElectronicChannel.  # noqa: E501

        List of localized service channel descriptions. Possible type values are: Description, Summary (in version 7 ShortDescription). (Max.Length: 2500 Description).  # noqa: E501

        :return: The service_channel_descriptions of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :rtype: list[VmOpenApiLocalizedListItem]
        """
        return self._service_channel_descriptions

    @service_channel_descriptions.setter
    def service_channel_descriptions(self, service_channel_descriptions):
        """Sets the service_channel_descriptions of this V11VmOpenApiElectronicChannel.

        List of localized service channel descriptions. Possible type values are: Description, Summary (in version 7 ShortDescription). (Max.Length: 2500 Description).  # noqa: E501

        :param service_channel_descriptions: The service_channel_descriptions of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :type: list[VmOpenApiLocalizedListItem]
        """

        self._service_channel_descriptions = service_channel_descriptions

    @property
    def area_type(self):
        """Gets the area_type of this V11VmOpenApiElectronicChannel.  # noqa: E501

        Area type. Possible values are: Nationwide, NationwideExceptAlandIslands or LimitedType.  In version 7 and older: WholeCountry, WholeCountryExceptAlandIslands, AreaType.  # noqa: E501

        :return: The area_type of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :rtype: str
        """
        return self._area_type

    @area_type.setter
    def area_type(self, area_type):
        """Sets the area_type of this V11VmOpenApiElectronicChannel.

        Area type. Possible values are: Nationwide, NationwideExceptAlandIslands or LimitedType.  In version 7 and older: WholeCountry, WholeCountryExceptAlandIslands, AreaType.  # noqa: E501

        :param area_type: The area_type of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :type: str
        """

        self._area_type = area_type

    @property
    def support_phones(self):
        """Gets the support_phones of this V11VmOpenApiElectronicChannel.  # noqa: E501

        List of support phone numbers for the service channel.  # noqa: E501

        :return: The support_phones of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :rtype: list[V4VmOpenApiPhone]
        """
        return self._support_phones

    @support_phones.setter
    def support_phones(self, support_phones):
        """Sets the support_phones of this V11VmOpenApiElectronicChannel.

        List of support phone numbers for the service channel.  # noqa: E501

        :param support_phones: The support_phones of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :type: list[V4VmOpenApiPhone]
        """

        self._support_phones = support_phones

    @property
    def support_emails(self):
        """Gets the support_emails of this V11VmOpenApiElectronicChannel.  # noqa: E501

        List of support email addresses for the service channel. (Max.Length: 100).  # noqa: E501

        :return: The support_emails of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :rtype: list[VmOpenApiLanguageItem]
        """
        return self._support_emails

    @support_emails.setter
    def support_emails(self, support_emails):
        """Sets the support_emails of this V11VmOpenApiElectronicChannel.

        List of support email addresses for the service channel. (Max.Length: 100).  # noqa: E501

        :param support_emails: The support_emails of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :type: list[VmOpenApiLanguageItem]
        """

        self._support_emails = support_emails

    @property
    def languages(self):
        """Gets the languages of this V11VmOpenApiElectronicChannel.  # noqa: E501

        List of languages the service channel is available in (two letter language code).  # noqa: E501

        :return: The languages of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :rtype: list[str]
        """
        return self._languages

    @languages.setter
    def languages(self, languages):
        """Sets the languages of this V11VmOpenApiElectronicChannel.

        List of languages the service channel is available in (two letter language code).  # noqa: E501

        :param languages: The languages of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :type: list[str]
        """

        self._languages = languages

    @property
    def web_pages(self):
        """Gets the web_pages of this V11VmOpenApiElectronicChannel.  # noqa: E501

        List of service channel web pages.  # noqa: E501

        :return: The web_pages of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :rtype: list[V9VmOpenApiWebPage]
        """
        return self._web_pages

    @web_pages.setter
    def web_pages(self, web_pages):
        """Sets the web_pages of this V11VmOpenApiElectronicChannel.

        List of service channel web pages.  # noqa: E501

        :param web_pages: The web_pages of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :type: list[V9VmOpenApiWebPage]
        """

        self._web_pages = web_pages

    @property
    def service_hours(self):
        """Gets the service_hours of this V11VmOpenApiElectronicChannel.  # noqa: E501

        List of service channel service hours.  # noqa: E501

        :return: The service_hours of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :rtype: list[V11VmOpenApiServiceHour]
        """
        return self._service_hours

    @service_hours.setter
    def service_hours(self, service_hours):
        """Sets the service_hours of this V11VmOpenApiElectronicChannel.

        List of service channel service hours.  # noqa: E501

        :param service_hours: The service_hours of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :type: list[V11VmOpenApiServiceHour]
        """

        self._service_hours = service_hours

    @property
    def channel_id(self):
        """Gets the channel_id of this V11VmOpenApiElectronicChannel.  # noqa: E501

        Gets or sets the special channel identifier.  # noqa: E501

        :return: The channel_id of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        """Sets the channel_id of this V11VmOpenApiElectronicChannel.

        Gets or sets the special channel identifier.  # noqa: E501

        :param channel_id: The channel_id of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :type: str
        """

        self._channel_id = channel_id

    @property
    def version_id(self):
        """Gets the version_id of this V11VmOpenApiElectronicChannel.  # noqa: E501

        The identifier for current version.  # noqa: E501

        :return: The version_id of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this V11VmOpenApiElectronicChannel.

        The identifier for current version.  # noqa: E501

        :param version_id: The version_id of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :type: str
        """

        self._version_id = version_id

    @property
    def service_channel_type(self):
        """Gets the service_channel_type of this V11VmOpenApiElectronicChannel.  # noqa: E501

        Type of the service channel. Channel types: EChannel, WebPage, PrintableForm, Phone or ServiceLocation.  # noqa: E501

        :return: The service_channel_type of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :rtype: str
        """
        return self._service_channel_type

    @service_channel_type.setter
    def service_channel_type(self, service_channel_type):
        """Sets the service_channel_type of this V11VmOpenApiElectronicChannel.

        Type of the service channel. Channel types: EChannel, WebPage, PrintableForm, Phone or ServiceLocation.  # noqa: E501

        :param service_channel_type: The service_channel_type of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :type: str
        """

        self._service_channel_type = service_channel_type

    @property
    def organization_id(self):
        """Gets the organization_id of this V11VmOpenApiElectronicChannel.  # noqa: E501

        PTV organization identifier responsible for the channel.  # noqa: E501

        :return: The organization_id of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this V11VmOpenApiElectronicChannel.

        PTV organization identifier responsible for the channel.  # noqa: E501

        :param organization_id: The organization_id of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def service_channel_names(self):
        """Gets the service_channel_names of this V11VmOpenApiElectronicChannel.  # noqa: E501

        Localized list of service channel names. Possible type values are: Name, AlternativeName (in version 7 AlternateName).  # noqa: E501

        :return: The service_channel_names of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :rtype: list[VmOpenApiLocalizedListItem]
        """
        return self._service_channel_names

    @service_channel_names.setter
    def service_channel_names(self, service_channel_names):
        """Sets the service_channel_names of this V11VmOpenApiElectronicChannel.

        Localized list of service channel names. Possible type values are: Name, AlternativeName (in version 7 AlternateName).  # noqa: E501

        :param service_channel_names: The service_channel_names of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :type: list[VmOpenApiLocalizedListItem]
        """

        self._service_channel_names = service_channel_names

    @property
    def areas(self):
        """Gets the areas of this V11VmOpenApiElectronicChannel.  # noqa: E501

        List of service channel areas.  # noqa: E501

        :return: The areas of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :rtype: list[VmOpenApiArea]
        """
        return self._areas

    @areas.setter
    def areas(self, areas):
        """Sets the areas of this V11VmOpenApiElectronicChannel.

        List of service channel areas.  # noqa: E501

        :param areas: The areas of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :type: list[VmOpenApiArea]
        """

        self._areas = areas

    @property
    def services(self):
        """Gets the services of this V11VmOpenApiElectronicChannel.  # noqa: E501

        List of linked services including relationship data.  # noqa: E501

        :return: The services of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :rtype: list[V11VmOpenApiServiceChannelService]
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this V11VmOpenApiElectronicChannel.

        List of linked services including relationship data.  # noqa: E501

        :param services: The services of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :type: list[V11VmOpenApiServiceChannelService]
        """

        self._services = services

    @property
    def service_collections(self):
        """Gets the service_collections of this V11VmOpenApiElectronicChannel.  # noqa: E501


        :return: The service_collections of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :rtype: list[VmOpenApiServiceServiceCollection]
        """
        return self._service_collections

    @service_collections.setter
    def service_collections(self, service_collections):
        """Sets the service_collections of this V11VmOpenApiElectronicChannel.


        :param service_collections: The service_collections of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :type: list[VmOpenApiServiceServiceCollection]
        """

        self._service_collections = service_collections

    @property
    def publishing_status(self):
        """Gets the publishing_status of this V11VmOpenApiElectronicChannel.  # noqa: E501

        Publishing status. Possible values are: Draft, Published, Deleted or Modified.  # noqa: E501

        :return: The publishing_status of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :rtype: str
        """
        return self._publishing_status

    @publishing_status.setter
    def publishing_status(self, publishing_status):
        """Sets the publishing_status of this V11VmOpenApiElectronicChannel.

        Publishing status. Possible values are: Draft, Published, Deleted or Modified.  # noqa: E501

        :param publishing_status: The publishing_status of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :type: str
        """

        self._publishing_status = publishing_status

    @property
    def modified(self):
        """Gets the modified of this V11VmOpenApiElectronicChannel.  # noqa: E501

        Date when item was modified/created (UTC).  # noqa: E501

        :return: The modified of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this V11VmOpenApiElectronicChannel.

        Date when item was modified/created (UTC).  # noqa: E501

        :param modified: The modified of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :type: datetime
        """

        self._modified = modified

    @property
    def responsible_sote_organization(self):
        """Gets the responsible_sote_organization of this V11VmOpenApiElectronicChannel.  # noqa: E501

        Sote organization that is responsible for the service channel. Notice! At the moment always empty - the property is a placeholder for later use.  # noqa: E501

        :return: The responsible_sote_organization of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :rtype: str
        """
        return self._responsible_sote_organization

    @responsible_sote_organization.setter
    def responsible_sote_organization(self, responsible_sote_organization):
        """Sets the responsible_sote_organization of this V11VmOpenApiElectronicChannel.

        Sote organization that is responsible for the service channel. Notice! At the moment always empty - the property is a placeholder for later use.  # noqa: E501

        :param responsible_sote_organization: The responsible_sote_organization of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :type: str
        """

        self._responsible_sote_organization = responsible_sote_organization

    @property
    def ontology_terms(self):
        """Gets the ontology_terms of this V11VmOpenApiElectronicChannel.  # noqa: E501

        List of ontology terms related to the all service connections.  # noqa: E501

        :return: The ontology_terms of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :rtype: list[V4VmOpenApiOntologyTerm]
        """
        return self._ontology_terms

    @ontology_terms.setter
    def ontology_terms(self, ontology_terms):
        """Sets the ontology_terms of this V11VmOpenApiElectronicChannel.

        List of ontology terms related to the all service connections.  # noqa: E501

        :param ontology_terms: The ontology_terms of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :type: list[V4VmOpenApiOntologyTerm]
        """

        self._ontology_terms = ontology_terms

    @property
    def area_municipalities(self):
        """Gets the area_municipalities of this V11VmOpenApiElectronicChannel.  # noqa: E501

        List of municipalities including municipality code and a localized list of municipality names.  # noqa: E501

        :return: The area_municipalities of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :rtype: list[VmOpenApiMunicipality]
        """
        return self._area_municipalities

    @area_municipalities.setter
    def area_municipalities(self, area_municipalities):
        """Sets the area_municipalities of this V11VmOpenApiElectronicChannel.

        List of municipalities including municipality code and a localized list of municipality names.  # noqa: E501

        :param area_municipalities: The area_municipalities of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :type: list[VmOpenApiMunicipality]
        """

        self._area_municipalities = area_municipalities

    @property
    def is_visible_for_all(self):
        """Gets the is_visible_for_all of this V11VmOpenApiElectronicChannel.  # noqa: E501

        Indicates if channel can be used (referenced within services) by other users from other organizations.  # noqa: E501

        :return: The is_visible_for_all of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :rtype: bool
        """
        return self._is_visible_for_all

    @is_visible_for_all.setter
    def is_visible_for_all(self, is_visible_for_all):
        """Sets the is_visible_for_all of this V11VmOpenApiElectronicChannel.

        Indicates if channel can be used (referenced within services) by other users from other organizations.  # noqa: E501

        :param is_visible_for_all: The is_visible_for_all of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :type: bool
        """

        self._is_visible_for_all = is_visible_for_all

    @property
    def security(self):
        """Gets the security of this V11VmOpenApiElectronicChannel.  # noqa: E501


        :return: The security of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :rtype: ISecurityOwnOrganization
        """
        return self._security

    @security.setter
    def security(self, security):
        """Sets the security of this V11VmOpenApiElectronicChannel.


        :param security: The security of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :type: ISecurityOwnOrganization
        """

        self._security = security

    @property
    def available_languages(self):
        """Gets the available_languages of this V11VmOpenApiElectronicChannel.  # noqa: E501

        Gets or sets available languages  # noqa: E501

        :return: The available_languages of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :rtype: list[str]
        """
        return self._available_languages

    @available_languages.setter
    def available_languages(self, available_languages):
        """Sets the available_languages of this V11VmOpenApiElectronicChannel.

        Gets or sets available languages  # noqa: E501

        :param available_languages: The available_languages of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :type: list[str]
        """

        self._available_languages = available_languages

    @property
    def signature_quantity(self):
        """Gets the signature_quantity of this V11VmOpenApiElectronicChannel.  # noqa: E501

        How many signatures are required.  # noqa: E501

        :return: The signature_quantity of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :rtype: int
        """
        return self._signature_quantity

    @signature_quantity.setter
    def signature_quantity(self, signature_quantity):
        """Sets the signature_quantity of this V11VmOpenApiElectronicChannel.

        How many signatures are required.  # noqa: E501

        :param signature_quantity: The signature_quantity of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :type: int
        """

        self._signature_quantity = signature_quantity

    @property
    def requires_signature(self):
        """Gets the requires_signature of this V11VmOpenApiElectronicChannel.  # noqa: E501

        Is signature required.  # noqa: E501

        :return: The requires_signature of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :rtype: bool
        """
        return self._requires_signature

    @requires_signature.setter
    def requires_signature(self, requires_signature):
        """Sets the requires_signature of this V11VmOpenApiElectronicChannel.

        Is signature required.  # noqa: E501

        :param requires_signature: The requires_signature of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :type: bool
        """

        self._requires_signature = requires_signature

    @property
    def requires_authentication(self):
        """Gets the requires_authentication of this V11VmOpenApiElectronicChannel.  # noqa: E501

        Does the electronic channel require authentication.  # noqa: E501

        :return: The requires_authentication of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :rtype: bool
        """
        return self._requires_authentication

    @requires_authentication.setter
    def requires_authentication(self, requires_authentication):
        """Sets the requires_authentication of this V11VmOpenApiElectronicChannel.

        Does the electronic channel require authentication.  # noqa: E501

        :param requires_authentication: The requires_authentication of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :type: bool
        """

        self._requires_authentication = requires_authentication

    @property
    def attachments(self):
        """Gets the attachments of this V11VmOpenApiElectronicChannel.  # noqa: E501

        List of attachments.  # noqa: E501

        :return: The attachments of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :rtype: list[VmOpenApiAttachmentWithType]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this V11VmOpenApiElectronicChannel.

        List of attachments.  # noqa: E501

        :param attachments: The attachments of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :type: list[VmOpenApiAttachmentWithType]
        """

        self._attachments = attachments

    @property
    def accessibility_classification(self):
        """Gets the accessibility_classification of this V11VmOpenApiElectronicChannel.  # noqa: E501

        The accessibility classification.  # noqa: E501

        :return: The accessibility_classification of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :rtype: list[VmOpenApiAccessibilityClassification]
        """
        return self._accessibility_classification

    @accessibility_classification.setter
    def accessibility_classification(self, accessibility_classification):
        """Sets the accessibility_classification of this V11VmOpenApiElectronicChannel.

        The accessibility classification.  # noqa: E501

        :param accessibility_classification: The accessibility_classification of this V11VmOpenApiElectronicChannel.  # noqa: E501
        :type: list[VmOpenApiAccessibilityClassification]
        """

        self._accessibility_classification = accessibility_classification

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(V11VmOpenApiElectronicChannel, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V11VmOpenApiElectronicChannel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
