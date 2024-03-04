
from .choices import *
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, user_id, password, hp, email,
                    business_name, business_add, business_regnum, region, **extra_fields):
        
        user = self.model(
            user_id = user_id,

            hp = hp,
            email = email,
            business_name = business_name,
            business_add = business_add,
            business_regnum = business_regnum,
            region = region,

            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, user_id, password, hp=None, email=None,
                         business_name=None, business_add=None, business_regnum=None, region=None):

        user = self.create_user(user_id, password, hp, email, business_name, business_add, business_regnum, region)
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.level = 0
        user.save(using=self._db)

        return user



class User(AbstractBaseUser, PermissionsMixin):
    
    objects = UserManager()

    user_id = models.CharField(max_length=15, verbose_name="아이디", unique=True)
    password = models.CharField(max_length=256, verbose_name="비밀번호")

    hp = models.CharField(max_length=11, verbose_name="휴대폰번호", null=True)
    email = models.CharField(max_length=33, verbose_name="이메일", null=True, unique=True)
    level = models.CharField(choices=LEVEL_CHOICES, max_length=18, verbose_name="등급", default=2)

    business_name = models.CharField(max_length=33, verbose_name="사업자상호", null=True)
    business_add = models.CharField(max_length=33, verbose_name="사업자주소", null=True)
    business_regnum = models.CharField(max_length=33, verbose_name="사업자등록번호", null=True)
    region = models.CharField(choices=REGION_CHOICES, max_length=18, verbose_name="지역", null=True)


    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='가입일', null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['email']
    
    def __str__(self):
        return self.user_id

    class Meta:
        db_table = "USER_TB"
        verbose_name = "사용자"
        verbose_name_plural = "사용자"
