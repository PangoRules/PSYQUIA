from django.contrib import admin
from account.models import Account
# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'nombres', 'date_joined', 'last_login',)
    list_filter = ('date_joined',)
    exclude = ('is_admin', 'is_staff', 'is_superuser',)
    search_fields = ('nombres', 'email')
    list_per_page = 

    def get_queryset(self, request):
        return Account.objects.filter(is_superuser=False)
    

admin.site.register(Account,AccountAdmin)