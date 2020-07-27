from django.contrib import admin

from .models import UserFortuneType, FortuneBoard

# Register your models here.
admin.site.register(UserFortuneType)
admin.site.register(FortuneBoard)
