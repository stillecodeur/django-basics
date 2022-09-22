from django.template.defaulttags import url
from django.urls import include,path
from rest_framework import routers
from gtaapi import views

urlpatterns = [
path('users/', views.user_list),
path('users/<str:id>', views.user_detail),
]


# router = routers.DefaultRouter()
# router.register(r'users/', views.user_list)
# router.register(r'users/(?P<pk>[0-9]+)/', views.user_detail)

# urlpatterns=[
#  path('',include(router.urls))
# ]
