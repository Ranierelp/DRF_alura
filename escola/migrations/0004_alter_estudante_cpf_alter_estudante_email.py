# Generated by Django 5.1 on 2024-08-22 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0003_matricula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudante',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
        migrations.AlterField(
            model_name='estudante',
            name='email',
            field=models.EmailField(max_length=30),
        ),
    ]
