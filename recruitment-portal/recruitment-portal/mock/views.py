from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from . models import Mock, MockIt
from django.urls import reverse_lazy
from profiles.models import Profile
from django.views.generic import UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
import requests
from django.contrib.auth.models import auth, User

def list_view(request):
    qs = MockIt.objects.all().order_by('created')
    paginator = Paginator(qs, 6)
    page_number = request.GET.get('page')
    qsfinal = paginator.get_page(page_number)
    total_pages = qsfinal.paginator.num_pages

    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
    else:
        profile = None
    context = {
        'qs': qsfinal,
        'profile': profile,
        'lastpage': total_pages,
        'totalPageList': [n+1 for n in range(total_pages)]
    }

    return render(request, 'main.html', context)

def dbms_view(request):
    paginator= Paginator(Mock.objects.all(),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj":page_obj}
    return render(request,"index.html",context)