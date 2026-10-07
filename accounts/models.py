from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser
import uuid


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError("Email field required.")
        user = self.model(
            email=email,
            **kwargs
        )
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)

        if kwargs.get("is_staff") is not True:
            raise ValueError("admin must be staff")
        return self.create_user(email, password, **kwargs)


class CustomUser(AbstractUser):
    key = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)    
    username = None
    email = models.EmailField(unique=True)
    contact_number = models.CharField(null=True, blank=True)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.id} | {self.email}"


