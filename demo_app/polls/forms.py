from .models import TODO
from django.forms import ModelForm


# creating a form
class TodoForm(ModelForm):
    class Meta:
        model = TODO
        fields = ["text"]
