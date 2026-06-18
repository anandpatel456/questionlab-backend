from django.contrib import admin
from .models import Difficulty, Question, QuestionBank, QuestionType, Subject, Concept

admin.site.register(Subject)
admin.site.register(Difficulty)
admin.site.register(QuestionType)
admin.site.register(QuestionBank)
admin.site.register(Question)
admin.site.register(Concept)
