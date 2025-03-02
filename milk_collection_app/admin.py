from django.contrib import admin
from .models import CollectionCenter

# Commented out other models
# from .models import Farmer, MilkCollectionEntry, Staff

# class MilkCollectionEntryAdmin(admin.ModelAdmin):
#     list_display = ('farmer', 'quantity', 'collection_date', 'collection_time')

# admin.site.register(Farmer)
admin.site.register(CollectionCenter)
# admin.site.register(MilkCollectionEntry, MilkCollectionEntryAdmin)
# admin.site.register(Staff)
