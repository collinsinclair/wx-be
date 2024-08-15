from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import *

models: set = {
    VitalSign,
    VitalSignDescriptor,
    Category,
    Condition,
    Note,
    Prevention,
    SignsSymptoms,
    TreatmentPrinciples,
    EvacuationGuidelines,
}


class TextEntryInline(GenericTabularInline):
    model = Note
    extra = 1


@admin.register(Prevention)
class ListModelAAdmin(admin.ModelAdmin):
    inlines = [TextEntryInline]


@admin.register(SignsSymptoms)
class ListModelAAdmin(admin.ModelAdmin):
    inlines = [TextEntryInline]


@admin.register(TreatmentPrinciples)
class ListModelAAdmin(admin.ModelAdmin):
    inlines = [TextEntryInline]


@admin.register(EvacuationGuidelines)
class ListModelAAdmin(admin.ModelAdmin):
    inlines = [TextEntryInline]


already_registered: set = {
    Prevention,
    SignsSymptoms,
    TreatmentPrinciples,
    EvacuationGuidelines,
}
not_registered: set = models - already_registered

for model in not_registered:
    admin.site.register(model)
