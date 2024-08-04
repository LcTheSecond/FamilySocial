from django.db import models

# Create your models here.


class Profile(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="nome")
    last_name = models.CharField(max_length=100, verbose_name="sobrenome")
    date_of_birth = models.DateField(verbose_name="data de nascimento")
    spouse = models.OneToOneField("self", on_delete=models.PROTECT, null=True, blank=True, verbose_name="casal")
    father = models.ForeignKey(
        "self", on_delete=models.PROTECT, null=True, blank=True, related_name="father_children", verbose_name="pai"
    )
    mother = models.ForeignKey(
        "self", on_delete=models.PROTECT, null=True, blank=True, related_name="mother_children", verbose_name="mae"
    )
    date_of_death = models.DateField(null=True, blank=True, verbose_name="data de falecimento")
    phone_number = models.CharField(max_length=20, null=True, blank=True, verbose_name="telefone")
    mobile_number = models.CharField(max_length=20, null=True, verbose_name="celular")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    class Meta:
        verbose_name = "perfil"
        verbose_name_plural = "perfils"