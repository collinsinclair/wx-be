from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    VitalSignViewSet,
    VitalSignDescriptorViewSet,
    CategoryViewSet,
    ConditionViewSet,
    TextEntryViewSet,
    PreventionViewSet,
    SignsSymptomsViewSet,
    TreatmentPrincipalsViewSet,
    EvacuationGuidelinesViewSet,
)

router = DefaultRouter()
router.register(r"vital-signs", VitalSignViewSet)
router.register(r"vital-sign-descriptors", VitalSignDescriptorViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"conditions", ConditionViewSet)
router.register(r"text-entries", TextEntryViewSet)
router.register(r"preventions", PreventionViewSet)
router.register(r"signs-symptoms", SignsSymptomsViewSet)
router.register(r"treatment-principals", TreatmentPrincipalsViewSet)
router.register(r"evacuation-guidelines", EvacuationGuidelinesViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
