# Generated by Django 3.1.4 on 2022-02-05 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0004_auto_20220205_0719'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='organisation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='leads.userprofile'),
            preserve_default=False,
        ),
    ]
