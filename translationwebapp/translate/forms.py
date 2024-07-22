from django import forms
class TranslationForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, required=False, label='Input Text')
    audio = forms.FileField(required=False, label='Upload Audio')
    target_language = forms.CharField(max_length=5, label='Target Language (e.g., en for English)')

