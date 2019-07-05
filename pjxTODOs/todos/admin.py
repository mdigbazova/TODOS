from django.contrib import admin

from . models import Todo, Profile

# Register your models here.


#class TodoAdmin(admin.ModelAdmin):
    # readonly_fields = ('highlighted',)


admin.site.register(Todo)
admin.site.register(Profile)
