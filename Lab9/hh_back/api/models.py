from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()
    city = models.CharField()
    address = models.TextField()

    def __str__(self):
        return f'{self.name} {self.description} {self.city} {self.address}'
    
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }
        

class Vacancy(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()
    salary = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE,
                                 related_name='vacancies')   

    def __str__(self):
        return f'{self.name} {self.description} {self.salary} {self.company}'
    
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
            'company': self.company
        }