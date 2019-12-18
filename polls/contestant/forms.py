from django import forms
from .models import Contestant

# This class handles the form that accepts data while creating a new contestant
class ContestantForm(forms.Form):
    name = forms.CharField()
    level = forms.CharField()
    reg_number = forms.CharField()


# =========ends here==========

class ContestantModelForm(forms.ModelForm):
    class Meta:
        model = Contestant
        fields = ['name', 'level', 'reg_number', 'image']

    """
     This functions handles the vetting of creation of new contestants
     to ensure no repetitions are made,
     this is done by checking if a contestant's reg_number already exists
    """
    def clean_reg_number(self, *args, **kwargs):
        instance = self.instance
        name = self.cleaned_data.get('name')
        reg_number = self.cleaned_data.get('reg_number')
        qs = Contestant.objects.filter(reg_number = reg_number)
        if instance is not None:
            qs = qs.exclude(id = instance.id)
        if qs.exists():
            raise forms.ValidationError("This contestant already exists")
        # return reg_number

        #====== validation ends here=====
