from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserForm

# Register your models here.
class FormsAdmin(admin.ModelAdmin):
    form = CustomUserForm

admin.site.register(CustomUser, FormsAdmin)