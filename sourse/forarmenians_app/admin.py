from django.contrib import admin
from forarmenians_app.models import *

admin.site.register(Ad)
admin.site.register(AdAddress)
admin.site.register(AdCountry)
admin.site.register(AdState)
admin.site.register(AdPhoto)

admin.site.register(VehicleBrand)
admin.site.register(VehicleModel)
admin.site.register(VehicleCarcaseType)
admin.site.register(VehicleDriveUnit)
admin.site.register(VehicleMotorType)
admin.site.register(VehicleYear)
admin.site.register(VehicleAd)

admin.site.register(JobAd)
admin.site.register(JobKeySkills)
admin.site.register(JobWorkExperience)
admin.site.register(JobLanguageSkill)
admin.site.register(JobVacancy)
admin.site.register(JobResume)

admin.site.register(NewsCategory)
admin.site.register(News)

admin.site.register(EntertainmentType)
admin.site.register(EntertainmentAd)

