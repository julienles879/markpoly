from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Mark(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)   

    def __str__(self):
        return f"{self.name} ({self.topic.name})"

class Question(models.Model): 
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    answer = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text} ({self.mark.name})"