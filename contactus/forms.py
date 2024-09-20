from django import forms
from .models import Message

class MessageRequest(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['firstName', 'lastName', 'companyName', 'mobile', 'email', 'messageText']