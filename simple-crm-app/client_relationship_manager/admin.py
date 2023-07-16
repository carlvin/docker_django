from django.contrib import admin
from .models import Client, Device,User,Agent,UserProfile

# Register your models her
admin.site.register(Client)
admin.site.register(Device)
admin.site.register(Agent)
admin.site.register(UserProfile)
admin.site.register(User)
