from django import forms


class UserForm(forms.Form):
    first_name = forms.CharField(label='Имя', min_length=2, help_text="HELP TEXT FOR NAME")
    second_name = forms.CharField(label='Фамилия')
    age = forms.IntegerField(label='Возраст', min_value=1)
    number = forms.CharField(label='Номер')
    email = forms.EmailField(widget=forms.TextInput(attrs={"class": "email"}))
    required_css_class = "required"
    error_css_class = "error"


class AnimalForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=155, label='Имя')
    price = forms.IntegerField(min_value=2, max_value=10000, label='Цена')
