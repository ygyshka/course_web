from django import forms
from mailing.models import Clients, Message, Mailing


class MixinForm:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ClientForm(MixinForm, forms.ModelForm):

    class Meta:
        model = Clients
        fields = '__all__'
        # fields = ('contact_mail', 'full_name', 'comment')


class MessageForm(MixinForm, forms.ModelForm):

    class Meta:
        model = Message
        fields = '__all__'


class MailingForm(MixinForm, forms.ModelForm):

    class Meta:
        model = Mailing
        fields = '__all__'
