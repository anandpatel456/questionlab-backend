from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Difficulty(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class QuestionType(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class QuestionBank(models.Model):
    name = models.CharField(max_length=255)

    hash = models.CharField(
        max_length=64,
        unique=True,
        null=True,
        blank=True
    )
    tags = models.CharField(
        max_length=500,
        blank=True,
        default=""
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )
    export_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name



class Question(models.Model):
    question_text = models.TextField()
    answer = models.TextField()
    options = models.JSONField(default=list)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    question_bank = models.ForeignKey(QuestionBank, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text[:50]
    
class Concept(models.Model):
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="concepts"
    )

    name = models.CharField(
        max_length=255
    )

    def __str__(self):
        return self.name


class Activity(models.Model):
    ACTION_TYPES = [
        ("generate", "Generated Questions"),
        ("bank", "Created Question Bank"),
        ("export", "Exported"),
        ("delete", "Deleted Question Bank"),
        ("edit", "Edited Question Bank"),
    ]

    action_type = models.CharField(max_length=20, choices=ACTION_TYPES)
    description = models.CharField(max_length=255)
    subject = models.CharField(max_length=255, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.action_type} - {self.description}"