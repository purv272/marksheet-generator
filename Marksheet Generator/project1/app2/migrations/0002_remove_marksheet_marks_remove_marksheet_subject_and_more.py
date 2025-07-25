# Generated by Django 5.2.1 on 2025-06-19 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marksheet',
            name='marks',
        ),
        migrations.RemoveField(
            model_name='marksheet',
            name='subject',
        ),
        migrations.AddField(
            model_name='marksheet',
            name='aiml206_practical',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='marksheet',
            name='aiml206_theory',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='marksheet',
            name='aiml207_practical',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='marksheet',
            name='aiml207_theory',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='marksheet',
            name='aiml208_practical',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='marksheet',
            name='aiml208_theory',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='marksheet',
            name='aiml209_practical',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='marksheet',
            name='aiml209_theory',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='marksheet',
            name='aiml210_practical',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='marksheet',
            name='aiml210_theory',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='marksheet',
            name='aiml211_practical',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='marksheet',
            name='hs11103a_practical',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='marksheet',
            name='it284_practical',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
