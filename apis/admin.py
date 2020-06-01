from django.contrib import admin
from apis.models import Driver, Area, Residents, Vehicle, Complaint


# Register your models here.
admin.site.register(Driver)
admin.site.register(Area)
admin.site.register(Residents)
admin.site.register(Vehicle)
admin.site.register(Complaint)