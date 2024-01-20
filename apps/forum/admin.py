from django.contrib import admin
from apps.forum.models import Forum

# Register your models here.
class ForumAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ["name"]


admin.site.register(Forum, ForumAdmin)