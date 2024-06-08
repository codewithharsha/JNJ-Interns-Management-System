from django.db import models
from django.utils import timezone

class Registration(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    status = models.CharField(max_length=255, blank=True, null=True)
    last_login = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class CourseEnrollment(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=30)
    user_mobile = models.CharField(max_length=11)
    course_name = models.CharField(max_length=50)
    testimonial = models.CharField(max_length=200, null=True, blank=True)
    course_completion = models.CharField(max_length=1)
    testimonial_status = models.CharField(max_length=1, null=True, blank=True)

    class Meta:
        db_table = 'course_enrollments'

    def __str__(self):
        return f"{self.user.name} - {self.course_name}"
