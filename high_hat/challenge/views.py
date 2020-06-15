from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils import timezone

from .models import Challenge,ChallengeFromHighhat,Addchallenge,Sample

# Create your views here.
def home(request):
    return render(request, 'home.html')

def challenges(request):
    challenges1 = Challenge.objects
    return render(request, 'challenges.html', { 'challenges1': challenges1 })

def challenge(request, challenge_id):
    challenges2 = get_object_or_404(Challenge, pk=challenge_id)
    return render(request, 'challenge.html', { 'challenges2': challenges2 })

def challengesFromHighhat(request):
    fromHighhats = ChallengeFromHighhat.objects
    return render(request, 'challenges.html', { 'fromHighhats': fromHighhats })

def challengeFromHighhat(request, fromHighhat_id):
    fromHighhat = get_object_or_404(ChallengeFromHighhat, pk=fromHighhat_id)
    return render(request, 'challenge.html', { 'fromHighhat': fromHighhat })


def moreSong(request):
    return render(request, 'moreSong.html')

def samples(request):
    samples = Sample.objects.all()
    return render(request, 'samples.html',{'samples': samples})

def sample(request, sample_id):
    sampledetails = get_object_or_404(Sample, pk = sample_id)
    return render(request, 'sample.html', {'sampledetails' : sampledetails})

def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"], password=request.POST["password1"])
            auth.login(request,user)
            return redirect('home')
    return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

# -------------------------

def new(request):
    return render(request, 'new-challenge.html')

def create(request):
    challenge = Challenge()
    challenge.writer = request.GET.get('writer')
    challenge.title = request.GET.get('title')
    challenge.body = request.GET.get('body')
    challenge.reward = request.GET.get('reward')
    challenge.types = request.GET.get('types')
    challenge.usages = request.GET.get('usages')
    challenge.pub_date = timezone.datetime.now()
    challenge.save()
    return redirect('challenges')

# ---------------------------------------------------

def add(request):
    return render(request, 'add-challenge.html')

def addChallengeCreate(request):
    addChallenge = Addchallenge()
    addChallenge.writer = request.GET.get('writer')
    addChallenge.music = request.GET.get('music')
    addChallenge.pub_date = timezone.datetime.now()
    addChallenge.save()
    return redirect('challenges')

def getAddChallenge(request):
    getAddChallenges = Addchallenge()
    return render(request, 'challenge.html', { 'getAddChallenges': getAddChallenges })

# ---------------------------------------------------

def sample_like(request):
    return render(request, 'sample_like.html')

def sample_download(request):
    return render(request, 'sample_download.html')

def logout(request):
    auth.logout(request)
    return redirect('home')