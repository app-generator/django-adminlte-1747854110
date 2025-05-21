# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Clientes(models.Model):

    #__Clientes_FIELDS__
    nome = models.CharField(max_length=255, null=True, blank=True)

    #__Clientes_FIELDS__END

    class Meta:
        verbose_name        = _("Clientes")
        verbose_name_plural = _("Clientes")


class Parametros(models.Model):

    #__Parametros_FIELDS__
    valor = models.TextField(max_length=255, null=True, blank=True)

    #__Parametros_FIELDS__END

    class Meta:
        verbose_name        = _("Parametros")
        verbose_name_plural = _("Parametros")


class Recursos(models.Model):

    #__Recursos_FIELDS__
    nome = models.CharField(max_length=255, null=True, blank=True)

    #__Recursos_FIELDS__END

    class Meta:
        verbose_name        = _("Recursos")
        verbose_name_plural = _("Recursos")


class Eleicao(models.Model):

    #__Eleicao_FIELDS__
    titulo = models.CharField(max_length=255, null=True, blank=True)
    recursos = models.ForeignKey(Recursos, on_delete=models.CASCADE)
    clientes = models.ForeignKey(Clientes, on_delete=models.CASCADE)

    #__Eleicao_FIELDS__END

    class Meta:
        verbose_name        = _("Eleicao")
        verbose_name_plural = _("Eleicao")



#__MODELS__END
