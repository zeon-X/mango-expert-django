from django import forms
from .models import MangoExport

class MangoExportForm(forms.ModelForm):
    class Meta:
        model = MangoExport
        fields = ['variety', 'description', 'price']

    def clean_variety(self):
        variety = self.cleaned_data['variety']
        if MangoExport.objects.filter(variety=variety).exists():
            raise forms.ValidationError("Variety name already exists!")
        return variety
