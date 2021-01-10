from django.contrib import admin
from Prediction.models import Predictions
from django import forms
# Register your models here.
class prediction(admin.ModelAdmin):
    list_display=('profile','age','sex','cp','resting_bp','fasting_blood_sugar','resting_ecg','max_heart_rate','exercise_induced_angina','st_depression','st_slope','number_of_vessels','thallium_scan_results','predicted_on','pred_percentage')
admin.site.register(Predictions,prediction)

from Prediction.models import UserProfileInfo

class UserProfile(admin.ModelAdmin):
    list_display = ('user','image_tag')
admin.site.register(UserProfileInfo,UserProfile)

