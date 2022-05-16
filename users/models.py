from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin, UserManager

class User(AbstractUser, PermissionsMixin):
    # username = models.CharField(
    #     _('username'),
    #     max_length=150,
    #     unique=True,
    #     help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
    #     validators=[username_validator],
    #     error_messages={
    #         'unique': _("A user with that username already exists."),
    #     },
    # )
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField('Email address', unique=True)
    is_staff = models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.',    )
    is_active = models.BooleanField('active', default=True,
        help_text=(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    #PermissionsMixin inhertin olganimiz uchun 
    # is_superuser
    # is_staff
    # groups

    date_joined = models.DateTimeField('Date joined', auto_now=True)
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['first_name']
    # objects = UserManager()
    # null = False (emaili yo'q foydalanuvhi bo'lmaslik kerak), odatda null=False 
    # unique=True (bitta email bitta foydalanuvchi) shuning uchun blank=True bo'lmaydi
    