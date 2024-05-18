# в файле forms.py вашего приложения

from django import forms

class MyForm(forms.Form):
    my_choices = [(1, 'Билл Гейтс'), (2, 'Линукс Торвальдс'), (3, 'Марк Цукерберг')]
    my_field = forms.ChoiceField(choices=my_choices, widget=forms.Select(attrs={'min': '1'}))
