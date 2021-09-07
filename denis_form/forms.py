from django import forms
from django.forms import ModelForm
from .models import Token
import random


class TokenForm(forms.ModelForm):
    class Meta:
        model = Token
        fields = ['firstname', 'lastname','email','department_to_visit','purpose','address','phone']


    def save(self):

        order = super().save(commit=False)
        order.token = self.queue_token()
        order.save()

    def queue_token(self):
        alphabets = "A"
        numbers = "01234"
        alpha_numeric = alphabets + numbers
        length = 5
        generate_token = "".join(random.sample(alpha_numeric, length))
        if Token.objects.filter(token=generate_token).exists():
            token = "".join(random.sample(alpha_numeric, length))
            return token
        else:
            return generate_token