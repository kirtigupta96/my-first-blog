from django import forms
#from .models import Profile
from .models import Education

# class ProfileForm(forms.ModelForm):
#
#     class Meta:
#         model = Profile
#         fields = ('firstName', 'lastName', 'contact')


CATEGORIES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)


class SecondaryEducationForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=CATEGORIES, required=True)

    class Meta:
        model = Education
        fields = ('name', 'homeadd', 'dob', 'contact','gender', 'yoc1', 'board1', 'percentage1', 'yoc2', 'board2', 'percentage2',
                  'yoc3', 'percentage3','college','course',
                  'company_i', 'duration', 'profile_i', 'company_i2', 'duration2', 'profile_i2',
                  'title_p','description_p','skills', 'work', 'git_hub', 'linked_in',)

#class EducationForm(forms.ModelForm):

# class SecondaryEducationForm(forms.ModelForm):
#     class Meta:
#         model = Education
#         fields = ('yoc1', 'board1', 'percentage1', 'yoc2', 'board2', 'percentage2', 'college', 'dob',
#                   'name', 'contact', 'git_hub', 'linked_in', 'company','duration','work',)
#         labels = {
#             'yoc1': "Year of completion(1)",
#             'board1':"Name of the Board",
#             'percentage1': "Percentage/ CGPA",
#             'yoc2': "Year of completion(2)",
#             'board2': "Name of the Board",
#             'percentage2': "Percentage/ CGPA",
#             'name': "Name of the Applicant",
#             'college': "Name of the College",
#             'dob': "Date Of Birth",
#             #'add': "Permanent Address",
#             'contact': "Contact No.",
#             'git_hub': "Add link to GitHub Profile",
#             'linked_in': "Add link to Linkedin Profile",
#             'company': "Name of the Company",
#             'duration': "Duration of Internship(in months)",
#             'work': "Work Profile/Designation",
#         }