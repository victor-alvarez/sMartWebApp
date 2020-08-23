from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

USERNAME_REGEX = '^[a-zA-Z0-9.+-]*$'

class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError("Email is required")
        user = self.model(
            username = username,
            email = self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, username, email, password=None):
        user = self.create_user(username, email, password=password)
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name='email address'
    )

    username = models.CharField(
        max_length=255,
        unique=True,
        validators = [
            RegexValidator( regex=USERNAME_REGEX,
                            message='Username must be alphanumeric',
                            code='invalid username')
        ]
    )

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

class Student(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    username = models.CharField(
        max_length=255,
        unique=False,
        validators=[
            RegexValidator(regex=USERNAME_REGEX,
                           message='Username must be alphanumeric',
                           code='invalid username')
        ],
        default='username'
    )

    email = models.EmailField(
        max_length=255,
        unique=False    ,
        verbose_name='email address',
        default='email@email.com'

    )

    def __str__(self):
        return self.username

class Mentor(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    username = models.CharField(
        max_length=255,
        unique=False,
        validators=[
            RegexValidator(regex=USERNAME_REGEX,
                           message='Username must be alphanumeric',
                           code='invalid username')
        ],
        default='username'
    )

    email = models.EmailField(
        max_length=255,
        unique=False,
        verbose_name='email address',
        default='email@email.com'

    )

    def __str__(self):
        return self.username


