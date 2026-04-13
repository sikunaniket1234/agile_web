import os
import django
import random
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agile_web.settings')
django.setup()

from main.models import (
    Service, SubService, PricingPlan, ContactLead, MarketingFeature,
    TechTool, BlogPost, Client, Project, HeroSlide, FooterSettings, SocialLink, Comment
)

def run():
    print("Clearing old data...")
    Service.objects.all().delete()
    PricingPlan.objects.all().delete()
    ContactLead.objects.all().delete()
    MarketingFeature.objects.all().delete()
    TechTool.objects.all().delete()
    BlogPost.objects.all().delete()
    Client.objects.all().delete()
    Project.objects.all().delete()
    HeroSlide.objects.all().delete()
    FooterSettings.objects.all().delete()
    SocialLink.objects.all().delete()
    Comment.objects.all().delete() # New model!

    print("Seeding Services & SubServices...")
    s1 = Service.objects.create(
        title="Web Development", 
        icon_name="code", 
        short_description="Modern web apps designed for scale.",
        long_description="We build robust full-stack applications using Django, React, and modern cloud technologies to ensure your business scales effectively.",
    )
    SubService.objects.create(service=s1, title="Frontend Engineering", description="React, Vue, and Angular expertise.", icon_name="web")
    SubService.objects.create(service=s1, title="Backend Architecture", description="Python and Node.js scalable backends.", icon_name="storage")

    s2 = Service.objects.create(
        title="SEO Optimization",
        icon_name="trending_up",
        short_description="Data-driven SEO to rank higher.",
        long_description="Our technical and content SEO strategies bring organic and engaging traffic right to your doorstep.",
    )
    SubService.objects.create(service=s2, title="Technical SEO", description="Site speed, sitemaps, and core web vitals.", icon_name="speed")

    s3 = Service.objects.create(
        title="Mobile Apps",
        icon_name="smartphone",
        short_description="Native and cross-platform apps.",
        long_description="We craft elegant, lightning-fast mobile apps using Flutter and React Native for both iOS and Android platforms.",
    )
    SubService.objects.create(service=s3, title="iOS native", description="Swift development for Apple ecosystem.", icon_name="phone_iphone")
    SubService.objects.create(service=s3, title="Cross-Platform", description="Flutter and React Native solutions.", icon_name="devices")

    s4 = Service.objects.create(
        title="Cloud Infrastructure",
        icon_name="cloud",
        short_description="AWS, GCP, and Azure migrations.",
        long_description="Scale without limits. We migrate, monitor, and manage zero-downtime infrastructure for enterprise operations.",
    )
    SubService.objects.create(service=s4, title="Kubernetes", description="High-availability container orchestration.", icon_name="view_module")

    print("Seeding Tech Tools...")
    TechTool.objects.create(name="Django", logo_url="https://static.djangoproject.com/img/logos/django-logo-negative.png")
    TechTool.objects.create(name="React", logo_url="https://upload.wikimedia.org/wikipedia/commons/a/a7/React-icon.svg")
    TechTool.objects.create(name="AWS", logo_url="https://upload.wikimedia.org/wikipedia/commons/9/93/Amazon_Web_Services_Logo.svg")
    TechTool.objects.create(name="Docker", logo_url="https://www.docker.com/wp-content/uploads/2022/03/vertical-logo-monochromatic.png")
    TechTool.objects.create(name="PostgreSQL", logo_url="https://upload.wikimedia.org/wikipedia/commons/2/29/Postgresql_elephant.svg")

    print("Seeding Pricing Plans...")
    PricingPlan.objects.create(name="Starter", price="$499", period="/mo", is_popular=False, features="Basic Website,5 Pages,Email Support,Basic SEO")
    PricingPlan.objects.create(name="Pro", price="$999", period="/mo", is_popular=True, features="Custom Web App,Unlimited Pages,Priority Support,Advanced SEO,Analytics")
    PricingPlan.objects.create(name="Enterprise", price="Custom", period="/yr", is_popular=False, features="Dedicated Team,Custom Architecture,24/7 Support,Penetration Testing")

    print("Seeding Marketing Features...")
    MarketingFeature.objects.create(title="Global Reach", description="Connect with users around the world natively.", icon_url="public", is_image=False)
    MarketingFeature.objects.create(title="High Conversion", description="Optimized UX to turn visitors into aggressive buyers.", icon_url="https://cdn-icons-png.flaticon.com/512/3135/3135715.png", is_image=True)
    MarketingFeature.objects.create(title="A/B Testing", description="Data-centric iterations to improve metrics.", icon_url="assessment", is_image=False)
    MarketingFeature.objects.create(title="Viral Media", description="Leverage algorithms across social platforms.", icon_url="share", is_image=False)

    print("Seeding Long Blog Posts...")
    b1 = BlogPost.objects.create(
        title="The Architect's Guide to Django Channels & WebSockets",
        category="Engineering",
        image_url="https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&q=80&w=800",
        excerpt="Master real-time data flow in your Python web apps seamlessly.",
        content="""The world of web development is increasingly pivoting towards real-time interactivity. Gone are the days when a simple page reload was acceptable for fetching new data. Today's users expect live chat, dynamic notifications, and live-updating dashboards.

Enter Django Channels.

Historically, Django was built around a synchronous request-response cycle. It excelled at generating HTML, processing forms, and interacting with databases. However, scaling it for persistent connections like WebSockets was challenging. Django Channels changes this paradigm by wrapping Django's core with an asynchronous event loop (using ASGI).

### Understanding ASGI
ASGI (Asynchronous Server Gateway Interface) is the spiritual successor to WSGI. It provides a standard interface between async-capable Python web servers, frameworks, and applications. 

### Implementing a Basic Consumer
A 'Consumer' in Channels is akin to a 'View' in standard Django. It accepts an incoming connection, processes messages, and sends responses. By subclassing `AsyncWebsocketConsumer`, you can manage a WebSocket lifecycle:
1. `connect()`: Authenticate the user and accept the socket.
2. `receive()`: Parse incoming JSON payloads and execute business logic.
3. `disconnect()`: Clean up resources and remove the user from broadcast groups.

If you are building an enterprise application, integrating Redis as a channel layer is non-negotiable. Redis acts as the message broker, allowing different instances of your application (or different workers) to communicate. This means a user connected to Worker A can instantly receive a chat message sent by a user connected to Worker B.

By mastering Django Channels, you elevate your backend architecture from a static data supplier into a living, real-time ecosystem."""
    )
    
    b2 = BlogPost.objects.create(
        title="Why SEO Fails: The Hidden Technical Debt",
        category="Marketing",
        image_url="https://images.unsplash.com/photo-1432888498266-38ffec3eaf0a?auto=format&fit=crop&q=80&w=800",
        excerpt="Are JavaScript frameworks destroying your Google rankings?",
        content="""You've launched a stunning, blazing-fast React application. The animations are smooth, the user experience is flawless, and the design is award-winning. But a month later, your organic traffic is flatlining. Why?

The culprit is often Technical SEO debt introduced by Client-Side Rendering (CSR).

### The JavaScript Rendering Penalty
When Googlebot crawls a standard HTML page, the content is immediately available in the raw response. However, when it crawls a React or Vue SPA (Single Page Application), the initial HTML is essentially empty (usually just a `<div id="root"></div>`). Googlebot has to queue the page for JavaScript execution, which is resource-intensive and delayed. Sometimes, this rendering fails or times out, resulting in unindexed content.

### The Solution: SSR and SSG
To combat this, the industry has heavily gravitated towards Next.js (for React) and Nuxt.js (for Vue). 

**Server-Side Rendering (SSR)** generates the HTML on a node server for every request. This ensures the bot receives a fully populated HTML document immediately. 
**Static Site Generation (SSG)** pre-renders the HTML at build time, yielding the absolute fastest Time to First Byte (TTFB) possible, which is a massive ranking factor in Core Web Vitals.

### Beyond Rendering: Core Web Vitals
Google's algorithm now heavily penalizes layout shifts (CLS) and slow paint times (LCP). If you are loading massive unoptimized hero images or injecting ad scripts that push content down the page as it loads, your rankings will suffer regardless of your content quality.

True SEO is no longer just about keywords and backlinks; it's a deeply technical engineering challenge."""
    )

    b3 = BlogPost.objects.create(
        title="Scaling PostgreSQL for 1 Million Concurrent Users",
        category="Engineering",
        image_url="https://images.unsplash.com/photo-1544197150-b99a580bb7a8?auto=format&fit=crop&q=80&w=800",
        excerpt="Database indexing, connection pooling, and read replicas.",
        content="""PostgreSQL is arguably the most advanced open-source relational database in the world. However, out of the box, it is configured for maximum compatibility—not maximum performance under extreme load. 

When your application suddenly goes viral, the database is almost always the first bottleneck.

### 1. Connection Pooling (PgBouncer)
PostgreSQL handles each connection by spawning a new OS process. This consumes significant RAM (usually around 10MB per connection). If 5,000 users connect simultaneously, your database server will crash entirely from memory exhaustion. 

Enter PgBouncer. It maintains a pool of active connections to the database and multiplexes thousands of lightweight client connections on top of them. This is mandatory for scaling.

### 2. Strategic Indexing
A missing index on a heavily queried foreign key can turn a 2ms query into a 2-second sequential scan. However, over-indexing is also detrimental—every index slows down INSERT and UPDATE operations. We recommend utilizing `pg_stat_statements` to identify the most expensive queries and indexing specifically for those access patterns.

### 3. Read Replicas
For most web tier applications, the read-to-write ratio is heavily skewed (e.g., 90% reads, 10% writes). By standing up multiple Read Replicas, you can route operations like user authentication, dashboard loads, and reporting to the replicas, reserving the primary database exclusively for critical transactional writes.

Mastering these three pillars ensures PostgreSQL remains a bedrock for your infrastructure, rather than a single point of failure."""
    )

    b4 = BlogPost.objects.create(
        title="UI Trends 2026: Glassmorphism Meets Neo-Brutalism",
        category="Design",
        image_url="https://images.unsplash.com/photo-1558222218-b7b54eede3f3?auto=format&fit=crop&q=80&w=800",
        excerpt="How opposing design paradigms are merging into a unified aesthetic.",
        content="""For the last five years, web design has been torn between two aggressive extremes: the hyper-polished, blurred-background elegance of Glassmorphism (popularized by macOS and iOS), and the aggressive, raw, high-contrast shock of Neo-Brutalism (popularized by Figma, Gumroad, and indie SaaS).

In 2026, we are witnessing a fascinating synthesis.

### The Best of Both Worlds
Designers are building interfaces that utilize the structural grid and bold typography of Neo-Brutalism, but softening the internal elements with Glassmorphic utility panes. The result is an interface that feels highly legible and energetic, but simultaneously premium and deep.

**Key Characteristics:**
- **Harsh Borders, Soft Backgrounds:** Using strict 2px solid black (or bright white) borders for layout structure, while the content areas themselves feature deep `backdrop-filter: blur(20px)` glass effects.
- **Aggressive Typography:** Giant, overlapping headers juxtaposed with delicate UI typography for data tables.
- **Kinetic Interactions:** Buttons don't just gently fade—they physically depress with sharp transform transitions, providing intense haptic-like visual feedback.

This merge proves that aesthetic trends aren't linear; they are cyclical and combinatorial. By blending these styles, we create digital environments that are visually striking yet remarkably intuitive."""
    )

    print("Seeding Comments for Blogs...")
    Comment.objects.create(post=b1, name="Alice Chen", body="This completely clarified how ASGI works compared to WSGI. I struggled with Channels for weeks before this. Thank you!")
    Comment.objects.create(post=b1, name="DevOps Dan", body="Are you planning to write a follow-up on deploying Channels with Daphne vs Uvicorn in production?")
    Comment.objects.create(post=b2, name="Sarah SEO", body="Spot on. I see so many clients drop 50% of their organic traffic when they rebuild their site in React without configuring Next.js SSR.")
    Comment.objects.create(post=b3, name="Marcus DB", body="PgBouncer is a lifesaver. It literally took our RDS CPU utilization from 95% down to 20% overnight.")
    Comment.objects.create(post=b4, name="Designer Dave", body="I've definitely noticed this trend on awwwards. It's a tricky balance but looks amazing when pulled off right.")

    print("Seeding Clients...")
    Client.objects.create(name="TechCorp", logo_url="https://upload.wikimedia.org/wikipedia/commons/a/a9/Amazon_logo.svg", website="https://techcorp.com")
    Client.objects.create(name="GlobalNet", logo_url="https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg", website="https://globalnet.io")
    Client.objects.create(name="Finastra", logo_url="https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Cisco_logo_blue_2016.svg/1024px-Cisco_logo_blue_2016.svg.png", website="#")
    Client.objects.create(name="AeroDynamics", logo_url="https://upload.wikimedia.org/wikipedia/commons/a/ab/Apple-logo.png", website="#")

    print("Seeding Projects...")
    Project.objects.create(
        title="Agile E-commerce Prototype",
        description="A modern frontend prototype for retail.",
        image_url="https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&q=80&w=500",
        project_type="IN_HOUSE",
    )
    Project.objects.create(
        title="FinTech Dashboard",
        description="Revamping a banking portal.",
        image_url="https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&q=80&w=500",
        project_type="COMPLETED",
    )
    Project.objects.create(
        title="Healthcare Analytics",
        description="HIPAA compliant data processing.",
        image_url="https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&fit=crop&q=80&w=500",
        project_type="ONGOING",
    )
    Project.objects.create(
        title="AI Chatbot Cluster",
        description="Customer support automated via LLMs.",
        image_url="https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&q=80&w=500",
        project_type="ONGOING",
    )

    print("Seeding Hero Slides...")
    HeroSlide.objects.create(
        badge_text="Welcome to Agile Web",
        heading_line_1="Transform Your",
        heading_gradient_text="Digital Future.",
        subtext="We build custom digital ecosystems for enterprise operations.",
        graphic_type="CUBE",
        order=1
    )
    HeroSlide.objects.create(
        badge_text="Audience Growth",
        heading_line_1="Reach a Global",
        heading_gradient_text="Audience.",
        subtext="Marketing strategies, SEO, and Analytics that deliver direct ROI.",
        graphic_type="RING",
        order=2
    )

    print("Seeding Footer...")
    FooterSettings.objects.create(
        company_name="Agile Web Services",
        tagline="Empowering your digital journey safely since 2026.",
        copyright_text="© 2026 Agile Web Services. All rights reserved."
    )
    SocialLink.objects.create(platform="X", url="https://twitter.com/", order=1)
    SocialLink.objects.create(platform="FACEBOOK", url="https://facebook.com/", order=2)
    SocialLink.objects.create(platform="INSTAGRAM", url="https://instagram.com/", order=3)

    print("Database successfully seeded!")

if __name__ == '__main__':
    run()
