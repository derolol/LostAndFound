from django.contrib import admin
from . import models

#FindThingPeople
class FTPAdmin(admin.ModelAdmin):
    list_display = ('thingName', 'findPosition', 'description', 'findTime', 'contactByQQ', 'contactByAddress','contactByWeChat', 'contactByEmail', 'contactByPhone')

admin.site.register(models.FindThingPeople, FTPAdmin)

#LostThingPeople
class LTPAdmin(admin.ModelAdmin):
    list_display = ('thingName', 'lostPosition', 'description', 'lostTime', 'contactByQQ', 'contactByAddress','contactByWeChat', 'contactByEmail', 'contactByPhone')

admin.site.register(models.LostThingPeople, LTPAdmin)
