from django import forms
from django.core import validators

class contactForm(forms.Form):
    name = forms.CharField(label="Your Name: ", initial="Abdul Khaleq", help_text="You must write your fullname", required=False, disabled=False, widget=forms.Textarea(attrs={'id': 'text_area', 'class': 'class1 class2', 'placeholder':'Enter your name'}))
    file = forms.FileField()
    # email = forms.EmailField(label="User Email")
    # age =forms.IntegerField()
    age =forms.CharField(widget=forms.DateInput(attrs={'type':'date'}))
    # weigth =forms.FloatField()
    # balance =forms.DecimalField()
    # check = forms.BooleanField()
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    appointment = forms.DateTimeField(widget=forms.DateInput(attrs={'type':'datetime-local'}))
    CHOICE = [('S','Small'),('M','Medium'),('L','Large')]
    size = forms.ChoiceField(choices=CHOICE, widget=forms.RadioSelect)
    MEAL = [('P','Pepperoni'),('M','Mashroom'),('B','Beef')]
    pizza = forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)

# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)
    # def clean_name(self):
    #     valName = self.cleaned_data['name']
    #     if len(valName) < 10:
    #         raise forms.ValidationError("Enter name with at least 10 characters")
    #     return valName
    # def clean_email(self):
    #     valEmail = self.cleaned_data['email']
    #     if '.com' not in valEmail:
    #         raise forms.ValidationError("Your email must contain .com")
    #     return valEmail
    def clean(self):
        clean_data = super().clean()
        nameVal = self.cleaned_data['name']
        emailVal = self.cleaned_data['email']
        if len(nameVal) < 10:
            raise forms.ValidationError("Enter name with at least 10 characters")
        if '.com' not in emailVal:
            raise forms.ValidationError("Your email must contain .com")

def len_check(value):
    if len(value) < 10:
        raise forms.ValidationError('Enter a value at least 10 chars')
class StudentData(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(10, message='Enter name with at least 10 characters')])
    text = forms.CharField(widget=forms.TextInput, validators=[len_check])
    email = forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator(message='Enter a valid Email')])
    age = forms.IntegerField(validators=[validators.MinValueValidator(18, message='Age must be at least 18'), validators.MaxValueValidator(32, message='Age must be max 32')])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf', 'png'], message='File Extension must be ended with .pdf')])

class passwordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        con_pass = self.cleaned_data['confirm_password']
        val_name = self.cleaned_data['name']
        if val_pass != con_pass:
            raise forms.ValidationError("Password doesn't match")
        if len(val_name) < 10:
            raise forms.ValidationError('Name must be at least 10 chars')