# Generated by Django 4.1.7 on 2023-04-03 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tercera_pre_entrega', '0003_notas_usuario_delete_borrado_delete_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='usuario',
            field=models.TextField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fecha_nacimiento',
            field=models.DateField(auto_now_add=True),
        ),
    ]
