# Generated by Django 4.2 on 2023-10-02 20:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("shortener", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="shorturl",
            options={
                "ordering": ["-created"],
                "verbose_name": "shorturl",
                "verbose_name_plural": "shorturls",
            },
        ),
    ]