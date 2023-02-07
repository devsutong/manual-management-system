from django import forms
from  .models import Item


class ItemDetailForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        exclude = ("qrcode",)