# Generated by Django 2.2.4 on 2020-03-21 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='num',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='closedate',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='opendate',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='professor',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='semester',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='note',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='order',
            field=models.IntegerField(default=99),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lectureimage',
            name='order',
            field=models.IntegerField(default=99),
        ),
        migrations.AlterField(
            model_name='weeklyclass',
            name='num',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='weeklyclass',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
