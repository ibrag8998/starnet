from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    first_name = None
    last_name = None

    full_name = models.CharField(_("full name"), max_length=254, blank=True, null=True)

    last_request = models.DateTimeField(_("last request to the service"), auto_now_add=True)

    REQUIRED_FIELDS = []

    def update_last_request(self):
        self.last_request = timezone.now()
        self.save()
