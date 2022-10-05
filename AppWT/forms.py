from django import forms
from ckeditor.widgets import CKEditorWidget

class PosteoFormulario(forms.Form):
    titulo=forms.CharField(max_length=120)
    equipo=forms.CharField(max_length=120)
    posteo=forms.CharField(widget = CKEditorWidget())