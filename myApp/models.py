from django.db import models

# Create your models here.
class Agent(models.Model):
    agent_Name = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self) -> str:
        return str(self.id)
class Status(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
class Lead(models.Model):
    client_Name         = models.CharField(max_length=200)
    business_Type       = models.CharField(max_length=100)
    mobile_No           = models.CharField(max_length=10)
    email               = models.EmailField()
    address             = models.CharField(max_length=500)
    requirement         = models.TextField()
    department          = models.CharField(max_length=50)
    agent_id            = models.ForeignKey(Agent,on_delete=models.CASCADE)
    status              = models.ForeignKey(Status,on_delete=models.CASCADE,null=True)
    def __str__(self) -> str:
        return str(self.agent_id)