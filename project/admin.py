from django.contrib import admin
from import_export import resources
from .models import Account, Members
from import_export.admin import ImportExportModelAdmin

class AccountAdmin(admin.ModelAdmin):
    list_display = ('id','name')

admin.site.register(Account,AccountAdmin)

    
class MemberResource(resources.ModelResource):
    class Meta:
        model = Members
        fields = ('id', 'first_name', 'last_name', 'phone_number', 'client_member_id','account')

class MembersAdmin(ImportExportModelAdmin):
    resource_class = MemberResource
    list_display = ('id', 'first_name', 'last_name', 'phone_number', 'client_member_id','account')
    search_fields = ('id','first_name', 'last_name', 'phone_number')
admin.site.register(Members, MembersAdmin)
