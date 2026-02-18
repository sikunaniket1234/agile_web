from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import (
    Service, SubService, PricingPlan, ContactLead, 
    MarketingFeature, TechTool, BlogPost, Client, 
    Project, HeroSlide, FooterSettings, SocialLink
)
from .resources import (
    HeroSlideResource, ServiceResource, SubServiceResource, 
    ProjectResource, PricingPlanResource, MarketingFeatureResource, 
    TechToolResource, BlogPostResource, ClientResource, 
    ContactLeadResource, SocialLinkResource
)

# 1. Define the Inline for SubService (Allows adding sub-services inside Service page)
class SubServiceInline(admin.TabularInline):
    model = SubService
    extra = 1

# 2. Hero Slide Admin (With Import/Export)
@admin.register(HeroSlide)
class HeroSlideAdmin(ImportExportModelAdmin):
    resource_class = HeroSlideResource
    list_display = ('heading_line_1', 'graphic_type', 'active', 'order')
    list_editable = ('active', 'order')

# 3. Service Admin (With Import/Export AND Inline)
@admin.register(Service)
class ServiceAdmin(ImportExportModelAdmin):
    resource_class = ServiceResource
    list_display = ('title', 'icon_name', 'active')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [SubServiceInline] # Connects SubService table inside Service page

# 4. SubService Admin (Optional: allows bulk importing SubServices separately)
@admin.register(SubService)
class SubServiceAdmin(ImportExportModelAdmin):
    resource_class = SubServiceResource
    list_display = ('title', 'service', 'icon_name')
    list_filter = ('service',)

# 5. Project Admin
@admin.register(Project)
class ProjectAdmin(ImportExportModelAdmin):
    resource_class = ProjectResource
    list_display = ('title', 'project_type', 'link')
    list_filter = ('project_type',)

# 6. Pricing Plan Admin
@admin.register(PricingPlan)
class PricingPlanAdmin(ImportExportModelAdmin):
    resource_class = PricingPlanResource
    list_display = ('name', 'price', 'is_popular')

# 7. Marketing Feature Admin
@admin.register(MarketingFeature)
class MarketingFeatureAdmin(ImportExportModelAdmin):
    resource_class = MarketingFeatureResource
    list_display = ('title', 'is_image')

# 8. Tech Tool Admin
@admin.register(TechTool)
class TechToolAdmin(ImportExportModelAdmin):
    resource_class = TechToolResource
    list_display = ('name',)

# 9. Blog Post Admin
@admin.register(BlogPost)
class BlogPostAdmin(ImportExportModelAdmin):
    resource_class = BlogPostResource
    list_display = ('title', 'category', 'date_posted')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('category',)

# 10. Client Admin
@admin.register(Client)
class ClientAdmin(ImportExportModelAdmin):
    resource_class = ClientResource
    list_display = ('name',)

# 11. Contact Lead Admin
@admin.register(ContactLead)
class ContactLeadAdmin(ImportExportModelAdmin):
    resource_class = ContactLeadResource
    list_display = ('name', 'email', 'service_type', 'submitted_at')
    readonly_fields = ('submitted_at',)
    list_filter = ('service_type', 'submitted_at')

# 12. Social Link Admin
@admin.register(SocialLink)
class SocialLinkAdmin(ImportExportModelAdmin):
    resource_class = SocialLinkResource
    list_display = ('platform', 'url', 'active', 'order')
    list_editable = ('order', 'active')
    list_filter = ('platform', 'active')

# 13. Footer Settings (Standard Admin is usually fine for single objects)
admin.site.register(FooterSettings)