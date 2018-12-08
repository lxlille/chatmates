from django.contrib import admin
from homepage.models import Friendship
from accounts.models import User
from discussion.models import Discussion

# Register your models here.
admin.site.register(User)
admin.site.register(Friendship)
admin.site.register(Discussion)