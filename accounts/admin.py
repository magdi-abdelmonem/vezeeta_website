import site
from django.contrib import admin
from .models import *

admin.site.register(Profile)
#admin.site.register(Evaluation)
admin.site.register(Comment)
