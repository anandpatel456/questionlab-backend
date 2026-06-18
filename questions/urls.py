from django.urls import path

from .views import (
    DashboardStatsView,
    DeleteQuestionBankView,
    GenerateQuestionsView,
    MasterDataView,
    QuestionBankDetailView,
    QuestionBankListView,
    SaveQuestionBankView,
    ConceptListView,
    ExportQuestionBankView,
    UpdateQuestionView,
    UpdateQuestionBankView,
    ActivityListView,
)

urlpatterns = [
    path("master-data/", MasterDataView.as_view()),
    path("generate-questions/", GenerateQuestionsView.as_view()),
    path("save-question-bank/", SaveQuestionBankView.as_view()),
    path("question-banks/", QuestionBankListView.as_view()),
    path("question-banks/<int:pk>/", QuestionBankDetailView.as_view()),
    path("question-banks/<int:pk>/export/", ExportQuestionBankView.as_view()), 
    path("concepts/", ConceptListView.as_view()),
    path("delete-question-bank/<int:bank_pk>/", DeleteQuestionBankView.as_view()),
    path("question-banks/<int:pk>/update/", UpdateQuestionBankView.as_view()),
    path("questions/<int:question_id>/update/", UpdateQuestionView.as_view()),
    path("dashboard-stats/", DashboardStatsView.as_view()),
    path("activities/", ActivityListView.as_view()),
]