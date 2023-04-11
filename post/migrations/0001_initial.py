# Generated by Django 3.2.15 on 2023-04-08 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_heading', models.CharField(max_length=200)),
                ('post_text', models.TextField()),
                ('post_author', models.CharField(default='anonymous', max_length=100)),
            ],
            options={
                'verbose_name': 'POST',
                'verbose_name_plural': 'POST',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post')),
            ],
            options={
                'verbose_name': 'Like',
                'verbose_name_plural': 'Like',
            },
        ),
    ]