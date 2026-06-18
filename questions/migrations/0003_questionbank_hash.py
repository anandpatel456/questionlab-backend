from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("questions", "0002_concept"),
    ]

    operations = [
        migrations.AddField(
            model_name="questionbank",
            name="hash",
            field=models.CharField(max_length=64, unique=True, null=True, blank=True),
        ),
    ]
