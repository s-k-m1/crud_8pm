from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    age = models.PositiveIntegerField()
        
    GENDER_CHOICES = [
    ("male", "Male"),
    ("female", "Female"),
    ("other", "Others")  
    ]
    
    SUBJECT_CHOICES = [
        ("java", "Java"),
        ("python", "Python"),
        ("mern", "Mern"),
        ("react", "React"),        
    ]

    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default="male")
    subjects = models.CharField(max_length=20, choices=SUBJECT_CHOICES)
    bio = models.TextField()
    
    class Meta:
        db_table = 'student'
    
    