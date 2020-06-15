from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

import challenge.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', challenge.views.home, name="home"),
    path('challenges/', challenge.views.challenges, name="challenges"),
    path('challenges/', challenge.views.challengesFromHighhat, name="challengesFromHighhat"),
    path('challenge/<int:challenge_id>', challenge.views.challenge, name="challenge"),
    path('challenge/<int:fromHighhat_id>', challenge.views.challengeFromHighhat, name="fromHighhat"),
    path('new/', challenge.views.new, name="new"),
    path('challenge/create', challenge.views.create, name="create"),
    path('add-challenge/', challenge.views.add, name="add-challenge"),
    path('challenge/add1', challenge.views.addChallengeCreate, name="add1"),
    path('moreSong/', challenge.views.moreSong, name="moreSong"),
    path('login/', challenge.views.login, name="login"),
    path('signup/', challenge.views.signup, name="signup"),
    path('dashboard/', challenge.views.dashboard, name="dashboard"),
    path('samples/', challenge.views.samples, name="samples"),
    path('samples/sample/<int:sample_id>', challenge.views.sample, name="sample"),
    path('logout/', challenge.views.logout, name="logout"),
    path('sample_like/', challenge.views.sample_like, name="sample_like"),
    path('sample_download/', challenge.views.sample_download, name="sample_download"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)