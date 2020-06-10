from .models import TourOrder
from django import forms



class TourOrderForm(forms.ModelForm):
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
    class Meta:
        model = TourOrder
        fields = ("first_name", "last_name", "email", "phone_number")