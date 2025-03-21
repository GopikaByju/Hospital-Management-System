from django.contrib import admin

from secondapp.forms import FacilitiesForm
from secondapp.models import DepartmentModel, GalleryModel, FacilitiesModel, DoctorsModel, BookingModel, CareersModel, \
    Person

# Register your models here.
# from .models import DepartmentModel

admin.site.register(DepartmentModel)
admin.site.register(GalleryModel)
admin.site.register(FacilitiesModel)
admin.site.register(DoctorsModel)
admin.site.register(BookingModel)
admin.site.register(CareersModel)
admin.site.register(Person)
