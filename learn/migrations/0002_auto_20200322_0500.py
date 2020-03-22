# Generated by Django 2.2.4 on 2020-03-22 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='order',
        ),
        migrations.AddField(
            model_name='lecture',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='lecture',
            name='num',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='LectureImage',
        ),
    ]
