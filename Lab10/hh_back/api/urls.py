from django.urls import path
from .views.cbv import  CompanyAPIView, CompanyDetailAPIView, CompanyVacanciesAPIView
from .views.fbv import vacancies, vacancy_detail, top_ten_vacancies
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('companies/', CompanyAPIView.as_view()),
    path('companies/<int:id>/', CompanyDetailAPIView.as_view()),
    path('companies/<int:id>/vacancies/', CompanyVacanciesAPIView.as_view()),
    path('vacancies/', vacancies),
    path('vacancies/<int:id>/', vacancy_detail),
    path('vacancies/top_ten/', top_ten_vacancies)
]