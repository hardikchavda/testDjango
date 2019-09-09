from django import forms
from blog1.models import studInfo

city_data = [
    ('rkt','Rajkot'),
    ('amd','Ahemedabad'),
    ('sur','Surat')
    ]

class abtusfrm(forms.Form):
    usr = forms.CharField(label="UserName",max_length=10, required=True,initial="Test123")
    pwd = forms.CharField(label="Password",max_length=10, required=True)
    address = forms.CharField(label="Address", max_length=255, required=False,widget=forms.Textarea)
    age  = forms.IntegerField(label="Age", required=True)
    email = forms.EmailField(label='E-Mail', required=True)
    date = forms.DateField(label="BirthDate", required=False,widget=forms.SelectDateWidget())
    city = forms.ChoiceField(label="City", choices=city_data, required=False)
    rmb_me = forms.BooleanField(label="Remember Me..",required=False,initial=False)
    
class dataForm(forms.ModelForm):
    rname = forms.CharField(
        label="Student Full Name",
        max_length=150,
        min_length=10,
        required=True,
        error_messages={
            "required":"Name field is required",
            "min_length":"Please Input min 10 Characters"
            })

    class Meta:
        model = studInfo
        fields = '__all__'
        # fields = ['rname','rcity']
        # exclude = ['rcity']


