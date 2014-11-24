from django import forms

class FeedbackForm(forms.Form):
    email = forms.EmailField(label="Your email",required=True)
    name = forms.CharField(label="Your Name")
    subject  = forms.CharField(label="Subject")
    message = forms.CharField(label="Your Message",widget=forms.Textarea)