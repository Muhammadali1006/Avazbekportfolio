from django import forms
from index.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ismingizni kiriting', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Emailingizni kiriting', 'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Mavzuni kiriting', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'placeholder': 'Xabaringizni yozing', 'class': 'form-control'}),
        }