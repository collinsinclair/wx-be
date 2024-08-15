from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models


class VitalSign(models.Model):
    abbreviation = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.abbreviation} - {self.name}"

    class Meta:
        verbose_name_plural = "Vital Signs"
        ordering = ["abbreviation"]


class VitalSignDescriptor(models.Model):
    vital_sign = models.ForeignKey(VitalSign, on_delete=models.PROTECT)
    descriptor = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.vital_sign.abbreviation}: {self.descriptor}"

    class Meta:
        verbose_name_plural = "Vital Sign Descriptors"
        unique_together = ("vital_sign", "descriptor")


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


class TextEntry(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    text = models.TextField()

    def __str__(self):
        return self.text[:50]

    class Meta:
        verbose_name_plural = "Text Entries"


class ListBase(models.Model):
    condition = models.ForeignKey(Condition, on_delete=models.PROTECT)
    descriptor = models.CharField(max_length=100, null=True, blank=True)
    text_entries = GenericRelation(TextEntry)

    class Meta:
        abstract = True


class Prevention(ListBase):

    def __str__(self):
        return f"Prevention - {self.descriptor}"

    class Meta:
        verbose_name_plural = "Preventions"


class SignsSymptoms(ListBase):
    vital_signs = models.ManyToManyField(VitalSignDescriptor, blank=True)
    related_signs_symptoms = models.ManyToManyField(
        "self", blank=True, symmetrical=False, related_name="referenced_by"
    )

    def __str__(self):
        return f"S/S of {self.condition.name} - {self.descriptor}"

    class Meta:
        verbose_name_plural = "Signs/Symptoms"


class TreatmentPrincipals(ListBase):

    def __str__(self):
        string_rep: str = f"Tx - {self.condition.name}"
        if self.descriptor:
            string_rep += f"({self.descriptor})"
        return string_rep

    class Meta:
        verbose_name_plural = "Treatment Principals"


class EvacuationGuidelines(ListBase):

    def __str__(self):
        return f"Evacuation Guidelines - {self.descriptor}"

    class Meta:
        verbose_name_plural = "Evacuation Guidelines"
