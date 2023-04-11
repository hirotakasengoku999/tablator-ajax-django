from django.db import models


class Post(models.Model):
    class Meta:
        verbose_name = ('POST')
        verbose_name_plural = ("POST")

    post_heading = models.CharField(max_length=200)
    post_text = models.TextField()
    post_author = models.CharField(max_length=100, default='anonymous')

    def __str__(self):
        return self.post_heading


class Like(models.Model):
    class Meta:
        verbose_name = ('Like')
        verbose_name_plural = ("Like")

    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class RESULT(models.Model):
    CHOICES = [
        ('未','未'),
        ('算定可', '算定可'),
        ('算定不可', '算定不可'),
    ]
    USER_CHECK = models.CharField(max_length=4, choices=CHOICES)
    PATIENT_ID = models.CharField(max_length=10)
    PATIENT_NAME = models.CharField(max_length=100)
    MEDICALCARE_DATE = models.CharField(max_length=10)
    DEPT = models.CharField(max_length=10)
    ITEM_NAME = models.CharField(max_length=100)
    PREDICT_PROBA = models.DecimalField(max_digits=4, decimal_places=1)
    CALCULATION_BOOL = models.BooleanField()
    BASIS_1 = models.CharField(max_length=100, null=True, blank=True)
    BASIS_2 = models.CharField(max_length=100, null=True, blank=True)
    BASIS_3 = models.CharField(max_length=100, null=True, blank=True)
    BASIS_4 = models.CharField(max_length=100, null=True, blank=True)
    BASIS_5 = models.CharField(max_length=100, null=True, blank=True)
    NOTE = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.PATIENT_ID
