from django.db import models
from django.utils.text import slugify

# --- Existing Models ---
# class Service(models.Model):
#     icon_name = models.CharField(max_length=50)
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     active = models.BooleanField(default=True)
#     def __str__(self): return self.title
# main/models.py

class Service(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, help_text="URL friendly name (auto-generated)")
    icon_name = models.CharField(max_length=50)
    short_description = models.TextField(help_text="Shown on Home Page cards")
    long_description = models.TextField(help_text="Shown on the detailed Service page")
    active = models.BooleanField(default=True)
    meta_title = models.CharField(max_length=70, blank=True, help_text="Title that appears on Google (Max 60 chars)")
    meta_description = models.TextField(max_length=160, blank=True, help_text="Description under the link on Google (Max 160 chars)")
    def save(self, *args, **kwargs):
        if not self.slug:
            original_slug = slugify(self.title)
            queryset = Service.objects.all()
            if self.pk:
                queryset = queryset.exclude(pk=self.pk)
            slug = original_slug
            counter = 1
            while queryset.filter(slug=slug).exists():
                slug = f"{original_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self): return self.title

class SubService(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='sub_services')
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_name = models.CharField(max_length=50, default="check_circle", help_text="Material Icon name")

    def __str__(self): return f"{self.service.title} - {self.title}"
class PricingPlan(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=20)
    period = models.CharField(max_length=20, default="/mo")
    is_popular = models.BooleanField(default=False)
    features = models.TextField(help_text="Comma-separated list")
    def get_features_list(self): return self.features.split(',')
    def __str__(self): return self.name

class ContactLead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    service_type = models.CharField(max_length=50)
    project_details = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"{self.name} - {self.email}"

# --- NEW MODELS ---

class MarketingFeature(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_url = models.CharField(max_length=255, help_text="URL to icon image (e.g., https://cdn...) or Material Icon name")
    is_image = models.BooleanField(default=True, help_text="Check if using an image URL, Uncheck if using Material Icon text")
    
    def __str__(self): return self.title

class TechTool(models.Model):
    name = models.CharField(max_length=50)
    logo_url = models.CharField(max_length=255)
    def __str__(self): return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, help_text="URL friendly name (auto-generated)")
    category = models.CharField(max_length=50) # e.g. Technology
    image_url = models.CharField(max_length=255, blank=True, null=True) # Cover image
    image_file = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    excerpt = models.TextField(help_text="Short summary for home page")

    @property
    def get_image_url(self):
        if self.image_file:
            return self.image_file.url
        return self.image_url if self.image_url else "https://via.placeholder.com/800x480"
    content = models.TextField(help_text="Full article content")
    date_posted = models.DateTimeField(auto_now_add=True)
    author_name = models.CharField(max_length=100, default="Agile Team")
    views_count = models.PositiveIntegerField(default=0)
    meta_title = models.CharField(max_length=70, blank=True)
    meta_description = models.TextField(max_length=160, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            original_slug = slugify(self.title)
            queryset = BlogPost.objects.all()
            if self.pk:
                queryset = queryset.exclude(pk=self.pk)
            slug = original_slug
            counter = 1
            while queryset.filter(slug=slug).exists():
                slug = f"{original_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self): return self.title

class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.post.title}"

class Client(models.Model):
    name = models.CharField(max_length=100)
    logo_url = models.CharField(max_length=255, help_text="URL to client logo image")
    website = models.URLField(blank=True, null=True)
    
    def __str__(self): return self.name

class Project(models.Model):
    STATUS_CHOICES = [
        ('IN_HOUSE', 'In-House Project'),
        ('ONGOING', 'Ongoing Project'),
        ('COMPLETED', 'Completed Case Study'),
    ]
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.CharField(max_length=255)
    project_type = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ONGOING')
    link = models.URLField(blank=True, null=True)
    
    def __str__(self): return self.title

# ... (Keep all your existing models: Service, Client, Project, etc.) ...

class HeroSlide(models.Model):
    GRAPHIC_CHOICES = [
        ('CUBE', '3D Cyber Cube'),
        ('RING', 'Pulsing Tech Ring'),
        ('GLOBE', ' glowing Globe Icon'),
        ('IMAGE', 'Standard Image (Use Image URL)'),
        ('NONE', 'No Graphic (Text Only)'),
    ]

    badge_text = models.CharField(max_length=50, default="Innovative Digital Solutions")
    heading_line_1 = models.CharField(max_length=50, default="Scale Your Vision")
    heading_gradient_text = models.CharField(max_length=50, default="Globally.")
    subtext = models.TextField(default="From custom software to viral marketing strategies...")
    
    # NEW FIELDS FOR GRAPHICS
    graphic_type = models.CharField(max_length=10, choices=GRAPHIC_CHOICES, default='CUBE')
    image_url = models.CharField(max_length=255, blank=True, null=True, help_text="Only used if 'Standard Image' is selected")
    
    active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)

    def __str__(self): return f"Slide: {self.heading_line_1}"

    class Meta:
        ordering = ['order']


class FooterSettings(models.Model):
    company_name = models.CharField(max_length=120, default="Agile Web")
    tagline = models.CharField(max_length=220, default="Building digital ecosystems that scale.")
    copyright_text = models.CharField(max_length=220, blank=True, help_text="Optional custom copyright line")

    def __str__(self):
        return f"Footer Settings - {self.company_name}"


class SocialLink(models.Model):
    PLATFORM_CHOICES = [
        ('X', 'X (Twitter)'),
        ('INSTAGRAM', 'Instagram'),
        ('FACEBOOK', 'Facebook'),
    ]

    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    url = models.URLField()
    active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']
        unique_together = ('platform', 'url')

    def __str__(self):
        return f"{self.platform} - {self.url}"
