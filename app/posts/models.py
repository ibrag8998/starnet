from html import unescape

from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.html import strip_tags
from django.utils.text import Truncator
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey('users.User', on_delete=models.SET_NULL, related_name='authored_posts', null=True,
                               verbose_name=_("author"))

    content = RichTextUploadingField(_("content"))
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)

    class Meta:
        verbose_name = _("post")
        verbose_name_plural = _("posts")

    def __str__(self):
        return self.get_cut_content()

    def get_cut_content(self):
        return strip_tags(unescape(Truncator(self.content).words(20, html=True, truncate=' …')))

    def get_likes_amount(self):
        return self.likes.count()


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='likes', verbose_name=_("user"),
                             null=True)
    post = models.ForeignKey('posts.Post', on_delete=models.SET_NULL, related_name='likes', verbose_name=_("post"),
                             null=True)

    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)

    class Meta:
        verbose_name = _("like")
        verbose_name_plural = _("likes")
        unique_together = ['user', 'post']

    def __str__(self):
        return f"{self.user} liked post \"{self.post}\""
