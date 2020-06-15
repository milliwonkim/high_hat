from django.contrib import admin
from .models import Challenge, ChallengeFromHighhat, Addchallenge, Sample

# Register your models here.
admin.site.register(Challenge)
admin.site.register(ChallengeFromHighhat)
admin.site.register(Addchallenge)
admin.site.register(Sample)