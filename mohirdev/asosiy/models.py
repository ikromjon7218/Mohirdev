from django.db import models

class Profil(models.Model):
    ism = models.CharField(max_length=30)
    username = models.CharField(max_length=60)
    sana = models.DateField(auto_now_add=True)
    email = models.CharField(max_length=40, blank=True)
    tel = models.CharField(max_length=20, blank=True)
    def __str__(self):
        return self.ism

class Ustoz(models.Model):
    ism = models.CharField(max_length=20)
    malumot = models.CharField(max_length=400)
    rasm = models.FileField(blank=True, null=True)
    def __str__(self):
        return self.ism

class Kurs(models.Model):
    nom = models.CharField(max_length= 20)
    rasm = models.FileField(blank=True, null=True)
    daraja = models.CharField(max_length=30, choices=[("Boshlang'ich", "boshlang'ich"), ("o'rta", "O'rta"), ("Yuqori", "yuqori")])
    narx = models.CharField(max_length=40)
    def __str__(self):
        return self.nom

class Ustoz_Kurs(models.Model):
    kurs_id = models.ForeignKey(Kurs, on_delete=models.CASCADE)
    ustoz_id = models.ForeignKey(Ustoz, on_delete=models.CASCADE)
    def __str__(self):
        return self.kurs_id.nom
class Tanlangan(models.Model):
    kurs_id = models.ForeignKey(Kurs, on_delete=models.CASCADE)
    profil_id = models.ForeignKey(Profil, on_delete=models.CASCADE)

class Xarid(models.Model):
    kurs_id = models.ForeignKey(Kurs, on_delete=models.CASCADE)
    profil_id = models.ForeignKey(Profil, on_delete=models.CASCADE)
    holat = models.CharField(max_length=20, default="Yangi")
    sana = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.kurs_id.nom

class Izoh(models.Model):
    baho = models.PositiveSmallIntegerField(default=5)
    sana = models.DateTimeField(blank=True, null=True)
    matn = models.CharField(max_length=90)
    profil_id = models.ForeignKey(Profil, on_delete=models.CASCADE)
    kurs_id = models.ForeignKey(Kurs, on_delete=models.CASCADE)
    def __str__(self):
        return self.profil_id.ism