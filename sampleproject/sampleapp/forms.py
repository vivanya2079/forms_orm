from django import forms
from .models import ForgottModel

# class ForgottForm(forms.ModelForm):
#     class Meta:
#         model = ForgottModel
#         fields = [
#             "Email",
#             "PhoneNo",
#         ]
        
        
class ForgottForm(forms.ModelForm):
    class Meta:
        model = ForgottModel
        fields = [
            "Title",
            "Year",
            "Summary",
        ]