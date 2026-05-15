from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['person', 'company', 'service', 'booking_date', 'status', 'comment']

        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date'}),
        }