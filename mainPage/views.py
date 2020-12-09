from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView

from .models import Member


class HomePageView(TemplateView):
    template_name = 'home.html'


class TeamPageView(ListView):
    template_name = 'members/index.html'

    queryset = Member.objects.all()
    context_object_name = 'members'


class TeamPageCreate(CreateView):
    model = Member
    template_name = 'members/member_new.html'
    fields = ['name','role','email','image_link']

class MemberPageUpdate(UpdateView):
    model = Member
    template_name = 'members/member_upd.html'
    field = ['']
