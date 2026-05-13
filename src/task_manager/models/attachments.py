from django.db import models


from config.models import BaseModel




class Attachments(BaseModel):
    name = models.CharField(
        max_length=64,
        unique=True,
        verbose_name="Наименование"
    )

    task = models.ForeignKey(
        to='Tasks',
        related_name='attachments',
        on_delete=models.CASCADE,
    )
    file = models.FileField(
        upload_to='attachments_file',
        null=True, blank=True,
        verbose_name='Файлы'
    )
    photo = models.ImageField(
        upload_to='attachments_photo',
        null=True,
        blank=True,
        verbose_name='Фото'
    )



    class Meta:
        ordering = ['name']
        db_table = 'attachments'
        verbose_name = 'Вложение'
        verbose_name_plural = 'Вложения'

    def __str__(self):
        return self.name
