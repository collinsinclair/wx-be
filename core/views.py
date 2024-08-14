from rest_framework import viewsets

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
from .serializers import (
    VitalSignSerializer,
    VitalSignDescriptorSerializer,
    CategorySerializer,
    ConditionSerializer,
    TextEntrySerializer,
    PreventionSerializer,
    SignsSymptomsSerializer,
    TreatmentPrincipalsSerializer,
    EvacuationGuidelinesSerializer,
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
    queryset = TextEntry.objects.all()
    serializer_class = TextEntrySerializer


class PreventionViewSet(viewsets.ModelViewSet):
    queryset = Prevention.objects.all()
    serializer_class = PreventionSerializer


class SignsSymptomsViewSet(viewsets.ModelViewSet):
    queryset = SignsSymptoms.objects.all()
    serializer_class = SignsSymptomsSerializer


class TreatmentPrincipalsViewSet(viewsets.ModelViewSet):
    queryset = TreatmentPrincipals.objects.all()
    serializer_class = TreatmentPrincipalsSerializer


class EvacuationGuidelinesViewSet(viewsets.ModelViewSet):
    queryset = EvacuationGuidelines.objects.all()
    serializer_class = EvacuationGuidelinesSerializer
