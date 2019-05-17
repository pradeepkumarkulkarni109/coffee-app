from django import forms

class UploadFileForm(forms.Form):
    file1 = forms.ImageField(required=False)
    file2 = forms.ImageField(required=False)


class UploadFile(forms.Form):
    file3 =forms.ImageField(required=False)