from django import forms
from .models import Computer
from django.core.validators import RegexValidator
from .wol import check_hash

class SelectComputer(forms.Form):
    computers = forms.ModelChoiceField(queryset=Computer.objects.all(),label="Select a Computer")
    pwd = forms.CharField(widget=forms.PasswordInput,label="Site Password")

    def clean_pwd(self):
        pwd = self.cleaned_data['pwd']
        if check_hash(pwd):
            return pwd
        raise forms.ValidationError("Invalid Password")



class ComputerForm(forms.ModelForm):
    mac_addr = forms.RegexField(regex=r'^([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F])$',label="MAC Address (00:00:00:00:00:00)")
    ip_addr = forms.RegexField(regex=r'^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$',label="IP Address")

    pwd = forms.CharField(widget=forms.PasswordInput,label="Site Password")

    def clean_pwd(self):
        pwd = self.cleaned_data['pwd']
        if check_hash(pwd):
            return pwd
        raise forms.ValidationError("Invalid Password")

    class Meta:
        model = Computer
        fields = ('name', 'ip_addr', 'mac_addr')