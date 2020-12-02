from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    phone = forms.CharField()

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        phone = int(cleaned_data.get('phone'))
        if not name and not email and not phone:
            raise forms.ValidationError('You have to write something!')