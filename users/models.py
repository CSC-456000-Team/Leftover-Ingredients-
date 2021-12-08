from django.contrib.auth.models import User
from django.db import models
from PIL import Image

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default="profile_pics/default.png", upload_to="profile_pics"
    )

    def __str__(self):
        return f"{self.user.username} Profile"

    # Below code only for handling images in local
    # Connecting S3 using Pillow will casue issue so that comments out

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
