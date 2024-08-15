from django.db import models

# Create your models here.

class User(models.Model):
    STUDENT='student'
    TEACHER='teacher'
    ROLES = (
        (STUDENT, 'talaba'),
        (TEACHER,"o'qituvchi")
    )
    role=models.CharField(max_length=200,choices=ROLES)
    full_name=models.CharField(max_length=200,blank=False)

    def __str__(self):
        return self.full_name

class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    count=models.IntegerField()

    def __str__(self):
        return self.title

class BookRecord(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    took_on=models.DateTimeField(auto_now_add=True)
    returned_date=models.DateField()

    def __str__(self):
        return self.user.full_name






