from django import forms
from .models import VideoJuegos, JuegosDeMesa


class VideoJuegosForm(forms.ModelForm):
    class Meta:
        model = VideoJuegos
        fields = '__all__'


class JuegosDeMesaForm(forms.ModelForm):
    class Meta:
        model = JuegosDeMesa
        fields = '__all__'
