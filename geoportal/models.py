from django.db import models

# Create your models here.

class provinces(models.Model):
    province_name = models.CharField(max_length=100)
    p_cent_lat = models.FloatField(max_length=20, default="")
    p_cent_long = models.FloatField(max_length=20, default="")

    def __str__(self):
        return str(self.pk) +" "+ self.province_name 

class territories(models.Model):
    territory_name = models.CharField(max_length=100)
    t_cent_lat = models.FloatField(max_length=20, default="")
    t_cent_long = models.FloatField(max_length=20, default="")
    province = models.ForeignKey('provinces', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) +" "+ self.territory_name

class sectors(models.Model):
    sector_name = models.CharField(max_length=100)
    s_cent_lat = models.FloatField(max_length=20, default="")
    s_cent_long = models.FloatField(max_length=20, default="")
    territory = models.ForeignKey('territories', on_delete=models.CASCADE)


    def __str__(self):
        return self.sector_name

class station(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    owner = models.CharField(max_length=100)
    physical_adresse = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    state = models.CharField(max_length=100, blank=True, null=True)
    storage_capacity = models.FloatField(blank=True, null=True)
    opening_hours = models.TimeField(blank=True, null=True)
    closing_hours = models.TimeField(blank=True, null=True)
    type = models.ForeignKey('type', on_delete=models.CASCADE)
    sector = models.ForeignKey('sectors', on_delete=models.CASCADE)
    territory = models.ForeignKey('territories', on_delete=models.CASCADE)
    province = models.ForeignKey('provinces', on_delete=models.CASCADE)
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

