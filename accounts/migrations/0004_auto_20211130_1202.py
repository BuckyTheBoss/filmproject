# Generated by Django 3.2.9 on 2021-11-30 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20211130_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='skills',
            field=models.ManyToManyField(to='accounts.Skill'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='facebook',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='instagram',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='twitter',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='website',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
