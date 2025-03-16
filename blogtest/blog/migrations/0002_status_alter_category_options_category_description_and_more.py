# Generated by Django 5.1.5 on 2025-03-03 16:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Status",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name="category",
            options={"ordering": ["name"], "verbose_name_plural": "Categories"},
        ),
        migrations.AddField(
            model_name="category",
            name="description",
            field=models.TextField(default="No description provided"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("published", models.DateTimeField(auto_now_add=True, null=True)),
                ("title", models.CharField(max_length=255)),
                ("content", models.TextField()),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "categories",
                    models.ManyToManyField(related_name="posts", to="blog.category"),
                ),
                (
                    "status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="blog.status"
                    ),
                ),
            ],
            options={
                "ordering": ["-published"],
            },
        ),
    ]
