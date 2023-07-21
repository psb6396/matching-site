from .widgets import  DateTimePickerInput
from django.forms import ModelForm
from .models import My_user

class ExampleForm(ModelForm):
    class Meta:
        model = My_user
        fields = ['available_time', 'start_date', 'end_date']

        widgets = {
            'available_time' : DateTimePickerInput(),
            'start_date' : DateTimePickerInput(),
            'end_date' : DateTimePickerInput(),
        }