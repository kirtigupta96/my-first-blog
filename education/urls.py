from django.conf.urls import url
from . import views


urlpatterns = [
#   url(r'^$', views.login_list, name='login_list'),
    url(r'^$', views.edu_new, name='edu_new'),
    url(r'^profile/', views.edu_uneditable, name='edu_uneditable'),
    url(r'^update/', views.edu_editable, name='edu_editable')
   # url(r'^update/$', views.DetailsUpdate.as_view(), name='Details_Update')
    # url(r'personal/', views.personal_details, name='personal_details'),
    # url(r'internship/', views.internship_details, name='internship_details')
]