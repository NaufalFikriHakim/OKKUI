from django.db import models

# Create your models here.
class Acara(models.Model):
    nama = models.CharField(max_length=255)
    tanggal = models.DateField()
    tempat = models.TextField()

class Sponsor(models.Model):
    nama = models.CharField(max_length=255)
    acara = models.ForeignKey(Acara, on_delete=models.CASCADE)
    tipe = models.CharField(max_length=255)
    harga = models.IntegerField()
    benefit = models.TextField()

class Pembicara(models.Model):
    nama = models.CharField(max_length=255)
    acara = models.ForeignKey(Acara, on_delete=models.CASCADE)

class PengurusInti(models.Model):
    nama = models.CharField(max_length=255)
    jabatan = models.CharField(max_length=255)

class Divisi(models.Model):
    nama = models.CharField(max_length=255)

class Rapat(models.Model):
    divisi = models.ForeignKey(Divisi, on_delete=models.CASCADE)
    kehadiran = models.TextField()
    waktu = models.DateField()
    tempat = models.CharField(max_length=255)
    kesimpulan = models.TextField()

class BPH(models.Model):
    divisi = models.ForeignKey(Divisi, on_delete=models.CASCADE)
    nama = models.CharField(max_length=255)
    jabatan = models.CharField(max_length=255)

class Kelompok(models.Model):
    nomor = models.IntegerField(primary_key=True)

class Mentor(models.Model):
    nama = models.CharField(max_length=255)
    angkatan = models.IntegerField()
    jurusan = models.CharField(max_length=255)
    kelompok = models.ForeignKey(Kelompok, on_delete=models.CASCADE)

class Mentee(models.Model):
    nama = models.CharField(max_length=255)
    jurusan = models.CharField(max_length=255)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    kelompok = models.ForeignKey(Kelompok, on_delete=models.CASCADE)

class Mentoring(models.Model):
    kelompok = models.ForeignKey(Kelompok, on_delete=models.CASCADE)
    presensi = models.TextField()
    materi = models.CharField(max_length=255)