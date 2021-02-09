from django import forms
from .models import Post
class PostForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control bg-light",
            "placeholder": "Write A Caption...",
            "rows":2,
        })
    )
    image = forms.FileField(required=False,widget=forms.FileInput(
        attrs={
            
        }
    ))

class CommentForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!",
            "rows":1,
            "id":'comment_reply'
        })
    )



class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "body",
            "image",
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            if field == "body":
                self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'rows':2,
                })
                continue
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
    })


    