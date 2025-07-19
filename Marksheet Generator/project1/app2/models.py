from django.db import models

# Create your models here.

class Marksheet(models.Model):
    student_id = models.CharField(max_length=20)
    student_name = models.CharField(max_length=100)
    institute = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    semester = models.CharField(max_length=20)
    exam = models.CharField(max_length=50)

    aiml206_theory = models.CharField(max_length=5, blank=True, null=True)
    aiml206_practical = models.CharField(max_length=5, blank=True, null=True)

    aiml207_theory = models.CharField(max_length=5, blank=True, null=True)
    aiml207_practical = models.CharField(max_length=5, blank=True, null=True)

    aiml208_theory = models.CharField(max_length=5, blank=True, null=True)
    aiml208_practical = models.CharField(max_length=5, blank=True, null=True)

    aiml209_theory = models.CharField(max_length=5, blank=True, null=True)
    aiml209_practical = models.CharField(max_length=5, blank=True, null=True)

    aiml210_theory = models.CharField(max_length=5, blank=True, null=True)
    aiml210_practical = models.CharField(max_length=5, blank=True, null=True)

    aiml211_practical = models.CharField(max_length=5, blank=True, null=True)

    hs11103a_practical = models.CharField(max_length=5, blank=True, null=True)

    it284_practical = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return f"{self.student_name} - {self.degree} - Semester {self.semester}"
