from django.contrib import admin

from displays.models import MyDisplayModel, Line, Display

admin.site.register(Line)


class LineinLine(admin.StackedInline):
    model = Line
    extra = 0


class MyDisplayAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['display_model', ]}),
        ('Display information', {'fields': ['max_lines']}),
    ]
    # inlines = [LineinLine]


admin.site.register(Display)
admin.site.register(MyDisplayModel, MyDisplayAdmin)
