# Generated by Django 4.0.4 on 2022-04-19 01:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('support', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='contents',
        ),
        migrations.AddField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자'),
        ),
        migrations.AddField(
            model_name='answer',
            name='category',
            field=models.CharField(choices=[('general', '일반'), ('account', '계정'), ('etc', '기타')], max_length=20, null=True, verbose_name='카테고리'),
        ),
        migrations.AddField(
            model_name='answer',
            name='content',
            field=models.TextField(null=True, verbose_name='내용'),
        ),
        migrations.AddField(
            model_name='answer',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='최종수정일'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='create_date',
            field=models.DateTimeField(auto_now=True, verbose_name='작성일'),
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('general', '일반'), ('account', '계정'), ('etc', '기타')], max_length=20, null=True, verbose_name='카테고리')),
                ('subject', models.CharField(default='', max_length=200, null=True, verbose_name='제목')),
                ('content', models.TextField(verbose_name='내용')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='최종수정일')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='support.faq'),
        ),
        migrations.DeleteModel(
            name='Ask',
        ),
    ]
