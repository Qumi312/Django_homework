from django import forms


class ProductForm(forms.Form):
    name = forms.CharField(max_length=30)
    description = forms.CharField(
        max_length=2000,
        widget=forms.Textarea( attrs=({"class": "form-control", "placeholder": "Описание"})))
    price = forms.FloatField()
    quantity = forms.IntegerField()
    image = forms.ImageField()
