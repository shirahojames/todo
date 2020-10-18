from django.contrib import admin
from .models import Todo
# Register your models here.


#make a class that will display the created(readonly) in the admin age
class admini(admin.ModelAdmin):
    readonly_fields=('created',)

admin.site.register(Todo, admini)
