from django.db import models    

class ClientPresentation(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if other != None:
            if isinstance(other, str):
                return self.name == other
            elif isinstance(other, ClientPresentation):
                return self.name == other.name
        return False

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return self.name < other.name

class Treatment(models.Model):
    OBSERVATION = "OB"
    LONG_TERM_GOAL = "LT"
    SHORT_TERM_OBJECTIVE = "ST"
    THERAPEUTIC_INTERVENTION = "TI"
    CLIENT_PROGRESS = "CP"
    PLAN = "PL"
    TREATMENT_TYPE_CHOICES = [
        (OBSERVATION, "Observation/Assessment"),
        (LONG_TERM_GOAL, "Long Term Goal"),
        (SHORT_TERM_OBJECTIVE, "Short Term Objective"),
        (THERAPEUTIC_INTERVENTION, "Therapeutic Intervention"),
        (CLIENT_PROGRESS, "Client Progress"),
        (PLAN, "Plan for Next Session")
    ]

    treatment_type = models.CharField(
        max_length=2,
        choices=TREATMENT_TYPE_CHOICES,
        default=OBSERVATION)
    description = models.TextField()
    clientPresentation = models.ForeignKey(ClientPresentation, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    def __eq__(self, other):
        if other != None:
            if isinstance(other, str):
                return self.description == other
            elif isinstance(other, ClientPresentation):
                return self.description == other.description
        return self.description == other.description

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return self.description < other.description