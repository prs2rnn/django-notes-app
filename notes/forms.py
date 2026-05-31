from django import forms

from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'body', 'author']
        labels = {
            'title': 'Note title',
            'body': 'Note body',
            'author': 'Your name (optional)',
        }
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter the note title...',
                }
            ),
            'body': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 5,
                    'placeholder': 'Enter the text of the note...',
                }
            ),
            'author': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }
