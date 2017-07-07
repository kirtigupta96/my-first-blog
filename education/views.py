from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
#from .models import Profile
#from .forms import ProfileForm
from .models import Education
#from .forms import EducationForm
from .forms import SecondaryEducationForm
# from .forms import SeniorSecondaryEducationForm
# from .forms import PersonalDetails
# from .forms import Links
# from .forms import InternshipDetails
from django.views.generic import UpdateView
from .models import Education
from django.db.models import Q
from django.db import transaction



from django.utils import timezone


def edu_new(request):
    if request.method == "POST":
        form = SecondaryEducationForm(request.POST)
        if form.is_valid():
            Education = form.save(commit=False)
            Education.userID = request.user
            Education.created_date = timezone.now()
            Education.save()
    else:
        form= SecondaryEducationForm()

    # if request.method == "POST":
    #     formset = SeniorSecondaryEducationForm(request.POST)
    #     if formset.is_valid():
    #         Education = formset.save(commit=False)
    #         Education.userID = request.user
    #         Education.created_date = timezone.now()
    #         Education.save()
    # else:
    #     formset = SeniorSecondaryEducationForm()
    #
    return render(request, 'education/edu_edit.html', {'form': form,
                                                       })


def edu_editable(request):
    # with transaction.atomic():
        queryset = Education.objects.filter(id='1')
        # if request.method == "POST":
        #     form = q1(request.POST)
        #     # if form.is_valid():
        #     # # Education = form.save(commit=False)
        #     # # Education.userID = request.user
        #     # #Education.created_date = timezone.now()
        #     # Education.save()
        # else:
        #     form = q1()
        return render(request, 'education/edu_editable.html', {'queryset': queryset}
                      )


def edu_uneditable(request):
    queryset = Education.objects.filter(Q(id=2))
    # if request.method == "POST":
    #     form = q1(request.POST)
    #     # if form.is_valid():
    #     # # Education = form.save(commit=False)
    #     # # Education.userID = request.user
    #     # #Education.created_date = timezone.now()
    #     # Education.save()
    # else:
    #     form = q1()

    return render(request, 'education/edu_uneditable.html', {'queryset': queryset}
                  )

    # def DetailsUpdate(request):
#     model = Education
#     fields = ('name', 'homeadd', 'dob', 'contact','gender', 'yoc1', 'board1', 'percentage1', 'yoc2', 'board2', 'percentage2',
#               'yoc3', 'percentage3','college','course',
#               'company_i', 'duration', 'profile_i', 'company_i2', 'duration2', 'profile_i2',
#               'title_p','description_p','skills', 'work', 'git_hub', 'linked_in',)
#     render(request, 'education/')
# def personal_details(request):
#     if request.method == "POST":
#         form = PersonalDetails(request.POST)
#         if form.is_valid():
#             Education = form.save(commit=False)
#             Education.userID = request.user
#             Education.created_date = timezone.now()
#             Education.save()
#     else:
#         form= PersonalDetails()
#
#     if request.method == "POST":
#         formset = Links(request.POST)
#         if formset.is_valid():
#             Education = formset.save(commit=False)
#             Education.userID = request.user
#             Education.created_date = timezone.now()
#             Education.save()
#     else:
#         formset = Links()
#
#     return render(request, 'education/personal_edit.html', {'form': form,
#                                                             'formset': formset})
#
#
# def internship_details(request):
#     if request.method == "POST":
#         form = InternshipDetails(request.POST)
#         if form.is_valid():
#             Education = form.save(commit=False)
#             Education.userID = request.user
#             Education.created_date = timezone.now()
#             Education.save()
#     else:
#         form= InternshipDetails()
#
#     return render(request, 'education/internship.html', {'form': form})