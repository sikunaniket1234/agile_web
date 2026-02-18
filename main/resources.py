from import_export import resources
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget
from .models import (
    Service, SubService, PricingPlan, ContactLead, 
    MarketingFeature, TechTool, BlogPost, Client, 
    Project, HeroSlide, SocialLink
)

# 1. Hero Slide Resource
class HeroSlideResource(resources.ModelResource):
    class Meta:
        model = HeroSlide
        fields = ('id', 'heading_line_1', 'heading_gradient_text', 'subtext', 'badge_text', 'graphic_type', 'image_url', 'active', 'order')
        export_order = ('id', 'order', 'heading_line_1', 'graphic_type', 'active')

# 2. Service Resource
class ServiceResource(resources.ModelResource):
    class Meta:
        model = Service
        fields = ('id', 'title', 'slug', 'icon_name', 'short_description', 'long_description', 'active', 'meta_title', 'meta_description')
        export_order = ('id', 'title', 'active')

# 3. Sub-Service Resource (Linked to Service)
class SubServiceResource(resources.ModelResource):
    # This allows you to put the Service Title in the Excel sheet instead of just the ID number
    service = Field(
        column_name='service',
        attribute='service',
        widget=ForeignKeyWidget(Service, 'title')
    )

    class Meta:
        model = SubService
        fields = ('id', 'service', 'title', 'description', 'icon_name')

# 4. Project Resource
class ProjectResource(resources.ModelResource):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'image_url', 'project_type', 'link')

# 5. Pricing Plan Resource
class PricingPlanResource(resources.ModelResource):
    class Meta:
        model = PricingPlan
        fields = ('id', 'name', 'price', 'period', 'is_popular', 'features')

# 6. Marketing Feature Resource
class MarketingFeatureResource(resources.ModelResource):
    class Meta:
        model = MarketingFeature
        fields = ('id', 'title', 'description', 'icon_url', 'is_image')

# 7. Tech Tool Resource
class TechToolResource(resources.ModelResource):
    class Meta:
        model = TechTool
        fields = ('id', 'name', 'logo_url')

# 8. Blog Post Resource
class BlogPostResource(resources.ModelResource):
    class Meta:
        model = BlogPost
        fields = ('id', 'title', 'slug', 'category', 'image_url', 'excerpt', 'content', 'date_posted', 'meta_title')

# 9. Client Resource
class ClientResource(resources.ModelResource):
    class Meta:
        model = Client
        fields = ('id', 'name', 'logo_url', 'website')

# 10. Contact Lead Resource (Export Only - usually you don't import leads)
class ContactLeadResource(resources.ModelResource):
    class Meta:
        model = ContactLead
        fields = ('id', 'name', 'email', 'service_type', 'project_details', 'submitted_at')

# 11. Social Link Resource
class SocialLinkResource(resources.ModelResource):
    class Meta:
        model = SocialLink
        fields = ('id', 'platform', 'url', 'active', 'order')