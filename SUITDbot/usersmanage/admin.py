from django.contrib import admin

# Register your models here.
from .models import users, teachers, schedules

@admin.register(users)
class usersAdmin(admin.ModelAdmin):
    list_display = ("fname", "id_tg", "groupus")

@admin.register(schedules)
class schedulesAdmin(admin.ModelAdmin):
    list_display = ("group_user",  "dayi", "schedule", "updown")

@admin.register(teachers)
class teachersAdmin(admin.ModelAdmin):
    list_display = ("fname",  "dayi", "schedule", "updown")