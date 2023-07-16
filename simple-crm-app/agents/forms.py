from django import forms
from django.contrib.auth import get_user_model

#calling our own custom user 
User = get_user_model()

class AgentModelForm(forms.ModelForm):
    class Meta:
        model = User
        
        fields = (
            'email',
            'username',
            'first_name',
            'last_name',
        )