from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from django import forms
from .models import Students, Assignments, Lecturers


class LoginForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        self.fields['username'].label = 'Enter your name'
        self.error_messages['invalid_login'] = 'INVALID CREDENTIALS!!! Enter your name you used to create an account. \
            Name and password may be case-sensitive.'
        self.fields['username'] = UsernameField(widget=forms.TextInput(attrs={'autocomplete': 'off'}))
        

class SignupForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']


class UpdateProfileForm(forms.ModelForm):
    CHOICE_GENDER = (
        (None, '-- Select your gender --'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    CHOICE_COURSE = (
        (None, '-- Select course --'),
        ('Bsc. in Computer Science', 'Bsc. in Computer Science'),

    )
    CHOICE_SCHOOL = (
        (None, '-- Select your school --'),
        # ('School of Arts, Social Sciences and Business', 'School of Arts, Social Sciences and Business (SASSB)'),
        # ('School of Education', 'School of Education (SE)'),
        # ('School of Information, Communication & Media Studies', 'School of Information, Communication & Media Studies (INFOCOMS)'),
        ('School of Science, Agriculture & Environmental Science', 'School of Science, Agriculture & Environmental Science (SSAES)'),
    )
    CHOICE_YEAR = (
        (None, '-- Year of study --'),
        ('First year', 'First year (Fresher)'),
        ('Second year', 'Second year (Sophomore)'),
        ('Third year', 'Third year (Junior)'),
        ('Fourth year', 'Fourth year (Senior)'),
    )
    CHOICE_SEMESTER = (
        (None, '-- Select semester --'),
        ('1', '1'),
        ('2', '2'),
    )

    gender = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), choices=CHOICE_GENDER)
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel', 'placeholder': 'Enter your mobile no.'}), 
                help_text='<b>Enter your mobile number using your country code</b>, e.g. +254721 ...')
    
    course = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), choices=CHOICE_COURSE)
    school = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), choices=CHOICE_SCHOOL)
    year = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), choices=CHOICE_YEAR)
    semester = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), choices=CHOICE_SEMESTER)
    

    class Meta:
        model = Students
        fields = ['gender', 'phone_number', 'course', 'school', 'reg_no', 'year', 'semester', 'profile_pic']


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = Students
        fields = ['profile_pic']


class UploadAssignmentsForm(forms.ModelForm):
    CHOICE_UNITS = (
        (None, '-- Select unit --'),

    )
    
    unit = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select',}), choices=CHOICE_UNITS,
                help_text='Select the unit name of the assignment you want to upload<br><br>')
    document = forms.FileField(widget=forms.FileInput(attrs={'type': 'file', 'class': 'mb-2'}), 
                validators=[FileExtensionValidator(['doc', 'docx', 'odp', 'ods', 'odt', 'pdf', 'ppt', 'xlsx'])],
                help_text="<br>Supported file formats: .doc, .docx, .odp, .ods, .odt, .pdf, .ppt, .xlsx",

            )

    class Meta:
        model = Assignments
        fields = ['unit', 'document']

