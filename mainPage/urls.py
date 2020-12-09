from django.urls import path

from .views import HomePageView, TeamPageView, TeamPageCreate

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('members/', TeamPageView.as_view(),name='members'),
    path('members/add_member', TeamPageCreate.as_view(), name='add_member')
]
