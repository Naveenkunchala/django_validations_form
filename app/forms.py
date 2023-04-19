from django import forms
g=[('MALE','male'),('FEMALE','female')]
c=[['PYTHON','python'],('JAVA','java'),['SQL','sql']]


class studentForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    url=forms.URLField()
    email=forms.EmailField()
    date=forms.DateTimeField()
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    address=forms.CharField(max_length=100,widget=forms.Textarea(attrs={'cols':10,'rows':10}))
    #gender=forms.ChoiceField(choices=g)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    #course=forms.MultipleChoiceField(choices=c)
    course=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)
    
    
    