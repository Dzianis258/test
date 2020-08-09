from django.db import models


class Course(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    description = models.TextField()
    img = models.ImageField(default='default.png', upload_to='course_images')

    def __str__(self):
        return self.title
