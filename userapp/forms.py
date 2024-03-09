from django.forms import ModelForm
from.models import UserDeatils

class UserForm (ModelForm):
    class Meta:
        model= UserDeatils