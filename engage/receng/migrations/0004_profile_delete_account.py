# Generated by Django 4.0.4 on 2022-05-29 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receng', '0003_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.IntegerField()),
                ('comedy', models.IntegerField()),
                ('drama', models.IntegerField()),
                ('fantasy', models.IntegerField()),
                ('horror', models.IntegerField()),
                ('romance', models.IntegerField()),
                ('scifi', models.IntegerField()),
                ('thriller', models.IntegerField()),
                ('telugu', models.BooleanField()),
                ('hindi', models.BooleanField()),
                ('english', models.BooleanField()),
                ('to_watch', models.ManyToManyField(to='receng.movie')),
            ],
        ),
        migrations.DeleteModel(
            name='Account',
        ),
    ]
