from rest_framework import serializers
from .models import Question, QuestionBank


class GenerateQuestionsSerializer(
    serializers.Serializer
):
    subject = serializers.CharField()

    concepts = serializers.ListField(
        child=serializers.CharField(),
        required=False
    )

    instructions = serializers.CharField(
    required=False,
    allow_blank=True
    )

    difficulty = serializers.CharField()

    question_type = serializers.CharField()

    count = serializers.IntegerField()


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["id", "question_text","options", "answer"]


class QuestionBankSerializer(serializers.ModelSerializer):
    question_count = serializers.IntegerField()
    subject = serializers.SerializerMethodField()

    def get_subject(self, obj):
        question = obj.question_set.first()
        if question:
            return question.subject.name
        return ""

    class Meta:
        model = QuestionBank
        fields = [
            "id",
            "name",
            "tags",
            "subject",
            "created_at",
            "updated_at",
            "question_count",
        ]


class QuestionBankDetailSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(source="question_set", many=True)

    class Meta:
        model = QuestionBank
        fields = ["id", "name", "questions"]


class SaveQuestionBankSerializer(serializers.Serializer):
    subject = serializers.CharField()

    concepts = serializers.ListField(
        child=serializers.CharField(),
        required=False
    )

    questions = serializers.ListField()

    bank_name = serializers.CharField(
        required=False,
        allow_blank=True
    )


