"""Forms of the project."""

# Create your forms here.
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Thing

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']

    name = forms.CharField(max_length=35, widget=forms.TextInput(attrs={'max_length': '35'}), required=True)
    description = forms.CharField(max_length=120, widget=forms.Textarea, required=False)
    quantity = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(50)],
        widget=forms.NumberInput(attrs={'min': '0', 'max': '50'})
    )
