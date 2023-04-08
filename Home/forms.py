from django.forms import ModelForm
from .models import Note

class CreateNote(ModelForm):
    class Meta:
        model  = Note
        fields = ['title', 'body']