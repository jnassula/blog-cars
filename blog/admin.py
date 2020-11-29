from django.contrib import admin
from blog.models import Brand, Model, Fuel, Car

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Fuel)
class FuelAdmin(admin.ModelAdmin):
    pass


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass
