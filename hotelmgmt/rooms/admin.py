from django.contrib import admin
from.models import Room

# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    list_display=('name','price')

admin.site.register(Room,RoomAdmin)
