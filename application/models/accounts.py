from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, UserManager
)

class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(
        'Usuário', max_length=30, null=False, blank=False,
        unique=True, error_messages={'unique' : "Usuário já cadastrado!"},
    )
    name = models.CharField('Nome', max_length=255)
    email = models.EmailField(
        'E-mail', unique=True,
        error_messages = {'unique' : "E-mail já cadastrado!"},
    )
    is_staff = models.BooleanField('Equipe', default=False)
    is_active = models.BooleanField('Ativo', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self) -> str:
        return f'{self.username}'

    def get_full_name(self) ->str:
        return str(self)
