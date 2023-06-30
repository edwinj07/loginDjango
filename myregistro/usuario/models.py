from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Persona(models.Model):
    cc=models.BigIntegerField(primary_key=True,serialize=False)
    nombres=models.CharField(max_length=100)
    apellidos=models.CharField(max_length=100)
    foto=models.ImageField(upload_to='fotoper/',verbose_name='foto Perfil',null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def str(self):
        fila='cc'+self.cc+'nombres'+self.nombres+'apellidos'+self.apellidos+'foto'+self.foto + '-by' +self.user.username
        return fila
    def delete(self,using=None,keep_parent=False):
        self.foto.storage.delete(self.foto.name)
        super().delete()

