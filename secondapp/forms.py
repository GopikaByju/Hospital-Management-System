from django import forms

from secondapp.models import DepartmentModel, GalleryModel, FacilitiesModel, DoctorsModel, BookingModel, CareersModel


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = DepartmentModel
        fields='__all__'
        #fields = ['name', 'description']

class GalleryForm(forms.ModelForm):
    class Meta:
        model = GalleryModel
        fields='__all__'

class FacilitiesForm(forms.ModelForm):
    class Meta:
        model =FacilitiesModel
        fields='__all__'

class DoctorsForm(forms.ModelForm):
    class Meta:
        model=DoctorsModel
        fields='__all__'

class BookingForm(forms.ModelForm):
    class Meta:
        model=BookingModel
        fields='__all__'

class CareersForm(forms.ModelForm):
    class Meta:
        model=CareersModel
        fields='__all__'