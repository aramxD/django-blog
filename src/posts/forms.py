from django.db.models import fields
from django.forms import ModelForm, widgets, Textarea
from .models import *


class  CommentForm(ModelForm): 
    
    class Meta:
        model = Comment
        fields = 'content',
        widgets = {
            'content': Textarea ( attrs={
                'class':'form-control',
                'placeholder':'Type your comment',
                'id':'usercomment',
                'rows':2,
                }
            ),
        }


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'