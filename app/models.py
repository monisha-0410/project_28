from django.db import models

# Create your models here.
class Topic(models.Model):
    Topic_name=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.Topic_name
    

class WebPage(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
    Topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    url=models.URLField()
    Email=models.EmailField()
    Recreateemail=models.EmailField(default='india@gmail.com')

    def __str__(self):
        return self.name 
    

class AccessRecord(models.Model):
    name=models.ForeignKey(WebPage,on_delete=models.CASCADE)
    date=models.DateField()
    Author=models.CharField(max_length=100)

    def __str__(self):
        return self.Author