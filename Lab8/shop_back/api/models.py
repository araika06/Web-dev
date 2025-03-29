from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.id} {self.name}"
    
    def to_json(self):
        return {
            "id": self.id,
            "name": self.name
        }

class Product(models.Model):
    name = models.CharField(max_length=500)
    price = models.FloatField()
    description = models.TextField()
    count = models.IntegerField()
    is_active =  models.BooleanField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} {self.name} {self.price} {self.description} {self.count} {self.is_active} {self.category}"
    
    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "count": self.count,
            "is_active": self.is_active,
            "category": self.category.name
        }