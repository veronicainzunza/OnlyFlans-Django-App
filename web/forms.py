from django import forms
from .models import ContactForm, Flan
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email', 'customer_name', 'message']

#class ContactFormForm(forms.Form):
#    customer_email = forms.EmailField(label='Correo (forms.Form)', widget = forms.TextInput(attrs={'style': 'width: 95%;'}))
#    customer_name = forms.CharField(max_length=64, label='Nombre (forms.Form)', widget = forms.TextInput(attrs={'style': 'width: 95%;'}))
#    message = forms.CharField(label ='Mensaje (forms.Form)', widget = forms.Textarea(attrs = {'style': 'width: 95%; height: 150px;'}))
    
class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = "__all__"
        # fields = ("customer_email", "customer_name", "message")
        
        widgets ={
            "customer_email" : forms.TextInput(attrs={'style': 'width: 95%;'}),
            "customer_name" : forms.TextInput(attrs={'style': 'width: 95%;'}),
            "message" : forms.Textarea(attrs = {'style': 'width: 95%; height: 150px;'})
        }
        labels = {
            'customer_email' : 'Correo',
            'customer_name' : 'Nombre',
            'message' : 'Mensaje' 
        }

class FlanForm(forms.ModelForm):
    class Meta:
        model = Flan
        fields = ['flan_uuid', 'name', 'description', 'image_url', 'slug', 'is_private']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Agregar'))

