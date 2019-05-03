from django.contrib import admin

from displays.models import MyDisplayModel, Line, Display

admin.site.register(Line)


class LineinLine(admin.StackedInline):
    model = Line
    extra = 0


class MyDisplayAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['friendly_name', ]}),
        ('Display information', {'fields': ['serial_number']}),
    ]
    inlines = [LineinLine]


# admin.site.register(Display)
admin.site.register(Display, MyDisplayAdmin)
