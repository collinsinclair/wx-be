from rest_framework import generics, viewsets

from .models import (
    Category,
    Condition,
    EvacuationGuidelines,
    Prevention,
    SignsSymptoms,
    Note,
    TreatmentPrinciples,
    VitalSign,
    VitalSignDescriptor,
)
from .serializers import (
    CategorySerializer,
    ConditionDetailSerializer,
    ConditionSerializer,
    EvacuationGuidelinesSerializer,
    PreventionSerializer,
    SignsSymptomsSerializer,
    TextEntrySerializer,
    TreatmentPrincipalsSerializer,
    VitalSignDescriptorSerializer,
    VitalSignSerializer,
)


class VitalSignViewSet(viewsets.ModelViewSet):
    queryset = VitalSign.objects.all()
    serializer_class = VitalSignSerializer


class VitalSignDescriptorViewSet(viewsets.ModelViewSet):
    queryset = VitalSignDescriptor.objects.all()
    serializer_class = VitalSignDescriptorSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ConditionViewSet(viewsets.ModelViewSet):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer


class TextEntryViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = TextEntrySerializer


class PreventionViewSet(viewsets.ModelViewSet):
    queryset = Prevention.objects.all()
    serializer_class = PreventionSerializer


class SignsSymptomsViewSet(viewsets.ModelViewSet):
    queryset = SignsSymptoms.objects.all()
    serializer_class = SignsSymptomsSerializer


class TreatmentPrincipalsViewSet(viewsets.ModelViewSet):
    queryset = TreatmentPrinciples.objects.all()
    serializer_class = TreatmentPrincipalsSerializer


class EvacuationGuidelinesViewSet(viewsets.ModelViewSet):
    queryset = EvacuationGuidelines.objects.all()
    serializer_class = EvacuationGuidelinesSerializer


class ConditionDetailView(generics.RetrieveAPIView):
    queryset = Condition.objects.all()
    serializer_class = ConditionDetailSerializer

    def get_queryset(self):
        return Condition.objects.prefetch_related(
            "signssymptoms_set__vital_signs",
            "signssymptoms_set__text_entries",
            "treatmentprincipals_set__text_entries",
            "evacuationguidelines_set__text_entries",
        )
