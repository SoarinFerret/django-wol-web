from django.db import models

# Create your models here.

# Computers
class Computer(models.Model):
    computer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    mac_addr = models.CharField(max_length=40)
    ip_addr = models.CharField(max_length=40)

    def __str__(self):
        return self.name