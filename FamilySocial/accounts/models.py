from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from accounts.managers import CustomUserManager


# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Um modelo de usuário abstrato que implementa um usuário completo com
    permissões de administrador compatíveis.

    O nome de usuário e a senha são obrigatórios. Os outros campos são opcionais.
    """

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("nome de usuário"),
        max_length=150,
        unique=True,
        help_text=_(
            "Requerido. 150 caracteres ou menos. " "Letras, dígitos e @/./+/-/_ apenas."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("Já existe um usuário com esse nome de usuário."),
        },
    )

    first_name = models.CharField(_("nome"), max_length=150, blank=True)
    last_name = models.CharField(_("sobrenome"), max_length=150, blank=True)
    email = models.EmailField(_("endereço de e-mail"), blank=True)
    is_staff = models.BooleanField(
        _("status de staff"),
        default=False,
        help_text=_("Designa se o usuário pode logar no site de administração."),
    )
    is_active = models.BooleanField(
        _("ativo"),
        default=True,
        help_text=_(
            "Designa se este usuário deve ser tratado como ativo. "
            "Desmarque ao invés de excluir contas."
        ),
    )
    date_joined = models.DateTimeField(_("data de entrada"), default=timezone.now)

    objects = CustomUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        """Mets Classe para Usuário"""

        verbose_name = _("usuário")
        verbose_name_plural = _("usuários")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Retorna o nome completo, com o sobrenome separado por um espaço do nome.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Retorna o nome curto do usuário."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Envia um e-mail para este usuário."""
        send_mail(subject, message, from_email, [self.email], **kwargs)