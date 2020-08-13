from django.db import models
from django.contrib.auth.models import User
from PIL import Image


gender = [
    ('мужской', 'мужской'),
    ('женский', 'женский')
]

TYPE_CHOICES = (
    ('Полный пакет', 'full'),
    ('Бесплатный пакет', 'free')
)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField('Фото пользователя', default='default.png', upload_to='user_images')
    account_type = models.CharField(choices=TYPE_CHOICES, default='Бесплатный пакет', max_length=30)

    gender = models.CharField(default='мужской', verbose_name='Пол',
                              choices=gender, max_length=10)

    get_notifications = models.BooleanField(verbose_name='Получать уведомления', default=False)

    def __str__(self):
        return f'Профайл пользователя {self.user.username}'

    class Meta:
        verbose_name = 'Профайл'
        verbose_name_plural = 'Профайлы'

    def save(self, *args, **kwargs):
        super().save()
        image = Image.open(self.img.path)
        if image.height > 256 or image.width > 256:
            resize = (256, 256)
            image.thumbnail(resize)
            image.save(self.img.path)