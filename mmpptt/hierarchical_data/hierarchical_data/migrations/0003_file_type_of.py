# Generated by Django 2.2.5 on 2019-10-04 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hierarchical_data', '0002_auto_20191003_0038'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='type_of',
            field=models.CharField(choices=[('folder', 'FOLDER'), ('file', 'FILE')], default='file', max_length=6),
        ),
    ]