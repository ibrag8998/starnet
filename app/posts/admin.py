from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from commons.admin import AddFieldsetsMixin
from posts.models import Post


@admin.register(Post)
class PostAdmin(AddFieldsetsMixin, admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['content']}),
        (_("Other"), {'fields': ['author']})
    ]
    add_fieldsets = [
        (None, {'fields': ['content']})
    ]
    readonly_fields = ['author']
    search_fields = ['content', 'author__full_name']
    list_display = ['get_cut_content', 'author', 'get_likes_amount', 'created_at']
