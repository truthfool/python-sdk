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

class V10VmOpenApiGeneralDescriptionIn(object):
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
        'source_id': 'str',
        'requirements': 'list[VmOpenApiLanguageItem]',
        'legislation': 'list[V4VmOpenApiLaw]',
        'general_description_type_id': 'str',
        'available_languages': 'list[str]',
        'version_id': 'str',
        'id': 'str',
        'life_events': 'list[str]',
        'industrial_classes': 'list[str]',
        'current_publishing_status': 'str',
        'required_properties_available_languages': 'list[str]',
        'type': 'str',
        'service_charge_type': 'str',
        'names': 'list[VmOpenApiLocalizedListItem]',
        'descriptions': 'list[VmOpenApiLocalizedListItem]',
        'service_classes': 'list[str]',
        'ontology_terms': 'list[str]',
        'target_groups': 'list[str]',
        'general_description_type': 'str',
        'publishing_status': 'str',
        'delete_all_industrial_classes': 'bool',
        'delete_all_laws': 'bool',
        'delete_all_life_events': 'bool',
        'delete_service_charge_type': 'bool'
    }

    attribute_map = {
        'source_id': 'sourceId',
        'requirements': 'requirements',
        'legislation': 'legislation',
        'general_description_type_id': 'generalDescriptionTypeId',
        'available_languages': 'availableLanguages',
        'version_id': 'versionId',
        'id': 'id',
        'life_events': 'lifeEvents',
        'industrial_classes': 'industrialClasses',
        'current_publishing_status': 'currentPublishingStatus',
        'required_properties_available_languages': 'requiredPropertiesAvailableLanguages',
        'type': 'type',
        'service_charge_type': 'serviceChargeType',
        'names': 'names',
        'descriptions': 'descriptions',
        'service_classes': 'serviceClasses',
        'ontology_terms': 'ontologyTerms',
        'target_groups': 'targetGroups',
        'general_description_type': 'generalDescriptionType',
        'publishing_status': 'publishingStatus',
        'delete_all_industrial_classes': 'deleteAllIndustrialClasses',
        'delete_all_laws': 'deleteAllLaws',
        'delete_all_life_events': 'deleteAllLifeEvents',
        'delete_service_charge_type': 'deleteServiceChargeType'
    }

    def __init__(self, source_id=None, requirements=None, legislation=None, general_description_type_id=None, available_languages=None, version_id=None, id=None, life_events=None, industrial_classes=None, current_publishing_status=None, required_properties_available_languages=None, type=None, service_charge_type=None, names=None, descriptions=None, service_classes=None, ontology_terms=None, target_groups=None, general_description_type=None, publishing_status=None, delete_all_industrial_classes=None, delete_all_laws=None, delete_all_life_events=None, delete_service_charge_type=None):  # noqa: E501
        """V10VmOpenApiGeneralDescriptionIn - a model defined in Swagger"""  # noqa: E501
        self._source_id = None
        self._requirements = None
        self._legislation = None
        self._general_description_type_id = None
        self._available_languages = None
        self._version_id = None
        self._id = None
        self._life_events = None
        self._industrial_classes = None
        self._current_publishing_status = None
        self._required_properties_available_languages = None
        self._type = None
        self._service_charge_type = None
        self._names = None
        self._descriptions = None
        self._service_classes = None
        self._ontology_terms = None
        self._target_groups = None
        self._general_description_type = None
        self._publishing_status = None
        self._delete_all_industrial_classes = None
        self._delete_all_laws = None
        self._delete_all_life_events = None
        self._delete_service_charge_type = None
        self.discriminator = None
        if source_id is not None:
            self.source_id = source_id
        if requirements is not None:
            self.requirements = requirements
        if legislation is not None:
            self.legislation = legislation
        if general_description_type_id is not None:
            self.general_description_type_id = general_description_type_id
        if available_languages is not None:
            self.available_languages = available_languages
        if version_id is not None:
            self.version_id = version_id
        if id is not None:
            self.id = id
        if life_events is not None:
            self.life_events = life_events
        if industrial_classes is not None:
            self.industrial_classes = industrial_classes
        if current_publishing_status is not None:
            self.current_publishing_status = current_publishing_status
        if required_properties_available_languages is not None:
            self.required_properties_available_languages = required_properties_available_languages
        if type is not None:
            self.type = type
        if service_charge_type is not None:
            self.service_charge_type = service_charge_type
        self.names = names
        self.descriptions = descriptions
        self.service_classes = service_classes
        self.ontology_terms = ontology_terms
        self.target_groups = target_groups
        self.general_description_type = general_description_type
        self.publishing_status = publishing_status
        if delete_all_industrial_classes is not None:
            self.delete_all_industrial_classes = delete_all_industrial_classes
        if delete_all_laws is not None:
            self.delete_all_laws = delete_all_laws
        if delete_all_life_events is not None:
            self.delete_all_life_events = delete_all_life_events
        if delete_service_charge_type is not None:
            self.delete_service_charge_type = delete_service_charge_type

    @property
    def source_id(self):
        """Gets the source_id of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501

        External system identifier. User needs to be logged in to be able to get/set value.  # noqa: E501

        :return: The source_id of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this V10VmOpenApiGeneralDescriptionIn.

        External system identifier. User needs to be logged in to be able to get/set value.  # noqa: E501

        :param source_id: The source_id of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :type: str
        """

        self._source_id = source_id

    @property
    def requirements(self):
        """Gets the requirements of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501

        Localized service usage requirements (description of requirement). (Max.Length: 2500).  # noqa: E501

        :return: The requirements of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :rtype: list[VmOpenApiLanguageItem]
        """
        return self._requirements

    @requirements.setter
    def requirements(self, requirements):
        """Sets the requirements of this V10VmOpenApiGeneralDescriptionIn.

        Localized service usage requirements (description of requirement). (Max.Length: 2500).  # noqa: E501

        :param requirements: The requirements of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :type: list[VmOpenApiLanguageItem]
        """

        self._requirements = requirements

    @property
    def legislation(self):
        """Gets the legislation of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501

        Laws that a general description is based on.  # noqa: E501

        :return: The legislation of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :rtype: list[V4VmOpenApiLaw]
        """
        return self._legislation

    @legislation.setter
    def legislation(self, legislation):
        """Sets the legislation of this V10VmOpenApiGeneralDescriptionIn.

        Laws that a general description is based on.  # noqa: E501

        :param legislation: The legislation of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :type: list[V4VmOpenApiLaw]
        """

        self._legislation = legislation

    @property
    def general_description_type_id(self):
        """Gets the general_description_type_id of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501

        General description type id. Used internally to check the restrictions for usage.  In older versions: Default general description is Municipality.  # noqa: E501

        :return: The general_description_type_id of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :rtype: str
        """
        return self._general_description_type_id

    @general_description_type_id.setter
    def general_description_type_id(self, general_description_type_id):
        """Sets the general_description_type_id of this V10VmOpenApiGeneralDescriptionIn.

        General description type id. Used internally to check the restrictions for usage.  In older versions: Default general description is Municipality.  # noqa: E501

        :param general_description_type_id: The general_description_type_id of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :type: str
        """

        self._general_description_type_id = general_description_type_id

    @property
    def available_languages(self):
        """Gets the available_languages of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501

        Gets or sets available languages  # noqa: E501

        :return: The available_languages of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :rtype: list[str]
        """
        return self._available_languages

    @available_languages.setter
    def available_languages(self, available_languages):
        """Sets the available_languages of this V10VmOpenApiGeneralDescriptionIn.

        Gets or sets available languages  # noqa: E501

        :param available_languages: The available_languages of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :type: list[str]
        """

        self._available_languages = available_languages

    @property
    def version_id(self):
        """Gets the version_id of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501

        The identifier for current version.  # noqa: E501

        :return: The version_id of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this V10VmOpenApiGeneralDescriptionIn.

        The identifier for current version.  # noqa: E501

        :param version_id: The version_id of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :type: str
        """

        self._version_id = version_id

    @property
    def id(self):
        """Gets the id of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501

        Entity Guid identifier.  # noqa: E501

        :return: The id of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V10VmOpenApiGeneralDescriptionIn.

        Entity Guid identifier.  # noqa: E501

        :param id: The id of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def life_events(self):
        """Gets the life_events of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501

        List of life event urls. Sample url: http://urn.fi/URN:NBN:fi:au:ptvl:v3017  # noqa: E501

        :return: The life_events of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :rtype: list[str]
        """
        return self._life_events

    @life_events.setter
    def life_events(self, life_events):
        """Sets the life_events of this V10VmOpenApiGeneralDescriptionIn.

        List of life event urls. Sample url: http://urn.fi/URN:NBN:fi:au:ptvl:v3017  # noqa: E501

        :param life_events: The life_events of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :type: list[str]
        """

        self._life_events = life_events

    @property
    def industrial_classes(self):
        """Gets the industrial_classes of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501

        List of industrial class codes (see http://tilastokeskus.fi/meta/luokitukset/toimiala/001-2008/tekstitiedosto_en.txt).  # noqa: E501

        :return: The industrial_classes of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :rtype: list[str]
        """
        return self._industrial_classes

    @industrial_classes.setter
    def industrial_classes(self, industrial_classes):
        """Sets the industrial_classes of this V10VmOpenApiGeneralDescriptionIn.

        List of industrial class codes (see http://tilastokeskus.fi/meta/luokitukset/toimiala/001-2008/tekstitiedosto_en.txt).  # noqa: E501

        :param industrial_classes: The industrial_classes of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :type: list[str]
        """

        self._industrial_classes = industrial_classes

    @property
    def current_publishing_status(self):
        """Gets the current_publishing_status of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501

        Current version publishing status.  # noqa: E501

        :return: The current_publishing_status of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :rtype: str
        """
        return self._current_publishing_status

    @current_publishing_status.setter
    def current_publishing_status(self, current_publishing_status):
        """Sets the current_publishing_status of this V10VmOpenApiGeneralDescriptionIn.

        Current version publishing status.  # noqa: E501

        :param current_publishing_status: The current_publishing_status of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :type: str
        """

        self._current_publishing_status = current_publishing_status

    @property
    def required_properties_available_languages(self):
        """Gets the required_properties_available_languages of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501

        Internal property to check the languages within required lists: Names and Descriptions  # noqa: E501

        :return: The required_properties_available_languages of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :rtype: list[str]
        """
        return self._required_properties_available_languages

    @required_properties_available_languages.setter
    def required_properties_available_languages(self, required_properties_available_languages):
        """Sets the required_properties_available_languages of this V10VmOpenApiGeneralDescriptionIn.

        Internal property to check the languages within required lists: Names and Descriptions  # noqa: E501

        :param required_properties_available_languages: The required_properties_available_languages of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :type: list[str]
        """

        self._required_properties_available_languages = required_properties_available_languages

    @property
    def type(self):
        """Gets the type of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501

        Service type. Possible values are: Service, PermitOrObligation or ProfessionalQualification.  # noqa: E501

        :return: The type of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V10VmOpenApiGeneralDescriptionIn.

        Service type. Possible values are: Service, PermitOrObligation or ProfessionalQualification.  # noqa: E501

        :param type: The type of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def service_charge_type(self):
        """Gets the service_charge_type of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501

        Service charge type. Possible values are:  Chargeable or FreeOfCharge.  # noqa: E501

        :return: The service_charge_type of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :rtype: str
        """
        return self._service_charge_type

    @service_charge_type.setter
    def service_charge_type(self, service_charge_type):
        """Sets the service_charge_type of this V10VmOpenApiGeneralDescriptionIn.

        Service charge type. Possible values are:  Chargeable or FreeOfCharge.  # noqa: E501

        :param service_charge_type: The service_charge_type of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :type: str
        """

        self._service_charge_type = service_charge_type

    @property
    def names(self):
        """Gets the names of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501

        List of name entities. Possible type values are: Name, AlternativeName.   Sample single JSON object: {\"language\": \"fi\", \"value\": \"Perhepäivähoito esiopetusikäisille\", \"type\": \"Name\"}.  # noqa: E501

        :return: The names of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :rtype: list[VmOpenApiLocalizedListItem]
        """
        return self._names

    @names.setter
    def names(self, names):
        """Sets the names of this V10VmOpenApiGeneralDescriptionIn.

        List of name entities. Possible type values are: Name, AlternativeName.   Sample single JSON object: {\"language\": \"fi\", \"value\": \"Perhepäivähoito esiopetusikäisille\", \"type\": \"Name\"}.  # noqa: E501

        :param names: The names of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :type: list[VmOpenApiLocalizedListItem]
        """
        if names is None:
            raise ValueError("Invalid value for `names`, must not be `None`")  # noqa: E501

        self._names = names

    @property
    def descriptions(self):
        """Gets the descriptions of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501

        List of description entities. Requires two entities where ones type is \"Description\" or \"BackgroundDescription\" and the other ones type is \"Summary\".  Sample single JSON object: {\"language\": \"fi\", \"value\": \"Lyhyen kuvauksen kuvaus esimerkki teksti.\", \"type\": \"Summary\"}.  Other optional description types are UserInstruction, ChargeTypeAdditionalInfo, DeadLine, ProcessingTime, ValidityTime, GeneralDescriptionTypeAdditionalInformation.  # noqa: E501

        :return: The descriptions of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :rtype: list[VmOpenApiLocalizedListItem]
        """
        return self._descriptions

    @descriptions.setter
    def descriptions(self, descriptions):
        """Sets the descriptions of this V10VmOpenApiGeneralDescriptionIn.

        List of description entities. Requires two entities where ones type is \"Description\" or \"BackgroundDescription\" and the other ones type is \"Summary\".  Sample single JSON object: {\"language\": \"fi\", \"value\": \"Lyhyen kuvauksen kuvaus esimerkki teksti.\", \"type\": \"Summary\"}.  Other optional description types are UserInstruction, ChargeTypeAdditionalInfo, DeadLine, ProcessingTime, ValidityTime, GeneralDescriptionTypeAdditionalInformation.  # noqa: E501

        :param descriptions: The descriptions of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :type: list[VmOpenApiLocalizedListItem]
        """
        if descriptions is None:
            raise ValueError("Invalid value for `descriptions`, must not be `None`")  # noqa: E501

        self._descriptions = descriptions

    @property
    def service_classes(self):
        """Gets the service_classes of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501

        List of service class urls. Sample url: http://urn.fi/URN:NBN:fi:au:ptvl:v1065  # noqa: E501

        :return: The service_classes of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :rtype: list[str]
        """
        return self._service_classes

    @service_classes.setter
    def service_classes(self, service_classes):
        """Sets the service_classes of this V10VmOpenApiGeneralDescriptionIn.

        List of service class urls. Sample url: http://urn.fi/URN:NBN:fi:au:ptvl:v1065  # noqa: E501

        :param service_classes: The service_classes of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :type: list[str]
        """
        if service_classes is None:
            raise ValueError("Invalid value for `service_classes`, must not be `None`")  # noqa: E501

        self._service_classes = service_classes

    @property
    def ontology_terms(self):
        """Gets the ontology_terms of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501

        List of ontology term urls. Sample url: http://www.yso.fi/onto/koko/p2435  # noqa: E501

        :return: The ontology_terms of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :rtype: list[str]
        """
        return self._ontology_terms

    @ontology_terms.setter
    def ontology_terms(self, ontology_terms):
        """Sets the ontology_terms of this V10VmOpenApiGeneralDescriptionIn.

        List of ontology term urls. Sample url: http://www.yso.fi/onto/koko/p2435  # noqa: E501

        :param ontology_terms: The ontology_terms of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :type: list[str]
        """
        if ontology_terms is None:
            raise ValueError("Invalid value for `ontology_terms`, must not be `None`")  # noqa: E501

        self._ontology_terms = ontology_terms

    @property
    def target_groups(self):
        """Gets the target_groups of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501

        List of target group urls. Sample url: http://urn.fi/URN:NBN:fi:au:ptvl:v2004  # noqa: E501

        :return: The target_groups of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :rtype: list[str]
        """
        return self._target_groups

    @target_groups.setter
    def target_groups(self, target_groups):
        """Sets the target_groups of this V10VmOpenApiGeneralDescriptionIn.

        List of target group urls. Sample url: http://urn.fi/URN:NBN:fi:au:ptvl:v2004  # noqa: E501

        :param target_groups: The target_groups of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :type: list[str]
        """
        if target_groups is None:
            raise ValueError("Invalid value for `target_groups`, must not be `None`")  # noqa: E501

        self._target_groups = target_groups

    @property
    def general_description_type(self):
        """Gets the general_description_type of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501

        General description type. Possible values are: Municipality, BusinessSubregion, Church.  # noqa: E501

        :return: The general_description_type of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :rtype: str
        """
        return self._general_description_type

    @general_description_type.setter
    def general_description_type(self, general_description_type):
        """Sets the general_description_type of this V10VmOpenApiGeneralDescriptionIn.

        General description type. Possible values are: Municipality, BusinessSubregion, Church.  # noqa: E501

        :param general_description_type: The general_description_type of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :type: str
        """
        if general_description_type is None:
            raise ValueError("Invalid value for `general_description_type`, must not be `None`")  # noqa: E501

        self._general_description_type = general_description_type

    @property
    def publishing_status(self):
        """Gets the publishing_status of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501

        Publishing status. Possible values are: Draft or Published.  # noqa: E501

        :return: The publishing_status of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :rtype: str
        """
        return self._publishing_status

    @publishing_status.setter
    def publishing_status(self, publishing_status):
        """Sets the publishing_status of this V10VmOpenApiGeneralDescriptionIn.

        Publishing status. Possible values are: Draft or Published.  # noqa: E501

        :param publishing_status: The publishing_status of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :type: str
        """
        if publishing_status is None:
            raise ValueError("Invalid value for `publishing_status`, must not be `None`")  # noqa: E501

        self._publishing_status = publishing_status

    @property
    def delete_all_industrial_classes(self):
        """Gets the delete_all_industrial_classes of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501

        Set to true to delete all existing industrial classes (the IndustrialClasses collection for this object should be empty collection when this option is used).  # noqa: E501

        :return: The delete_all_industrial_classes of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :rtype: bool
        """
        return self._delete_all_industrial_classes

    @delete_all_industrial_classes.setter
    def delete_all_industrial_classes(self, delete_all_industrial_classes):
        """Sets the delete_all_industrial_classes of this V10VmOpenApiGeneralDescriptionIn.

        Set to true to delete all existing industrial classes (the IndustrialClasses collection for this object should be empty collection when this option is used).  # noqa: E501

        :param delete_all_industrial_classes: The delete_all_industrial_classes of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :type: bool
        """

        self._delete_all_industrial_classes = delete_all_industrial_classes

    @property
    def delete_all_laws(self):
        """Gets the delete_all_laws of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501

        Set to true to delete all existing laws within legislation (the legislation collection for this object should be empty collection when this option is used).  # noqa: E501

        :return: The delete_all_laws of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :rtype: bool
        """
        return self._delete_all_laws

    @delete_all_laws.setter
    def delete_all_laws(self, delete_all_laws):
        """Sets the delete_all_laws of this V10VmOpenApiGeneralDescriptionIn.

        Set to true to delete all existing laws within legislation (the legislation collection for this object should be empty collection when this option is used).  # noqa: E501

        :param delete_all_laws: The delete_all_laws of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :type: bool
        """

        self._delete_all_laws = delete_all_laws

    @property
    def delete_all_life_events(self):
        """Gets the delete_all_life_events of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501

        Set to true to delete all existing life events (the LifeEvents collection for this object should be empty collection when this option is used).  # noqa: E501

        :return: The delete_all_life_events of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :rtype: bool
        """
        return self._delete_all_life_events

    @delete_all_life_events.setter
    def delete_all_life_events(self, delete_all_life_events):
        """Sets the delete_all_life_events of this V10VmOpenApiGeneralDescriptionIn.

        Set to true to delete all existing life events (the LifeEvents collection for this object should be empty collection when this option is used).  # noqa: E501

        :param delete_all_life_events: The delete_all_life_events of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :type: bool
        """

        self._delete_all_life_events = delete_all_life_events

    @property
    def delete_service_charge_type(self):
        """Gets the delete_service_charge_type of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501

        Set to true to delete service charge type (ServiceChargeType property for this object should be empty when this option is used).  # noqa: E501

        :return: The delete_service_charge_type of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :rtype: bool
        """
        return self._delete_service_charge_type

    @delete_service_charge_type.setter
    def delete_service_charge_type(self, delete_service_charge_type):
        """Sets the delete_service_charge_type of this V10VmOpenApiGeneralDescriptionIn.

        Set to true to delete service charge type (ServiceChargeType property for this object should be empty when this option is used).  # noqa: E501

        :param delete_service_charge_type: The delete_service_charge_type of this V10VmOpenApiGeneralDescriptionIn.  # noqa: E501
        :type: bool
        """

        self._delete_service_charge_type = delete_service_charge_type

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
        if issubclass(V10VmOpenApiGeneralDescriptionIn, dict):
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
        if not isinstance(other, V10VmOpenApiGeneralDescriptionIn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
