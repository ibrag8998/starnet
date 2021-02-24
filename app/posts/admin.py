from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['content']}),
        (_("Other"), {'fields': ['author']})
    ]
    readonly_fields = ['author', 'created_at']
    search_fields = ['content']
    list_display = ['__str__', 'author', 'get_likes_amount', 'created_at']
