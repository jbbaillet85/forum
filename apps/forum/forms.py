from apps.forum.models import Forum
from django import forms


class ForumForm(forms.ModelForm):

    class Meta:
        model = Forum
        fields = [
            'name',
        ]
        help_texts = {
            'name': 'Le nom de forum',
        }
