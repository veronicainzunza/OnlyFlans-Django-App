from django.contrib import admin
from .models import Flan, ContactForm

# Register your models here.
@admin.register(Flan)
class FlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image_url', 'slug','is_private')
    search_fields = ('name','slug')
    list_filter = ('name','slug')


@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_email', 'message', 'contact_form_uuid')
    search_fields = ('customer_name', 'customer_email')



