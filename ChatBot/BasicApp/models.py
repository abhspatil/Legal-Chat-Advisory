from django.db import models

# Create your models here.

class Articles(models.Model):
    articleNum = models.IntegerField()
    statement = models.TextField() 
    
class ArticleDescription(models.Model):
    articleNum = models.ForeignKey(Articles, on_delete=models.CASCADE)
    #articleNum = models.IntegerField()
    description = models.TextField()
    
class References(models.Model):
    articleNum = models.ForeignKey(Articles,on_delete=models.CASCADE)
    #articleNum = models.IntegerField()
    links= models.TextField()

class Keywords(models.Model):
    articleNum = models.ForeignKey(Articles,on_delete=models.CASCADE)
    #articleNum = models.IntegerField()
    keyword = models.TextField()
    
    
class QueryData(models.Model):
    keywords = models.TextField()
    statement = models.TextField()
    description = models.TextField()
    links = models.TextField()
    
    
    
    
    
    
    
    