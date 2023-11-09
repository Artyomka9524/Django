from django.contrib import admin
from .models import Coin

class CoinAdmin(admin.ModelAdmin):
    list_display = ['is_eagle', 'create_at']        #формирования списка полей
    ordering = ['is_eagle']              #ортировка 2-х уровневая по полям




admin.site.register(Coin, CoinAdmin)


# Register your models here.
