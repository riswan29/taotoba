# myapp/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
from django.contrib.auth import get_user_model


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    role = models.CharField(max_length=5, choices=ROLE_CHOICES, default='user')
    
    def __str__(self):
        return self.username
    
class BlogPost(models.Model):
    KATEGORI_OPSI = (
        ('Pariwisata', 'Pariwisata'),
        ('Hukum', 'Hukum'),
        ('Agama', 'Agama'),
        ('Edukasi', 'Edukasi'),
    )
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    category = models.CharField(choices=KATEGORI_OPSI, max_length=20)
    kata_kunci = models.TextField()
    content = RichTextUploadingField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    