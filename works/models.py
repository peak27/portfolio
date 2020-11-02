from django.db import models

# Create your models here.

class Work(models.Model):

    CATEGORY = (
                ('EDA', 'EDA'),
                ('Text Analytics','Text Analytics'),
                ('Machine Learning','Machine Learning'),
                ('Deep Learning', 'Deep Learning'),
                ('Application Developnment', 'Application Developnment'),
                )

    # Images and Summary
    image = models.ImageField(upload_to = 'images/')
    title = models.CharField(max_length=100, null = True)
    summary = models.CharField(max_length=300)
    git = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length= 75, choices=CATEGORY)


    def __str__(self):
        return self.title

