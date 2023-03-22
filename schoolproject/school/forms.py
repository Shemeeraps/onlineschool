from django import forms


class updateprofile(forms.Form):
    name=forms.CharField(max_length=250,label="Your Name..",required=True)
    dob=forms.DateField()
    age=forms.IntegerField(label="Your age..")
    phone=forms.IntegerField(label="Your contact number..")
    email=forms.EmailField(label="Your email id")
    address=forms.CharField(max_length=1000,label="Your address")
    choices=[('M','Male'),('F','Female'),('Others','Others')]
    gender=forms.CharField(label='Gender',widget=forms.RadioSelect(choices=choices))
    purpose_choice=[
        ('Enquiry','ENQUIRY'),
        ('Place Order','PLACE ORDER'),
        ('Casual Browsing','CASUAL BROWSING')
    ]
    purpose= forms.CharField(label='Purpose', widget=forms.Select(choices=purpose_choice))
    material_choice=[
        ('Question Papers','QUESTION PAPERS'),
        ('Sample Project','SAMPLE PROJECT'),
        ('Pdf','PDF'),
        ('Videos','VIDEOS')
    ]
    material=forms.CharField(label='Material', widget=forms.Select(choices=material_choice))





