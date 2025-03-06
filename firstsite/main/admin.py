from django.contrib import admin

from .models import AdvUser, Topic, HomeWork, Lessons

admin.site.register(Topic)
admin.site.register(Lessons)
admin.site.register(HomeWork)
admin.site.register(AdvUser)
