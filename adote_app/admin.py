from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.http import HttpResponse
from .models import User

# Register your models here.


@admin.register(User)
class PersonAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active', )
    readonly_fields = ('password',)
    search_fields = ('username', 'email',)
    list_filter = ('username', 'email',)

    def alterar_dados(self, request, user):
        user = User.objects.all()
        return HttpResponse(user)
