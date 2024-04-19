from django.db import models
from django.contrib.auth.models import AbstractUser


class User1(AbstractUser):
    role = models.CharField(max_length=100, null=True, blank=True)
    assigned_TL = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        related_name="developers_tl",
        null=True,
        blank=True,
    )
    assigned_PM = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        related_name="developers_pm",
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        if not self.pk and "is_active" not in kwargs:
            self.is_active = False

        super().save(*args, **kwargs)


class Ticket(models.Model):
    title = models.CharField(max_length=100)
    detail = models.TextField()
    created_by = models.ForeignKey(
        User1, related_name="created_by", on_delete=models.PROTECT
    )
    created_for = models.ForeignKey(
        User1,
        related_name="created_for",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    status = models.CharField(max_length=100, default="assigned", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    user = models.ForeignKey(User1, on_delete=models.PROTECT)
    detail = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commented by {self.user.username} on {self.ticket.title}"
