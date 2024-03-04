from django.contrib import admin
from .models import Paesu_Record

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'user_id_p',
        'date',
        )
    search_fields = ('user_id_p','date',)

admin.site.register(Paesu_Record, UserAdmin)