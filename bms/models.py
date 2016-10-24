from django.db import models

# Create your models here.


class Salesperson(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
    
class Clients(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name


class Orders(models.Model):
    # Order is the core of the bms. And the value of bms is to follow the Orders.
    # each order is the result of Salesperson & Clients
    id = models.AutoField(primary_key=True)
    
    name = models.CharField(max_length=20)

    money = models.IntegerField()
    # the total amount of a order in fact. 
    # this amount can be different values according to STATUS_CHOICES
    
    date = models.DateField()
    
    STATUS_CHOICES = (
        ('BS', 'Before Set up a project'),
        ('BID', 'During Bid Process'),
        ('IM', 'Implement After Bid'),
        ('DONE', 'Get all Money Back'),
        )
    stutas = models.CharField(max_length=20, choices = STATUS_CHOICES)
    # stutas is a very important value to describe a order.
    
    under_the_hands_of = models.ForeignKey(
        Salesperson,
        on_delete=models.CASCADE,
    )
    # to tell who or which Salesperson should be on the charge.
    
    from_the_customer = models.ForeignKey(
        Clients,
        on_delete=models.CASCADE,
    )
    
