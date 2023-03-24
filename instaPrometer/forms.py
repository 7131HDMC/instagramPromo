from django import forms

class InstagramReporterForm(forms.Form):
        email = forms.CharField()
        password = forms.CharField()
        post = forms.CharField()
        comments_template = forms.CharField()

        max_coments = forms.IntegerField()