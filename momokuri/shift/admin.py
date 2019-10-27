from django.contrib import admin

# Register your models here.
from .models import Submit


class SubmitAdmin(admin.ModelAdmin):
    list_display = ('sort_id', 'name', 'memo', 'd1s', 'd1e', 'd2s', 'd2e', 'd3s', 'd3e', 'd4s',
                    'd4e', 'd5s', 'd5e', 'd6s', 'd6e', 'd7s', 'd7e', 'd8s', 'd8e', 'd9s', 'd9e',
                    'd10s', 'd10e', 'd11s', 'd11e', 'd12s', 'd12e', 'd13s', 'd13e', 'd14s', 'd14e',
                    'd15s', 'd15e', 'd16s', 'd16e')


admin.site.register(Submit, SubmitAdmin)
