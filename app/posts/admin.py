from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from commons.admin import AddFieldsetsMixin, short_description
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

    @short_description(_("content"))
    def get_cut_content(self, obj):
        return obj.get_cut_content()

    @short_description(_("likes amount"))
    def get_likes_amount(self, obj):
        return obj.get_likes_amount()
