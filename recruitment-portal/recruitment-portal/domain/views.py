from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Domains, Sde, Finance, Electronics, Machine, Gamedev, Datascience
from profiles.models import Profile
from django.views.generic import UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
import requests
from django.contrib.auth.models import auth, User

# @login_required
def list_view(request):
    qs = Domains.objects.all().order_by('created')
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

    return render(request, 'domain/main.html', context)

def sde_view(request):
    qs = Sde.objects.all().order_by('created')
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

    return render(request, 'domain/sde.html', context)

def finance_view(request):
    qs = Finance.objects.all().order_by('created')
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

    return render(request, 'domain/finance.html', context)

def electronics_view(request):
    qs = Electronics.objects.all().order_by('created')
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

    return render(request, 'domain/electronics.html', context)

def machine_view(request):
    qs = Machine.objects.all().order_by('created')
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

    return render(request, 'domain/machine.html', context)

def gamedev_view(request):
    qs = Gamedev.objects.all().order_by('created')
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

    return render(request, 'domain/gamedev.html', context)

def datascience_view(request):
    qs = Datascience.objects.all().order_by('created')
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

    return render(request, 'domain/datascience.html', context)