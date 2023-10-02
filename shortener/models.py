from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from shortener.service import shortcode


class Shorturl(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    url = models.URLField(_("URL"), max_length=500)
    identifier = models.CharField(
        _("Short URL"), default=shortcode, max_length=8, unique=True, editable=False
    )
    created = models.DateTimeField(_("Created"), auto_now_add=True)

    class Meta:
        verbose_name = _("shorturl")
        verbose_name_plural = _("shorturls")
        ordering = ["-created"]

    def __str__(self):
        return self.url

    def get_absolute_url(self):
        return reverse("shorturl_detail", kwargs={"identifier": self.identifier})
