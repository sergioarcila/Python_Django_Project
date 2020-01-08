from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .forms import FullProfileForm, EditUserForm, EditProfileForm
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from allauth.account.forms import SignupForm
from django.core.mail import send_mail
from .models import PlayerProfile
from payment.models import SubscriptionStatus
import uuid

User = get_user_model()

# Create your views here.
def example(request):
    return render(request, 'profiles/example.html')

@login_required
def home_profile(request):
    if hasattr(request.user, 'playerprofile'):
        return redirect(request.user.playerprofile.get_absolute_url())
    else:
        return redirect(reverse('home'))

def view_profile(request, uuid):
    profile = PlayerProfile.objects.get(id=uuid)
    highlightid = None
    skillsid = None
    if profile.highlight_video_link:
        highlightlink = profile.highlight_video_link
        highlightsplit = highlightlink.split('watch?v=')
        highlightid = highlightsplit[1]
    if profile.skills_video_link:
        skillslink = profile.skills_video_link
        skillssplit = skillslink.split('watch?v=')
        skillsid = skillssplit[1]

    context = {
        'profile': profile,
        'highlightid': highlightid,
        'skillsid': skillsid,
    }
    return render(request, 'profiles/view_profile.html', context)


def all_profiles(request):
    context = {
        'profiles': PlayerProfile.objects.all()
    }
    return render(request, 'profiles/all.html', context)


def edit_profile(request, uuid):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        profile = PlayerProfile.objects.get(id=uuid)
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        userform = EditUserForm(request.POST, instance=profile.user)
        if form.is_valid():
            form.save()

    # if a GET (or any other method) we'll create a blank form
    else:
        profile = PlayerProfile.objects.get(id=uuid)
        form = EditProfileForm(instance=profile)
        userform = EditUserForm(instance=profile.user)

    context = {
        'profile': profile,
        'form': form,
        'userform': userform,
        'formtitle': 'Edit Your Profile',
    }
    return render(request, 'profiles/edit_profile.html', context)


def new_profile(request):
    # try:
    #     request.user.sub_status
    # except SubscriptionStatus.DoesNotExist:
    #     return redirect('signup-pay')

    if request.method == 'POST':
        # profile = request.user.playerprofile
        form = FullProfileForm(request.POST, request.FILES)
        # userform = EditUserForm(request.POST)
        user = request.user
        if form.is_valid():
            print('valid')
            # user = User(email=userform.cleaned_data['email'],
            #             username=userform.cleaned_data['email'],
            #             first_name = userform.cleaned_data['first_name'],
            #             last_name = userform.cleaned_data['last_name'],
            #             password = make_password(userform.cleaned_data['password'])
            #             )
            # user.save()
            instance = form.save(commit=False)
            instance.user = user
            instance.save()

            # new_user = authenticate(username=userform.cleaned_data['email'], password=userform.cleaned_data['password'])
            # login(request, new_user)

            return redirect(instance.get_absolute_url())
            # return redirect(reverse('home'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FullProfileForm()
        # userform = EditUserForm()

    context = {
        # 'profile': request.user.playerprofile,
        'form': form,
        # 'userform': userform,
        'formtitle': 'Sign Up',
    }
    return render(request, 'profiles/edit_profile.html', context)

def new_user(request):
    if request.method == 'POST':
        # profile = request.user.playerprofile
        # userform = EditUserForm(request.POST)
        userform = SignupForm(request.POST)
        if userform.is_valid():
            print('valid')
            userform.save(request)
            # user = User(email=userform.cleaned_data['email'],
            #             username=userform.cleaned_data['email'],
            #             first_name = userform.cleaned_data['first_name'],
            #             last_name = userform.cleaned_data['last_name'],
            #             password = make_password(userform.cleaned_data['password'])
            #             )
            # user.save()
            # email_context = {
            #     'domain': '52dashboard.com',
            #     'token': token_gen.make_token(newuser),
            #     'uid': urlsafe_base64_encode(str(newuser.pk).encode('utf-8')),
            # }
            # msg_plain = render_to_string('accounts/verify_account_email.txt', email_context)
            #
            # send_mail(
            #     'Verify Your Email',
            #     msg_plain,
            #     'BSN Accounts <accounts@bescoutednow.com>',
            #     [user.email],
            #     fail_silently=True,
            # )
            # new_user = authenticate(username=userform.cleaned_data['email'], password=userform.cleaned_data['password'])
            # login(request, new_user)

            # return redirect('email-verification')
            # return redirect(reverse('home'))

    # if a GET (or any other method) we'll create a blank form
    else:
        userform = EditUserForm()

    context = {
        # 'profile': request.user.playerprofile,
        'userform': userform,
        'formtitle': 'Sign Up',
    }
    return render(request, 'profiles/new_user.html', context)
