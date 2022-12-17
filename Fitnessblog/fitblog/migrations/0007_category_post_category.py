# Generated by Django 4.1.1 on 2022-12-16 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitblog', '0006_post_created_on'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='Other', max_length=255),
        ),
    ]
