from django.contrib import admin
from .models import Account, Members

class AccountAdmin(admin.ModelAdmin):
    list_display = ('id','name')

admin.site.register(Account,AccountAdmin)

class MembersAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone_number', 'client_member_id','account')
    search_fields = ('first_name', 'last_name', 'phone_number')

admin.site.register(Members, MembersAdmin)
