from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    # Fields to display
    list_display = (
        'name',
        'subject',
        'user_id',
        'email',
        'contact_date',
    )

    search_fields = (
        'name',
        'email',
    )

    list_per_page = 25

    # orders contacts by date
    ordering = ('contact_date',)


admin.site.register(Contact, ContactAdmin)
