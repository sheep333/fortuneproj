from django import forms


class UserInfoForm(forms.Form):
    name = forms.CharField(max_length=30)
    birthday = forms.DateField(
        input_formats=('%Y-%m-%d', '%Y/%m/%d')
    )

    def clean_birthday(self):
        data = self.cleaned_data["birthday"]
        if data is None:
            self.add_error('birthday', '2020-1-1もしくは2020/1/1の形式で入力してください。')
        return data
