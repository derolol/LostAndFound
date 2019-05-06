import xadmin
from . import models

#FindThingPeople
class FTPAdmin(object):
    list_display = ('thingName', 'findPosition', 'description', 'findTime', 'contactByQQ', 'contactByAddress', 'contactByWeChat', 'contactByEmail', 'contactByPhone', 'img')

xadmin.site.register(models.FindThingPeople, FTPAdmin)

#LostThingPeople
class LTPAdmin(object):
    list_display = ('thingName', 'lostPosition', 'description', 'lostTime', 'contactByQQ', 'contactByAddress','contactByWeChat', 'contactByEmail', 'contactByPhone', 'img')

xadmin.site.register(models.LostThingPeople, LTPAdmin)
