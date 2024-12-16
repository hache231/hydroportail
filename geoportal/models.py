from django.db import models

# Create your models here.
class station(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    owner = models.CharField(max_length=100)
    physical_adresse = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    state = models.CharField(max_length=100, blank=True, null=True)
    Storage_capacity = models.FloatField(blank=True, null=True)
    Opening_hours = models.TimeField(blank=True, null=True)
    closing_hours = models.TimeField(blank=True, null=True)
    type = models.ForeignKey('type', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id) 

    
class product(models.Model):
    product_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id) + " " + self.product_name

class source(models.Model):
    source_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id) + " " + self.source_name

class service(models.Model):
    service_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id) + " " + self.service_name

class type(models.Model):
    type_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id) + " " + self.type_name

class Vendre(models.Model):
    station = models.ForeignKey(station, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Fournir(models.Model):
    station = models.ForeignKey(station, on_delete=models.CASCADE)
    source = models.ForeignKey(source, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Offrir(models.Model):
    station = models.ForeignKey(station, on_delete=models.CASCADE)
    service = models.ForeignKey(service, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

