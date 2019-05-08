# Generated by Django 2.2 on 2019-05-08 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190508_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='ingredients',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='foods', to='api.Ingredient'),
        ),
    ]
