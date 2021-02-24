from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    first_name = None
    last_name = None

    full_name = models.CharField(_("full name"), max_length=254)
