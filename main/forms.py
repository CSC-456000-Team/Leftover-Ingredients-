from django import forms

class ContactForm(forms.Form):
	contact_name = forms.CharField(max_length = 50)
	contact_email = forms.CharField(max_length = 150)
	contact_message = forms.CharField(widget=forms.Textarea, max_length = 2000)