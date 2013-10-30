# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Administrador(models.Model):
    id_administrador = models.DecimalField(decimal_places=0, primary_key=True, db_column='ID_ADMINISTRADOR', max_digits=9) # Field name made lowercase.
    id_grupo = models.ForeignKey(GrupoInvestigacion, db_column='ID_GRUPO') # Field name made lowercase.
    nombre = models.CharField(max_length=300, db_column='NOMBRE') # Field name made lowercase.
    class Meta:
        db_table = u'administrador'

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=240, unique=True)
    class Meta:
        db_table = u'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = u'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    content_type = models.ForeignKey(DjangoContentType)
    codename = models.CharField(max_length=300, unique=True)
    class Meta:
        db_table = u'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=90, unique=True)
    first_name = models.CharField(max_length=90)
    last_name = models.CharField(max_length=90)
    email = models.CharField(max_length=225)
    password = models.CharField(max_length=384)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    is_superuser = models.IntegerField()
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = u'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        db_table = u'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = u'auth_user_user_permissions'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey(DjangoContentType, null=True, blank=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=600)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    class Meta:
        db_table = u'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)
    app_label = models.CharField(max_length=300, unique=True)
    model = models.CharField(max_length=300, unique=True)
    class Meta:
        db_table = u'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=120, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = u'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=300)
    name = models.CharField(max_length=150)
    class Meta:
        db_table = u'django_site'

class GrupoInvestigacion(models.Model):
    id_grupo = models.DecimalField(decimal_places=0, primary_key=True, db_column='ID_GRUPO', max_digits=9) # Field name made lowercase.
    nombre_grupo = models.CharField(max_length=75, db_column='NOMBRE_GRUPO') # Field name made lowercase.
    registro_colciencias = models.CharField(max_length=60, db_column='REGISTRO_COLCIENCIAS') # Field name made lowercase.
    ranking = models.DecimalField(decimal_places=0, null=True, max_digits=21, db_column='RANKING', blank=True) # Field name made lowercase.
    fecha_fundado = models.DateField(db_column='FECHA_FUNDADO') # Field name made lowercase.
    class Meta:
        db_table = u'grupo_investigacion'

class Integrante(models.Model):
    id_integrante = models.DecimalField(decimal_places=0, primary_key=True, db_column='ID_INTEGRANTE', max_digits=9) # Field name made lowercase.
    id_semillero = models.ForeignKey(Semillero, db_column='ID_SEMILLERO') # Field name made lowercase.
    id_grupo = models.ForeignKey(GrupoInvestigacion, db_column='ID_GRUPO') # Field name made lowercase.
    nombreintegrante = models.CharField(max_length=60, db_column='NOMBREINTEGRANTE') # Field name made lowercase.
    descripcion = models.CharField(max_length=600, db_column='DESCRIPCION') # Field name made lowercase.
    fecha_ingreso = models.DateField(db_column='FECHA_INGRESO') # Field name made lowercase.
    fecha_salida = models.DateField(db_column='FECHA_SALIDA') # Field name made lowercase.
    cvlac = models.CharField(max_length=60, db_column='CVLAC', blank=True) # Field name made lowercase.
    tipo_integrante = models.CharField(max_length=60, db_column='TIPO_INTEGRANTE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'integrante'

class Proyectos(models.Model):
    id_proyecto = models.DecimalField(decimal_places=0, primary_key=True, db_column='ID_PROYECTO', max_digits=9) # Field name made lowercase.
    pro_id_proyecto = models.ForeignKey('self', null=True, db_column='PRO_ID_PROYECTO', blank=True) # Field name made lowercase.
    id_integrante = models.ForeignKey(Integrante, db_column='ID_INTEGRANTE') # Field name made lowercase.
    nombre_proyecto = models.CharField(max_length=90, db_column='NOMBRE_PROYECTO', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'proyectos'

class Semillero(models.Model):
    id_semillero = models.DecimalField(decimal_places=0, primary_key=True, db_column='ID_SEMILLERO', max_digits=2) # Field name made lowercase.
    id_grupo = models.ForeignKey(GrupoInvestigacion, db_column='ID_GRUPO') # Field name made lowercase.
    descripcion_semillero = models.CharField(max_length=600, db_column='DESCRIPCION_SEMILLERO') # Field name made lowercase.
    nombre_semillero = models.CharField(max_length=75, db_column='NOMBRE_SEMILLERO') # Field name made lowercase.
    class Meta:
        db_table = u'semillero'

