from django.contrib import admin
from .models import *

models = [
    Category,
    Condition,
    Prevention,
    SignsSymptoms,
    TreatmentPrincipals,
    EvacuationGuidelines,
]

for model in models:
    admin.site.register(model)
