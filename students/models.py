from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    classtype = models.CharField(max_length=20)
    discord = models.CharField(max_length=50)
    classday = models.CharField(max_length=50)
    parent = models.CharField(max_length=20)
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    profile = models.CharField(max_length=100, null=True, blank=True)
    schedule = models.CharField(max_length=100, null=True)
    additional_info = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class LessonTopic(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='topics')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Homework(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="homeworks")
    description = models.TextField()

    def __str__(self):
        return self.description