# Generated by Django 4.2.4 on 2023-08-29 07:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_photo', models.ImageField(blank=True, null=True, upload_to='image_user/', verbose_name=' фото геймера')),
                ('site', models.URLField(blank=True, max_length=255, null=True, verbose_name='веб-сайт')),
                ('vk', models.URLField(blank=True, max_length=255, null=True, verbose_name='аккаунт VK')),
                ('ratingUser', models.SmallIntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='геймер')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('BS', 'Кузнецы'), ('DD', 'ДД'), ('QG', 'Квестгиверы'), ('GM', 'Гилдмастеры'), ('DR', 'Торговцы'), ('LW', 'Кожевники'), ('Tn', 'Танки'), ('Hl', 'Хилы'), ('SM', 'Мастера заклинаний'), ('PM', 'Зельевары')], max_length=64, verbose_name='категория')),
                ('dataCreation', models.DateTimeField(auto_now_add=True, verbose_name='создан')),
                ('dataUpdate', models.DateTimeField(auto_now=True, verbose_name='редактировано')),
                ('title', models.CharField(max_length=128, verbose_name='название')),
                ('content', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='image_photo/', verbose_name='фото')),
                ('video', models.FileField(blank=True, null=True, upload_to='video/', verbose_name='видео')),
                ('file', models.FileField(blank=True, null=True, upload_to='file/', verbose_name='другое')),
                ('rating', models.SmallIntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fanboard.profile', verbose_name='геймер')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='текст комментария')),
                ('dataCreation', models.DateTimeField(auto_now_add=True, verbose_name='создан')),
                ('rating', models.SmallIntegerField(default=0)),
                ('approved_comment', models.BooleanField(blank=True, default=False, verbose_name='Комментарий одобрен')),
                ('commentPost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fanboard.post')),
                ('commentUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='автор комментария')),
            ],
        ),
    ]
