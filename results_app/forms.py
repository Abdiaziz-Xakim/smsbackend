# from django import forms
# from django.forms import modelformset_factory

# from academics.models import AcademicSession, AcademicTerm, Subject

# from .models import Result


# class CreateResults(forms.Form):
#     session = forms.ModelChoiceField(queryset=AcademicSession.objects.all())
#     term = forms.ModelChoiceField(queryset=AcademicTerm.objects.all())
#     subjects = forms.ModelMultipleChoiceField(
#         queryset=Subject.objects.all(), widget=forms.CheckboxSelectMultiple
#     )


# EditResults = modelformset_factory(
#     Result, fields=("test_score", "exam_score"), extra=0, can_delete=True
# )

from django import forms
from django.forms import modelformset_factory

from academics.models import AcademicYear, AcademicTerm, Subject

from .models import Result, SubjectResult


class CreateResults(forms.Form):
    session = forms.ModelChoiceField(queryset=AcademicYear.objects.all())
    term = forms.ModelChoiceField(queryset=AcademicTerm.objects.all())
    subjects = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(), widget=forms.CheckboxSelectMultiple
    )


class EditResults(forms.ModelForm):
    class Meta:
        model = SubjectResult
        fields = ["test_score", "exam_score"]
        widgets = {
            "test_score": forms.NumberInput(attrs={"class": "form-control"}),
            "exam_score": forms.NumberInput(attrs={"class": "form-control"}),
        }
