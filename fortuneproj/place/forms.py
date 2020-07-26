from django import forms

from .models import Place, PlaceComment


# inline_formsetでPlaceとPlaceCommentを同時に取得
class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = '__all__'


class PlaceCommentForm(forms.ModelForm):
    class Meta:
        model = PlaceComment
        fields = ('text', 'user_name')
