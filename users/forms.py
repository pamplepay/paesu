from .models import User

from django import forms
from django.contrib.auth.hashers import check_password


class LoginForm(forms.Form):
    user_id = forms.CharField(
        widget=forms.TextInput(
        attrs={'class': 'form-control',}), 
        max_length=16,
        label='아이디'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
        attrs={'class': 'form-control',}),
        label='비밀번호'
    )
    
    def clean(self):
        cleaned_data = super().clean()
        user_id = cleaned_data.get('user_id')
        password = cleaned_data.get('password')

        if user_id and password:
            try:
               user = User.objects.get(user_id=user_id)
            except User.DoesNotExist:
                self.add_error('user_id', '아이디가 존재하지 않습니다.')
                return
            
            if not check_password(password, user.password):
                self.add_error('password', '비밀번호가 틀렸습니다.')
