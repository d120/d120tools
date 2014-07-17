from django.db import models
from django.contrib import auth
import hashlib, base64

from django.contrib.auth.models import (
    UserManager, AbstractBaseUser, PermissionsMixin
)


class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = "auth_user"
    username = models.CharField('username', unique=True, max_length=40)
    password2 = models.CharField('password2', max_length=128)
    
    first_name = models.CharField('first_name', max_length=40)
    last_name = models.CharField('last_name', max_length=40)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
    )
    date_of_birth = models.DateField(blank=True, null=True)
    date_joined = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    def get_short_name(self):
        return self.username
    
    def set_password(self, raw_password):
        super(auth.models.User, self).set_password(raw_password)
        self.password2 = "{SHA}%s" % (base64.b64encode(hashlib.sha1(raw_password).digest()))
    

from django.contrib.auth import models as auth_models
auth_models.User = User


