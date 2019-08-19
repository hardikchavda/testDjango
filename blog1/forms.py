from django import forms

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
    date = forms.DateField(label="BirthDate", required=False)
    city = forms.ChoiceField(label="City", choices=city_data, required=False)
    rmb_me = forms.BooleanField(label="Remember Me..",required=False,initial=False)
    

