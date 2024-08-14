from django.db import models

class VitalSign(models.Model):
    abbreviation = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Condition(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Conditions"


class ListBase(models.Model):
    condition = models.ForeignKey(Condition, on_delete=models.PROTECT)
    descriptor = models.CharField(max_length=100)
    list = models.JSONField(default=list, blank=True)

    class Meta:
        abstract = True


class Prevention(ListBase):

    def __str__(self):
        return f"Prevention - {self.descriptor}"

    class Meta:
        verbose_name_plural = "Preventions"


class SignsSymptoms(ListBase):

    def __str__(self):
        return f"Signs/Symptoms - {self.descriptor}"

    class Meta:
        verbose_name_plural = "Signs/Symptoms"


class TreatmentPrincipals(ListBase):

    def __str__(self):
        return f"Treatment Principals - {self.descriptor}"

    class Meta:
        verbose_name_plural = "Treatment Principals"


class EvacuationGuidelines(ListBase):

    def __str__(self):
        return f"Evacuation Guidelines - {self.descriptor}"

    class Meta:
        verbose_name_plural = "Evacuation Guidelines"
