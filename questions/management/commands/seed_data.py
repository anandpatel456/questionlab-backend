from django.core.management.base import BaseCommand
from questions.models import Subject, Difficulty, QuestionType

class Command(BaseCommand):
    help = 'Seed initial data'

    def handle(self, *args, **kwargs):
        subjects = ["Mathematics", "Physics", "Chemistry", "Biology", "Computer Science", "Agentic AI"]
        for s in subjects:
            Subject.objects.get_or_create(name=s)

        difficulties = ["Easy", "Medium", "Hard"]
        for d in difficulties:
            Difficulty.objects.get_or_create(name=d)

        types = [
            {"name": "Multiple Choice", "value": "mcq"},
            {"name": "Short Answer", "value": "short"},
            {"name": "Long Answer", "value": "long"},
            {"name": "True/False", "value": "truefalse"},
        ]
        for t in types:
            QuestionType.objects.get_or_create(value=t["value"], defaults={"name": t["name"]})

        self.stdout.write(self.style.SUCCESS('Data seeded successfully!'))