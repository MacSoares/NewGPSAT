from django.db import models


class Evaluation(object):
    """Api model for evaluation."""

    def __init__(self):
        name = ""
        age = 0
        gender = ""
        wheight = 0.0
        height = 0.0
        amputationCause = ""
        amputationTime = 0
        amputationType = ""
        symptoms = ""
        medications = ""
        fisioTreatment = ""
        pregressLife = ""
        skinCondition = ""
        skinTemperature = ""
        skinHairandNails = ""
        skinColor = ""
        skinSensibility = ""
        skinConditions = ""
        skinPulses = ""
        deformities = ""
        trofism = ""
        bandaging = ""
        movementAmplitudeFlexion = 0
        movementAmplitudeAbdution = 0
        movementAmplitudeAddution = 0
        musculePowerFlexion = 0
        musculePowerAbdution = 0
        musculePowerAddution = 0
        stumpLength = 0.0
        stumpCircumference = 0.0
        legLength = 0.0
        legCircunference = 0.0
        posturalEvaluation = ""
