from django.db import models


class RealtorForm(models.Model):
    user_name = models.CharField('Имя', max_length=50)
    user_phone = models.CharField('Телефон', max_length=10)
    user_mail = models.EmailField('E-mail', max_length=40)
    user_comment = models.TextField('Сообщение')

    def __str__(self):
        return self.user_name


    class Meta:
        verbose_name = 'Заявка клиента'
        verbose_name_plural = 'Заявки клиентов'