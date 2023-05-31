from django.db import models


class Type(models.Model):
    title = models.CharField(max_length='48', verbose_name='Название')

    def __str__(self):
        return self.title


class Tasks(models.Model):
    condition = models.CharField(max_length=2000, verbose_name='Условие')
    answer = models.IntegerField(verbose_name='Ответ')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='tasks', verbose_name='Тип')

    def __str__(self):
        return self.id
