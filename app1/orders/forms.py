import re
from django import forms

class CreateOrderForm(forms.Form):
        
    phone_number = forms.CharField()
    delivery_address = forms.CharField()
    land_area = forms.DecimalField()
    land_processing_date = forms.DateField()

    def clean_phone_number(self):
        data = self.cleaned_data['phone_number']

        if not data.isdigit():
            raise forms.ValidationError("Номер телефона должен содержать только цифры")
        
        pattern = re.compile(r'^\d{10}$')
        if not pattern.match(data):
            raise forms.ValidationError("Неверный формат номера")

        return data
