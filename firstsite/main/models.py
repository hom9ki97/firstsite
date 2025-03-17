from django.db import models
from django.contrib.auth.models import AbstractUser


class AdvUser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name='Прошел активацию?')
    send_messages = models.BooleanField(default=True, verbose_name='Слать оповещение о новых комментариях?')

    class Meta(AbstractUser.Meta):
        pass


class Lessons(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='Название')
    order = models.SmallIntegerField(default=1, db_index=True, verbose_name='№ урока')
    content = models.TextField()
    topic = models.ForeignKey('Topic', on_delete=models.PROTECT, null=True, blank=True,
                              verbose_name='Тема занятий', related_name='lessons')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тема урока'
        verbose_name_plural = 'Темы уроков'


class Topic(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Тема урока')
    description = models.TextField()
    language = models.ForeignKey('Language', on_delete=models.PROTECT, null=True, blank=True,
                                 verbose_name='Язык программирования', related_name='topic')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Темы занятий'
        verbose_name = 'Тема занятия'
        ordering = ('name',)


class HomeWork(models.Model):
    lesson = models.ForeignKey('Lessons', on_delete=models.PROTECT, related_name='homeworks')
    task = models.TextField()
    order = models.SmallIntegerField(default=1, db_index=True, verbose_name='№ ДЗ')

    def __str__(self):
        return f"Домашнее задание к {self.lesson.title}"

    def get_topic(self):
        return self.lesson.topic

    class Meta:
        verbose_name = 'Домашнее задание'
        verbose_name_plural = 'Домашнии занятия'


class CodeExample(models.Model):
    lesson = models.ForeignKey('Lessons', on_delete=models.PROTECT, related_name='code_examples',
                               verbose_name='Код урока', null=True, blank=True)
    homework = models.ForeignKey('Homework', on_delete=models.PROTECT, related_name='code_examples',
                                 verbose_name='Код ДЗ', null=True, blank=True)
    title = models.CharField(max_length=100, default='Пример кода', verbose_name='Название примера')
    code_file = models.FileField(upload_to='code_examples/', verbose_name='Файл с кодом')
    description = models.TextField(blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пример кода'
        verbose_name_plural = 'Примеры кода'


class Language(models.Model):
    language = models.CharField(max_length=50, db_index=True, verbose_name='Язык программирования')

    def __str__(self):
        return self.language

    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'
