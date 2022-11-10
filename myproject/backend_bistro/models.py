from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class MenuItems(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=600)
    price = models.FloatField(null = True)
    spicy_level = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE)
    cuisine_id = models.ForeignKey('Cuisine', on_delete=models.CASCADE)
    def __str__(self):
        return self.title + ' ||  Description: ' + self.description + ' ||  Price: ' + str(self.price) + ' ||  Spicy Level: ' + str(self.spicy_level) + ' ||  Category ID: ' + str(self.category_id) + ' ||  Cuisine ID: ' + str(self.cuisine_id)
    
    def json(self):
        return {
            'title' : self.title,
            'description' : self.description,
            'price' : self.price,
            'spicy_level' : self.spicy_level,
            'cuisine' : {
                'title' : self.cuisine_id.cuisine_title,
            },
            'category' : {
                'category' : self.category_id.category_title,
            }
        }

class Category(models.Model):
    id
    category_title = models.CharField(max_length=16)
    def __str__(self):
        return 'Category ID: ' + str(self.id) + ' || Category Title: ' + self.category_title


class Cuisine(models.Model):
    id 
    cuisine_title = models.CharField(max_length=16)
    def __str__(self):
        return 'Cuisine ID: ' + str(self.id) + ' || Cuisine Title: ' + self.cuisine_title

# class MenuJoined(models.Model):
    
