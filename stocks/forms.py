from django import forms
from .models import Alert

class StockTickerForm(forms.Form):
    ticker = forms.CharField(label='Stock Ticker', max_length=10)

class DateRangeForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

class AlertForm(forms.ModelForm):
    class Meta:
        model = Alert
        fields = ['price']