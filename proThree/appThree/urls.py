from django.conf.urls import url
from appThree import views
app_name = 'appThree'
urlpatterns = [
    url('user/$',views.users, name = 'users'),
    url('newuser/$',views.newuser, name ='newuser')
]
