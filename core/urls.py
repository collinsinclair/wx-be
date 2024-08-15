from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    CategoryViewSet,
    ConditionDetailView,
    ConditionViewSet,
    EvacuationGuidelinesViewSet,
    PreventionViewSet,
    SignsSymptomsViewSet,
    TextEntryViewSet,
    TreatmentPrincipalsViewSet,
    VitalSignDescriptorViewSet,
    VitalSignViewSet,
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
    path(
        "conditions-detail/<int:pk>/",
        ConditionDetailView.as_view(),
        name="condition-detail",
    ),
]
