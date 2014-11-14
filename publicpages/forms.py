from django import forms

class FeedbackForm(forms.Form):
    email = forms.EmailField(label="Your email")
    name = forms.CharField(label="Your Name")
    message = forms.CharField(label="Your Message",widget=forms.Textarea)