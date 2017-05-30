# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# TODO: Hacer todos los metodos


class Profile(models.Model):
    id_perfil = models.AutoField(primary_key=True)
    avatar = models.ImageField("Avatar", upload_to="./media/user-avatars/", null=True,
                               default='./media/default/defaultUsr.png')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField("email", max_length=225)
    nombre = models.CharField("nombre", max_length=64, null=False)
    apellido = models.CharField("apellido", max_length=64, null=False)
    barrio = models.CharField("barrio", max_length=128, null=False)

    def get_cpc(self):
        return self.cpcCentro

    def __unicode__(self):
        return "Perfil::" + self.user.username


class CpcCentro(models.Model):
    id_cpc = models.AutoField(primary_key=True)
    nombre = models.CharField("nombre", max_length=225, null=False)
    barrio = models.CharField("barrio", max_length=64, null=False)
    perfil = models.ForeignKey(Profile, on_delete=models.CASCADE)


class Aula(models.Model):
    id_aula = models.AutoField(primary_key=True)
    nombre_aula = models.CharField("nombre_aula", max_length=64, null=False)
    capacidad = models.IntegerField("capacidad del aula")
    cpcCentro = models.ForeignKey(CpcCentro, on_delete=models.CASCADE)


class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    titulo = models.CharField("titulo", max_length=120)

    def __unicode__(self):
        return "Categoria: :" + self.titulo


class Album(models.Model):
    id_album = models.AutoField(primary_key=True)
    titulo = models.CharField("titulo", max_length=60, null=False)

    def mis_fotos(self):
        return self.fotos.values_list('foto__url').all()


class Taller(models.Model):
    id_taller = models.AutoField(primary_key=True)
    fecha_inicio = models.DateField("fecha inicio")
    fecha_finalizacion = models.DateField("fecha finalizacion")
    precio = models.CharField("precio", max_length=7, null=False)
    profesor = models.CharField("profe", max_length=60, null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)


class HorarioTaller(models.Model):
    id_horario = models.AutoField(primary_key=True)
    DIAS_SEMANA = (
        ('Lun', 'Lunes'),
        ('Mar', 'Martes'),
        ('Mier', 'Miercoles'),
        ('Jue', 'Jueves'),
        ('Vie', 'Viernes'),
        ('Sab', 'Sabado'),
        ('Dom', 'Domingo')
    )
    dia_semana = models.CharField(max_length=4, choices=DIAS_SEMANA)
    hora_inicio = models.TimeField("fecha inicio")
    hora_finalizacion = models.TimeField("fecha finalizacion")
    taller = models.ForeignKey(Taller, on_delete=models.CASCADE)


class Evento(models.Model):
    id_evento = models.AutoField(primary_key=True)
    descripcion = models.TextField("descripcion")
    ubicacion = models.CharField("ubicacion", max_length=255, null=False)
    fecha_inicio = models.DateField("fecha inicio")
    fecha_finalizacion = models.DateField("fecha finalizacion")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)


class Noticia(models.Model):
    id_noticia = models.AutoField(primary_key=True)
    titulo = models.CharField("titulo", max_length=255, null=False)
    descripcion = models.TextField("descripcion")
    fecha = models.DateField("fecha")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)


class FotoAlbum(models.Model):
    id_imagen = models.AutoField(primary_key=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    foto = models.ImageField("Imagen", upload_to='fotos-album/', null=False)

    def get_album(self):
        return self.id_album


class Telefono(models.Model):
    id_telefono = models.AutoField(primary_key=True)
    telefono1 = models.CharField("Telefono 1", max_length=25)
    telefono2 = models.CharField("Telefono 2", max_length=25)
    perfil = models.ForeignKey(Profile, on_delete=models.CASCADE)
    cpc = models.ForeignKey(CpcCentro, on_delete=models.CASCADE)
    taller = models.ForeignKey(Taller, on_delete=models.CASCADE)
