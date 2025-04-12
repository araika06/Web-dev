from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import CompanySerializer, VacancySerializer
from api.models import Company, Vacancy
from rest_framework import status

class CompanyAPIView(APIView):
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data) 
    
    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class CompanyDetailAPIView(APIView):
    def get_object(self, id):
        try:
            return Company.objects.get(id=id)
        except Company.DoesNotExist:
            return Response({'error': 'Company not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def get(self, request, id):
        company = self.get_object(id)
        serializer = CompanySerializer(company)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        company = self.get_object(id)
        serializer = CompanySerializer(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        company = self.get_object(id)
        company.delete()
        return Response({'message': 'Company deleted'})

class CompanyVacanciesAPIView(APIView):
    def get_object(self, id):
        try:
            return Company.objects.get(id=id)
        except Company.DoesNotExist:
            return Response({'error': 'Company not found'}, status=status.HTTP_404_NOT_FOUND) 

    def get(self, request, id):
        company = self.get_object(id)
        vacancies = Vacancy.objects.filter(company=company)
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)   
    
class VacancyAPIView(APIView):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VacancyDetailAPIView(APIView):
    def get_object(self, id):
        try:
            return Vacancy.objects.get(id=id)
        except Vacancy.DoesNotExist:
            return Response({'error':'Vacancy not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, id):
            vacancy = self.get_object(id)
            serializer = VacancySerializer(vacancy)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        vacancy = self.get_object(id)
        serializer = VacancySerializer(instance=vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        vacancy = self.get_object(id)
        vacancy.delete()
        return Response({'message': 'Vacancy deleted'})

class TopTenAPIView(APIView):
    def get(self, request):
         vacancies = Vacancy.objects.order_by('salary')[:10]
         serializer = VacancySerializer(vacancies, many=True)
         return Response(serializer.data, status=status.HTTP_200_OK)

