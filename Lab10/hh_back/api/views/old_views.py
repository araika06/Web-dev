import json
from django.shortcuts import render
from django.http import JsonResponse
from api.serializers import CompanySerializer, VacancySerializer
from api.models import Company, Vacancy
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def companies(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return JsonResponse(serializer.data, safe=False) 

    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = CompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt 
def company_detail(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist:
        return JsonResponse({'error': 'Company not found'}, status=404)
    
    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return JsonResponse(serializer.data, status=200)
    
    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = CompanySerializer(instance=company, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse({'message': 'Company deleted'})
    
@csrf_exempt 
def company_vacancies(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist:
        return JsonResponse({'error': 'Company not found'}, status=404)
    
    vacancies = Vacancy.objects.filter(company=company)
    serializer = VacancySerializer(vacancies, many=True)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt 
def vacancies(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = VacancySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt 
def vacancy_detail(request, id):
    try:
        vacancy = Vacancy.objects.get(id=id)
    except Vacancy.DoesNotExist:
        return JsonResponse({'error':'Vacancy not found'}, status=404)
    
    if request.method == 'GET':
        serializer = VacancySerializer(vacancy)
        return JsonResponse(serializer.data, status=200)
    
    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = VacancySerializer(instance=vacancy, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        vacancy.delete()
        return JsonResponse({'message': 'Vacancy deleted'})

@csrf_exempt
def top_ten_vacancies(request):
    vacancies = Vacancy.objects.order_by('-salary')[:10]
    serializer = VacancySerializer(vacancies, many=True)
    return JsonResponse(serializer.data, safe=False)