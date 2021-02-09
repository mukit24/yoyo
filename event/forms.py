from django import forms
from .models import Event
class DateInput(forms.DateInput):
    input_type = 'date'

class CreateEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            "headline",
            "description",
            "target_amount",
            "present_amount",
            "start_date",
            "end_date",
            "is_present",
        ]
        widgets = {
            'start_date': DateInput(),
            'end_date':DateInput(),
        }

        labels = {
            "is_present":"Runnug Event:"
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            if field == "is_present":
                self.fields[field].widget.attrs.update({
                'style': "margin:7px;"})
            elif field == "description":
                self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'rows':2,})
            else:
                self.fields[field].widget.attrs.update({
                'class': 'form-control'})