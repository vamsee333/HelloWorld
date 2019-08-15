from django.contrib import admin
from .models import HomePageItems,FAQ,RelatedAnswers
# Register your models here.
admin.site.register(HomePageItems)
admin.site.register(FAQ)
admin.site.register(RelatedAnswers)
