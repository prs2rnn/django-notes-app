from django.contrib.auth.models import User
from django.db import models
from PIL import Image

from .validators import validate_avatar_extension, validate_avatar_size


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True,
        null=True,
        validators=[validate_avatar_extension, validate_avatar_size],
    )
    bio = models.TextField(blank=True, max_length=30)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        try:
            old_avatar = Profile.objects.get(pk=self.pk).avatar
        except Profile.DoesNotExist:
            old_avatar = None
        super().save(*args, **kwargs)

        if old_avatar and old_avatar != self.avatar and old_avatar.name:
            old_avatar.delete(save=False)

        if self.avatar:
            img = Image.open(self.avatar.path)
            if img.width > 300 or img.height > 300:
                img.thumbnail((300, 300))
                img.save(self.avatar.path)
