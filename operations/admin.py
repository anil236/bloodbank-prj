from django.contrib import admin
from .models import donater , requestclass

# Register your models here.

admin.site.register(donater)
class donaterAdmin(admin.ModelAdmin):
    list_display =('id','name','birthyear','email','ph_no','address','bloodgroup')
    

admin.site.register(requestclass)
class requestAdmin(admin.ModelAdmin):
    list_display =('user_name','birthyear','email','ph_no','address','bloodgroup')
    