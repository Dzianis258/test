from django.db import models
from django.urls import reverse


class Course(models.Model):
    slug = models.SlugField(verbose_name='Название URL')
    title = models.CharField(verbose_name='Название курса', max_length=120)
    description = models.TextField(verbose_name='Описание курса')
    img = models.ImageField(verbose_name='Изображение профиля', default='default.png', upload_to='course_images')
    free = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course-detail', kwargs={'slug': self.slug})


class Lesson(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    number = models.IntegerField()
    video_url = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('lesson-detail', kwargs={'slug': self.course.slug, 'lesson_slug': self.slug})

