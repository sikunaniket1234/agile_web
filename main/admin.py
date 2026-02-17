from django.contrib import admin
from .models import (
    Service, SubService, PricingPlan, ContactLead, 
    MarketingFeature, TechTool, BlogPost, HeroSlide, 
    Client, Project, FooterSettings, SocialLink
)

# 1. Define the Inline (Must come before ServiceAdmin)
class SubServiceInline(admin.TabularInline):
    model = SubService
    extra = 1

# 2. Register Service WITH the custom Admin class
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'active')
    inlines = [SubServiceInline] # This connects the SubService table to Service!

# 3. Register the rest of the models
admin.site.register(PricingPlan)
admin.site.register(ContactLead)
admin.site.register(MarketingFeature)
admin.site.register(TechTool)
admin.site.register(Client)
admin.site.register(Project)
admin.site.register(HeroSlide)
admin.site.register(FooterSettings)

# 4. Blog Admin
@admin.register(BlogPost)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date_posted')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('platform', 'url', 'active', 'order')
    list_filter = ('platform', 'active')
    search_fields = ('url',)
