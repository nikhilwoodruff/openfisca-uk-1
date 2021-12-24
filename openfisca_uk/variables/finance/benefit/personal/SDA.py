from openfisca_uk.model_api import *


class SDA(Variable):
    value_type = float
    entity = Person
    label = u"Severe Disablement Allowance"
    definition_period = YEAR

    def formula(person, period, parameters):
        return person("SDA_reported", period)


class SDA_reported(Variable):
    value_type = float
    entity = Person
    label = u"Severe Disablement Allowance (reported)"
    definition_period = YEAR
