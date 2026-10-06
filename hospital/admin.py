from django.contrib import admin

# Register your models here.
from.models import UserComplaints
from.models import department,Doctors,hospital,online,vir,tokenbooking

class usercomplaintsAdmin(admin.ModelAdmin):
    pass
admin.site.register(UserComplaints,usercomplaintsAdmin)

class departmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(department,departmentAdmin)
admin.site.register(Doctors)
admin.site.register(hospital)
admin.site.register(vir)
admin.site.register(online)
admin.site.register(tokenbooking)


