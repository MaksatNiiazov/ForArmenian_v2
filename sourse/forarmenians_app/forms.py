from django import forms

from forarmenians_app.models import *


class VehicleForm(forms.ModelForm):
    photos = AdPhoto
    required_css_class = "submit-auto-select"

    class Meta:
        model = VehicleAd
        fields = "__all__"
