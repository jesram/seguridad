from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Paciente(models.Model):
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    cuenta = models.CharField(max_length=100)
    fecha_nacimiento = models.DateTimeField()
    saldo = models.DecimalField(max_digits=12, decimal_places=2)

    def __unicode__(self):
        return self.nombres

    def get_absolute_url(self):
        return reverse('paciente_edit', kwargs={'pk': self.pk})
