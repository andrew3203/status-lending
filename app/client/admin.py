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


class ImageAdminInline(admin.TabularInline):
    model = Image


class FeatureAdminInline(admin.TabularInline):
    model = Feature


class AdvantageAdminInline(admin.StackedInline):
    model = Advantage
    fieldsets = [
        ('', {
           'fields': (
            ('name', 'image'),
            ('desciption',)
           )
        })
    ]



@admin.register(Complex)
class ComplexAdmin(admin.ModelAdmin):
    list_display = ['name', 'square', 'price', 'site', 'created_at', 'updated_at']
    search_fields =  ['name', 'square', 'price']
    list_filter = ['is_published', SiteFilter]
    inlines = [
        FeatureAdminInline,
        ImageAdminInline,
        AdvantageAdminInline
    ]
    
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


@admin.register(SiteData)
class SiteDataAdmin(admin.ModelAdmin):
    list_display = ['site', 'meta_title', 'created_at',]
    search_fields =  ['site', 'meta_title', 'meta_description']
    list_filter = [SiteFilter,]
    
    fieldsets = [
        ('Основное', {
            'fields': (
                ('site',),
                ('meta_title',),
                ('meta_description',),
                ('scripts',),
                ('created_at',),
                ),
            }
        )
    ]
    readonly_fields = ['created_at',]


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['site', 'name', 'phone', 'email', 'created_at']
    search_fields =  ['site', 'name', 'phone', 'email']
    list_filter = [SiteFilter,]
    
    fieldsets = [
        ('Основное', {
            'fields': (
                ('site',),
                ('name', 'phone', 'email'),
                ('created_at',),
                ),
            }
        )
    ]
    readonly_fields = ['created_at',]