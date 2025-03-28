from django.db import models

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

class Lesson(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="lessons")
    date = models.DateField()  # data lekcji
    topic = models.CharField(max_length=255)
    homework = models.TextField(blank=True)
    is_settled = models.BooleanField(default=False)
    homework_done = models.BooleanField(default=False)
    homework_sent = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.date} - {self.topic}"

class Homework(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="homeworks")
    description = models.TextField()

    def __str__(self):
        return self.description