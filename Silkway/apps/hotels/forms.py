from django import forms
from .models import HotelOrder


class HotelOrderForm(forms.ModelForm):
    def init(self, *args, **kwargs):
        # first call parent's constructor
        super(HotelOrderForm, self).init(*args, **kwargs)
        # there's a fields property now
        self.fields['first_name'].widget.attrs={
            'placeholder': 'Введите имя',
            'class': 'form-control form-control-lg form-control-a'}

        self.fields['last_name'].widget.attrs={
            'placeholder': 'Введите фамилию',
            "class": "form-control form-control-lg form-control-a"}

        self.fields['email'].widget.attrs={
            'placeholder': 'Введите почту',
            "class": "form-control form-control-lg form-control-a"}
        
        self.fields['phone_number'].widget.attrs={
            'placeholder': 'Введите номер телефона',
            "class": "form-control form-control-lg form-control-a"}
        
        self.fields['check_in'].widget.attrs={
            'placeholder': 'Дата заезда',
            "class": "form-control form-control-lg form-control-a"}
        
        self.fields['check_out'].widget.attrs={
            'placeholder': 'Дата выезда',
            "class": "form-control form-control-lg form-control-a"}

    class Meta:
        model = HotelOrder
        fields = ("first_name", "last_name", "email", "phone_number", "check_in", "check_out")
