from django import forms

class SubmissionForm(forms.Form):
    to_check = forms.FileField(allow_empty_file=False, required=True)