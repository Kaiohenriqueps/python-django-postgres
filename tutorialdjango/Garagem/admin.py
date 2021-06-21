from django.contrib import admin
from .models import Garagem

# Register your models here.
@admin.register(Garagem)
class GaragemAdmin(admin.ModelAdmin):
    list_display = ("veiculo", "cor")
