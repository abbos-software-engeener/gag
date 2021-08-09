from django import forms
from .models import Post_Comment


class PostCommentForm(forms.ModelForm):
    class Meta:
        model = Post_Comment
        fields = ['comment', 'image']
        labels = {
            'comment': "Izoh",
            'image': "Rasm"
        }
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 2})
        }