from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from .models import (
    VitalSign,
    VitalSignDescriptor,
    Category,
    Condition,
    TextEntry,
    Prevention,
    SignsSymptoms,
    TreatmentPrincipals,
    EvacuationGuidelines,
)


class VitalSignSerializer(serializers.ModelSerializer):
    class Meta:
        model = VitalSign
        fields = ["id", "abbreviation", "name", "description"]


class VitalSignDescriptorSerializer(serializers.ModelSerializer):
    vital_sign = serializers.PrimaryKeyRelatedField(queryset=VitalSign.objects.all())

    class Meta:
        model = VitalSignDescriptor
        fields = ["id", "vital_sign", "descriptor"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "description"]


class ConditionSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Condition
        fields = ["id", "name", "category"]


class TextEntrySerializer(serializers.ModelSerializer):
    content_type = serializers.PrimaryKeyRelatedField(
        queryset=ContentType.objects.all()
    )
    object_id = serializers.IntegerField()

    class Meta:
        model = TextEntry
        fields = ["id", "content_type", "object_id", "text"]


class PreventionSerializer(serializers.ModelSerializer):
    condition = serializers.PrimaryKeyRelatedField(queryset=Condition.objects.all())

    class Meta:
        model = Prevention
        fields = ["id", "condition", "descriptor"]


class SignsSymptomsSerializer(serializers.ModelSerializer):
    condition = serializers.PrimaryKeyRelatedField(queryset=Condition.objects.all())
    vital_signs = serializers.PrimaryKeyRelatedField(
        queryset=VitalSignDescriptor.objects.all(), many=True
    )
    related_signs_symptoms = serializers.PrimaryKeyRelatedField(
        queryset=SignsSymptoms.objects.all(), many=True
    )
    text_entries = serializers.PrimaryKeyRelatedField(
        queryset=TextEntry.objects.all(), many=True
    )

    class Meta:
        model = SignsSymptoms
        fields = [
            "id",
            "condition",
            "descriptor",
            "vital_signs",
            "related_signs_symptoms",
            "text_entries",
        ]


class TreatmentPrincipalsSerializer(serializers.ModelSerializer):
    condition = serializers.PrimaryKeyRelatedField(queryset=Condition.objects.all())

    class Meta:
        model = TreatmentPrincipals
        fields = ["id", "condition", "descriptor"]


class EvacuationGuidelinesSerializer(serializers.ModelSerializer):
    condition = serializers.PrimaryKeyRelatedField(queryset=Condition.objects.all())

    class Meta:
        model = EvacuationGuidelines
        fields = ["id", "condition", "descriptor"]
