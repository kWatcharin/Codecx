from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class CustomUserAccountManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers 
    for authentication instead of usernames.
    """

    def create_superuser(self, user_name,  password, email, first_name, **other_fields):
        """
        Create and save a User with the given email and password.
        """
        
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assign to is_staff=True.'
            )

        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assign to is_superuser=True.'
            )

        return self.create(user_name, password, email, first_name, **other_fields)


    def create_user(self, user_name, password, email, first_name, telephone_numbers, **other_fields):
        """
        Create and save a User with the given email and password.
        """
        
        if not user_name:
            return ValueError(_('You must provide the user_name.'))
        if not email:
            return ValueError(_('You must provide the email address.'))
        if not first_name:
            return ValueError(_('You must provide the first name.'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, first_name=first_name, telephone_numbers=telephone_numbers,**other_fields)
        user.set_password(password)
        user.save(self.db)
        
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email adress'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    telephone_numbers = models.CharField(max_length=15, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomUserAccountManager()

    USERNAME_FIELD = 'email' 
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']

    class Meta:
        verbose_name_plural = 'UserAccoounts'

    def __str__(self):
        return f"{self.user_name}"

