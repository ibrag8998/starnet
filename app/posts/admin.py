from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['content']}),
        (_("Other"), {'fields': ['author']})
    ]
    readonly_fields = ['author']
    search_fields = ['content', 'author__full_name']
    list_display = ['get_cut_content', 'author', 'get_likes_amount', 'created_at']

    def get_cut_content(self, obj):
        return obj.get_cut_content()

    get_cut_content.short_description = _("content")

    def get_likes_amount(self, obj):
        return obj.get_likes_amount()

    get_likes_amount.short_description = _("likes amount")
