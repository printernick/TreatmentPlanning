from django.db import models    

class ClientPresentation(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

class Treatment(models.Model):
    OBSERVATIONAL = "OB"
    LONG_TERM_GOAL = "LT"
    SHORT_TERM_GOAL = "ST"
    THERAPEUTIC_INTERVENTION = "TI"
    CLIENT_PROGRESS = "CP"
    PLAN = "PL"
    TREATMENT_TYPE_CHOICES = [
        (OBSERVATIONAL, "Observational/Assessment"),
        (LONG_TERM_GOAL, "Long Term Goal"),
        (SHORT_TERM_GOAL, "Short Term Goal"),
        (THERAPEUTIC_INTERVENTION, "Therapeutic Intervention"),
        (CLIENT_PROGRESS, "Client Progress"),
        (PLAN, "Plan for Next Session")
    ]

    treatment_type = models.CharField(
        max_length=2,
        choices=TREATMENT_TYPE_CHOICES,
        default=OBSERVATIONAL)
    description = models.TextField()
    clientPresentation = models.ForeignKey(ClientPresentation, on_delete=models.CASCADE)

    def __str__(self):
        return self.description