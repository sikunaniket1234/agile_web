from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.db.models import Q
from .models import Service, PricingPlan, ContactLead, MarketingFeature, TechTool, BlogPost, Client, Project, HeroSlide, FooterSettings, SocialLink, Comment


def get_footer_context():
    return {
        'footer_settings': FooterSettings.objects.first(),
        'social_links': SocialLink.objects.filter(active=True),
    }
def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        service = request.POST.get('service-type')
        details = request.POST.get('project')
        
        # 1. Save to Database
        ContactLead.objects.create(name=name, email=email, service_type=service, project_details=details)
        
        # 2. Send Email Notification (Option B)
        subject = f"New Lead from {name} - {service}"
        message = f"Client: {name}\nEmail: {email}\nService: {service}\n\nProject:\n{details}"
        
        try:
            send_mail(
                subject, 
                message, 
                settings.DEFAULT_FROM_EMAIL, 
                [settings.ADMIN_EMAIL], # We will set this in settings.py
                fail_silently=False
            )
        except Exception as e:
            print(f"Email failed: {e}") # specific error printing for debug

        messages.success(request, 'Success! Your request has been sent.')
        return redirect('home')

    # Fetch all dynamic data
    # Blog Search Logic
    search_query = request.GET.get('q', '')
    blogs = BlogPost.objects.all().order_by('-date_posted')
    if search_query:
        blogs = blogs.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query))

    context = {
        'services': Service.objects.filter(active=True),
        'pricing_plans': PricingPlan.objects.all(),
        'marketing_features': MarketingFeature.objects.all(),
        'tech_stack': TechTool.objects.all(),
        'blogs': blogs,
        'search_query': search_query,
        # --- NEW DATA ---
        'clients': Client.objects.all(),
        'in_house_projects': Project.objects.filter(project_type='IN_HOUSE'),
        'ongoing_projects': Project.objects.filter(project_type='ONGOING'),
        'hero_slides': HeroSlide.objects.filter(active=True),
    }
    context.update(get_footer_context())
    return render(request, 'main/index.html', context)

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    
    # Increment View Counter
    post.views_count += 1
    post.save()
    
    # Handle Comment Form
    if request.method == 'POST' and 'comment_form' in request.POST:
        name = request.POST.get('name')
        body = request.POST.get('body')
        if name and body:
            Comment.objects.create(post=post, name=name, body=body)
            messages.success(request, 'Your comment was posted successfully!')
            return redirect('blog_detail', slug=post.slug)

    # Fetch Related Posts
    related_posts = BlogPost.objects.filter(category=post.category).exclude(id=post.id).order_by('-date_posted')[:3]

    context = {
        'post': post,
        'related_posts': related_posts,
    }
    context.update(get_footer_context())
    return render(request, 'main/blog_detail.html', context)
def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    # The sub_services are fetched automatically via the 'related_name' we defined in models
    context = {'service': service}
    context.update(get_footer_context())
    return render(request, 'main/service_detail.html', context)

def blog_list(request):
    search_query = request.GET.get('q', '')
    blogs = BlogPost.objects.all().order_by('-date_posted')
    if search_query:
        blogs = blogs.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query) | Q(category__icontains=search_query))

    context = {
        'blogs': blogs,
        'search_query': search_query,
    }
    context.update(get_footer_context())
    return render(request, 'main/blog_list.html', context)

def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
        f"Sitemap: {request.scheme}://{request.get_host()}/sitemap.xml",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")
