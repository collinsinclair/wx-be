from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from .models import (
    Category,
    Condition,
    EvacuationGuidelines,
    Prevention,
    SignsSymptoms,
    TextEntry,
    TreatmentPrincipals,
    VitalSign,
    VitalSignDescriptor,
)


class VitalSignSerializer(serializers.ModelSerializer):
    class Meta:
        model = VitalSign
        fields = ["id", "abbreviation", "name", "description"]


class VitalSignDescriptorSerializer(serializers.ModelSerializer):
    vital_sign = VitalSignSerializer()

    class Meta:
        model = VitalSignDescriptor
        fields = ["id", "vital_sign", "descriptor"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "description"]


class ConditionSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Condition
        fields = ["id", "name", "category"]


class TextEntrySerializer(serializers.ModelSerializer):
    content_type = serializers.SlugRelatedField(
        slug_field="model", queryset=ContentType.objects.all()
    )

    class Meta:
        model = TextEntry
        fields = ["id", "content_type", "object_id", "text"]


class PreventionSerializer(serializers.ModelSerializer):
    condition = ConditionSerializer()

    class Meta:
        model = Prevention
        fields = ["id", "condition", "descriptor"]


class SignsSymptomsSerializer(serializers.ModelSerializer):
    condition = ConditionSerializer()
    vital_signs = VitalSignDescriptorSerializer(many=True)
    related_signs_symptoms = serializers.SerializerMethodField()
    text_entries = TextEntrySerializer(many=True)

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

    def get_related_signs_symptoms(self, obj):
        return SignsSymptomsRelatedSerializer(
            obj.related_signs_symptoms.all(), many=True
        ).data


class SignsSymptomsRelatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignsSymptoms
        fields = ["id", "descriptor"]


class TreatmentPrincipalsSerializer(serializers.ModelSerializer):
    condition = ConditionSerializer()

    class Meta:
        model = TreatmentPrincipals
        fields = ["id", "condition", "descriptor"]


class EvacuationGuidelinesSerializer(serializers.ModelSerializer):
    condition = ConditionSerializer()

    class Meta:
        model = EvacuationGuidelines
        fields = ["id", "condition", "descriptor"]


class SignsSymptomsWithTextEntriesSerializer(serializers.ModelSerializer):
    condition = ConditionSerializer()
    vital_signs = VitalSignDescriptorSerializer(many=True)
    related_signs_symptoms = serializers.SerializerMethodField()
    text_entries = TextEntrySerializer(many=True)

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

    def get_related_signs_symptoms(self, obj):
        return SignsSymptomsRelatedSerializer(
            obj.related_signs_symptoms.all(), many=True
        ).data


class TreatmentPrincipalsWithTextEntriesSerializer(serializers.ModelSerializer):
    condition = ConditionSerializer()
    text_entries = TextEntrySerializer(many=True)

    class Meta:
        model = TreatmentPrincipals
        fields = ["id", "condition", "descriptor", "text_entries"]


class EvacuationGuidelinesWithTextEntriesSerializer(serializers.ModelSerializer):
    condition = ConditionSerializer()
    text_entries = TextEntrySerializer(many=True)

    class Meta:
        model = EvacuationGuidelines
        fields = ["id", "condition", "descriptor", "text_entries"]


class ConditionDetailSerializer(serializers.ModelSerializer):
    signs_symptoms = serializers.SerializerMethodField()
    treatment_principals = serializers.SerializerMethodField()
    evacuation_guidelines = serializers.SerializerMethodField()

    class Meta:
        model = Condition
        fields = [
            "id",
            "name",
            "category",
            "signs_symptoms",
            "treatment_principals",
            "evacuation_guidelines",
        ]

    def get_signs_symptoms(self, obj):
        signs_symptoms = obj.signssymptoms_set.prefetch_related("text_entries").all()
        return SignsSymptomsWithTextEntriesSerializer(signs_symptoms, many=True).data

    def get_treatment_principals(self, obj):
        treatment_principals = obj.treatmentprincipals_set.prefetch_related(
            "text_entries"
        ).all()
        return TreatmentPrincipalsWithTextEntriesSerializer(
            treatment_principals, many=True
        ).data

    def get_evacuation_guidelines(self, obj):
        evacuation_guidelines = obj.evacuationguidelines_set.prefetch_related(
            "text_entries"
        ).all()
        return EvacuationGuidelinesWithTextEntriesSerializer(
            evacuation_guidelines, many=True
        ).data
