from django.contrib import admin

from .models import User

class CustomUser(admin.ModelAdmin):
    fieldsets=(["Info",{"fields":["user_name","user_password","user_email","is_admin","is_blocked"]}],)
    list_display=["user_name","user_password","user_email","is_admin_user","is_blocked_user"]
    list_filter=["user_name"]
    search_fields=["user_name"]



class InlineUsr(admin.StackedInline):
    model=User
    extra=5



admin.site.register(User,CustomUser)
