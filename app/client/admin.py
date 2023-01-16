from django.contrib import admin
from client.models import *


class SiteFilter(admin.SimpleListFilter):
    title = 'Сайты'
    parameter_name = 'site_pk'

    def lookups(self, request, model_admin):
        sites = set([o.site.site for o in model_admin.model.objects.all()])
        return [(c.id, c.name) for c in sites]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(site__site__pk=self.value())
        else:
            return queryset


@admin.register(Complex)
class ComplexAdmin(admin.ModelAdmin):
    list_display = ['name', 'square', 'price', 'site', 'created_at', 'updated_at']
    search_fields =  ['name', 'square', 'price']
    list_filter = ['is_published', SiteFilter]
    
    fieldsets = [
        ('Основное', {
            'fields': (
                ('name', 'square', 'price'),
                ('site', 'is_published'),
                ('title_image', 'presentation', 'second_image'),
                ('desciption',),
                ('map',),
                ('wh_link', 'tg_link',),
                ('created_at', 'updated_at',),
                ),
            }
        )
    ]
    readonly_fields = ['created_at', 'updated_at']