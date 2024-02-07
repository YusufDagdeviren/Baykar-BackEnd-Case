from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


# Marka, Model, Ağırlık, Kategori vb.
class Iha(models.Model):
    KATEGORI_CHOICES = [
        ('sivil', 'Sivil İHA'),
        ('askeri', 'Askeri İHA'),
        ('hibrit', 'Hibrit İHA'),
        ('mini_iha', 'Mini İHA'),
        ('uzun_menzilli', 'Uzun Menzilli İHA'),
    ]
    marka = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    agirlik = models.FloatField()
    kategori = models.CharField(max_length=20, choices=KATEGORI_CHOICES)
# İHA, Tarih ve Saat Aralıkları, Kiralayan Üye vb.
class Kullanici(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    groups = models.ManyToManyField(Group, related_name='customuser_groups')
    user_permissions = models.ManyToManyField(
        Permission, related_name='customuser_user_permissions'
    )
    """
    def save(self, *args, **kwargs):
        if not self.id:
            self.password = make_password(self.password, gensalt())
        super(CustomUser, self).save(*args, **kwargs)    
    """
class Kiralama(models.Model):
    iha = models.ForeignKey(Iha, on_delete=models.CASCADE)
    kiralayan_uye = models.ForeignKey(Kullanici, on_delete=models.CASCADE)
    baslangic_tarihi = models.DateField()
    bitis_tarihi = models.DateField()
    baslangic_saat = models.TimeField()
    bitis_saat = models.TimeField()

class KullaniciDetay(models.Model):
    user = models.OneToOneField(Kullanici, on_delete=models.CASCADE)
    ihalar = models.ManyToManyField('Iha', related_name='kiralanan_ihalar', blank=True)
