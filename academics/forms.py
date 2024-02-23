# from django import forms
# from django.forms import ModelForm, modelformset_factory

# from .models import (
#     AcademicYear,
#     AcademicTerm,
#     SiteConfig,
#     StudentClass,
#     Subject,
# )

# SiteConfigForm = modelformset_factory(
#     SiteConfig,
#     fields=(
#         "key",
#         "value",
#     ),
#     extra=0,
# )


# class AcademicYearForm(ModelForm):
#     prefix = "Academic Session"

#     class Meta:
#         model = AcademicYear
#         fields = ["name", "current"]


# class AcademicTermForm(ModelForm):
#     prefix = "Academic Term"

#     class Meta:
#         model = AcademicTerm
#         fields = ["name", "current"]


# class SubjectForm(ModelForm):
#     prefix = "Subject"

#     class Meta:
#         model = Subject
#         fields = ["name"]


# class StudentClassForm(ModelForm):
#     prefix = "Class"

#     class Meta:
#         model = StudentClass
#         fields = ["name"]


# class CurrentSessionForm(forms.Form):
#     current_session = forms.ModelChoiceField(
#         queryset=AcademicYear.objects.all(),
#         help_text='Click <a href="/session/create/?next=current-session/">here</a> to add new session',
#     )
#     current_term = forms.ModelChoiceField(
#         queryset=AcademicTerm.objects.all(),
#         help_text='Click <a href="/term/create/?next=current-session/">here</a> to add new term',
#     )
