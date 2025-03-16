from django import forms
from .models import ContactMessage
from django.core.exceptions import ValidationError
from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'description']  # Fields included in the form


def test_validator(email):
    if email.upper()=="TEST@TEST.TEST":
        raise forms.ValidationError("Why hello there, Mr. Tester!")

class ContactForm(forms.Form):
    name=forms.CharField(max_length=123)
    email=forms.EmailField(validators=[test_validator])
    message=forms.CharField(widget=forms.Textarea)

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model=ContactMessage
        fields=["name","email","message"]
    def clean_email(self):
        email=self.cleaned_data.get("email")
        #print("----------------------")
        if email.upper()=="TEST@TEST.TEST":
            #print(email.upper())
            raise ValidationError("Why hello there, Mr. Tester!")
        return email
 