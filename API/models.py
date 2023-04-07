from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserDetails(models.Model):
    national_id = models.CharField(primary_key=True, max_length=11)
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    email_address = models.EmailField(unique=True)

    def __str__(self):
        return self.national_id


class Question(models.Model):
    question_text = models.TextField()
    question_image = models.ImageField(upload_to='question_images/', null=True, blank=True)


class AnswerOption(models.Model):
    option_text = models.TextField()
    is_correct = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class ExamAttempt(models.Model):
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    score = models.IntegerField(default=0)
    date_test_taken = models.DateField()
    duration_minutes = models.IntegerField(default=7)
    num_questions = models.IntegerField(default=25)

class UserAnswer(models.Model):
    answer_option = models.ForeignKey(AnswerOption, on_delete=models.CASCADE)
    exam_attempt = models.ForeignKey(ExamAttempt, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

# Create your models here.
