from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=75 , unique=True, verbose_name="Kursning nomi")
    description = models.TextField(blank=True, null=True, verbose_name="ursning tavsifi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Kurs yaratilgan vaqti")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Kurs oxirgi tahrirlangan vaqti")

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Talabaning FIO")
    email = models.EmailField(unique=True, verbose_name="Talabaning email manzili")
    enrolled_at = models.DateTimeField(auto_now_add=True, verbose_name="Ro‘yxatdan o‘tgan vaqti")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Course modeliga bog’lanadi")

    def __str__(self):
        return self.name

class Comment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Izoh qaysi kursga tegishli ekanligi")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Izohni qaysi talaba yozgani")
    comment_text = models.TextField(blank=True, null=True, verbose_name="Izohning matni")
    created_at =models.DateTimeField(auto_now_add=True, verbose_name="Izoh qoldirilgan vaqt")

    def __str__(self):
        return self.comment_text