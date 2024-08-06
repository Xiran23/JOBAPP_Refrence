from django.contrib import admin

from app.models import JobPost,Location,Skills,Author

# Register your models here.
# class JobAdmin(admin.ModelAdmin):
#     # pass 
#     list_display = ('__str__','titel','date', 'salary')
#     list_filter = ('date','salary','expiry')
#     search_fields = ['titel','description']
#     search_help_text = "write it and see it - cjora thapa"
#     # fields = (('title','description'),'expiry')
#     # exclude =  ('title',)
#     fieldsets= (
#         ('Basic information',{
#             'fields':('titel','description')
#         }),
#          ('More information',{
#              'classes':('collapse','wide'), 
#             'fields':(('expiry','salary'),'slug')
#         }),

    # )
    
# admin.site.register(JobPost,JobAdmin) 
admin.site.register(JobPost) 
admin.site.register(Location)
admin.site.register(Author) 
admin.site.register(Skills)