from django import forms
from django.core import validators
from first_app.models import User


# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("NAME NEEDS TO START WITH Z")

# class FormName(forms.Form):
#     name = forms.CharField(validators=[check_for_z])
#     email = forms.EmailField()
#     text = forms.CharField(widget=forms.Textarea)
#     botcatcher = forms.CharField(required=False,
#                                  widget=forms.HiddenInput,
#                                  validators=[validators.MaxLengthValidator(0)]
#                                 )

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        if email != vmail:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH!")

class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
