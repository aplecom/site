from django import forms

class CreateOrderForm(forms.Form):
        
    phone_number = forms.CharField()
    delivery_address = forms.CharField()
    land_area = forms.DecimalField()
    land_processing_date = forms.DateField()
