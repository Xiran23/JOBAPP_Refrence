from django import forms
from django.utils.translation import gettext_lazy as _

from subscribe.models import Subscribe 



class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        # fields= ['first_name','last_name','email']
        fields = '__all__'
        # exclude=("first_name")
        labels = {
            'first_name': _('Enter the first name custom label')
            }
        help_texts = {'first_name':_("enter char only")}
        error_message= {
            "first_name":{
                "required":_("you cannot move forward without first name")
            }
        }

# def validate_comma(value):
#     if '' in value:
#         raise forms.ValidationError("Invalid last name")
#     return value 
   

# class SubscribeForm(forms.Form):
#     first_name = forms.CharField(max_length=100,required=False,label="Enter a first name",help_text="will this")
#     last_name = forms.CharField(max_length=100,validators=[validate_comma])
#     email = forms.EmailField(max_length=100)

#     def clean_first_name(self):
#         data = self.clean_data['first_name']
#         if "," in data:
#             raise forms.ValidationError("Invalid first name")
#         return data
    


    