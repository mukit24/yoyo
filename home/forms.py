from django import forms
from .models import Contributer_Profile,Volunteer_Profile

class VolunteerProfileForm(forms.ModelForm):
    class Meta:
        model = Volunteer_Profile
        labels = {
            "full_name":"Full Name(if team then team name):",
            "profession":"Profession(Optional):",
            "facebook":"Facebook Link(Optional):",
            "about_me":"About(Optional):",
        }
        fields = [
            "full_name",
            "profile_picture",
            "profession",
            "address",
            "mobile",
            "facebook",
            "about_me",
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            if field == "about_me":
                self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'rows':3,
                })
            else:
                self.fields[field].widget.attrs.update({
                'class': 'form-control'})


class ContributerProfileForm(forms.ModelForm):
    class Meta:
        model = Contributer_Profile
        labels = {
            "facebook":"Facebook Link(Optional):",
            "about_me":"About(Optional):",
        }
        fields = [
            "full_name",
            "profile_picture",
            "profession",
            "address",
            "mobile",
            "facebook",
            "about_me",
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            if field == "about_me":
                self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'rows':3,
                })
            else:
                self.fields[field].widget.attrs.update({
                'class': 'form-control'})