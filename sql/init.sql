-- init_data.sql
-- Run this AFTER 'python manage.py migrate' has created the table structure.

-- 1. Create Superuser (Admin)
-- Password matches the hash provided (likely 'admin' or similar dev password)
INSERT INTO public.auth_user (
    password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined
)
VALUES (
    'pbkdf2_sha256$600000$bxN6DI9D44ETLjSkmLwiH3$ZR7XWUdnJLH6EcpNEzBfHTSzpmjIApWYWmhQNYA9QtA=', 
    NULL, TRUE, 'admin', 'Admin', 'User', 'admin@agile-web.com', TRUE, TRUE, NOW()
)
ON CONFLICT (username) DO NOTHING; -- Prevents error if admin exists


-- 2. Clear existing app data (Start Fresh)
TRUNCATE TABLE main_subservice, main_service, main_pricingplan, main_heroslide, main_client, main_project, main_marketingfeature, main_techtool, main_blogpost RESTART IDENTITY CASCADE;


-- 3. Hero Slides (High Impact)
INSERT INTO main_heroslide (badge_text, heading_line_1, heading_gradient_text, subtext, active, "order") VALUES
('Digital Excellence', 'Build Your', 'Legacy.', 'We engineer digital products that define industry standards and drive exponential growth for businesses in Bhubaneswar and beyond.', true, 1),
('AI Integrated', 'Future Proof', 'Solutions.', 'Leverage the power of Artificial Intelligence to automate workflows and scale faster.', true, 2),
('Global Scale', 'Expand Your', 'Reach.', 'Cloud-native architecture designed to handle millions of users from day one.', true, 3);


-- 4. Services (SEO Optimized)
INSERT INTO main_service (title, slug, icon_name, short_description, long_description, active, meta_title, meta_description) VALUES
('Web Development', 'web-development', 'language', 'High-performance websites built with React & Django.', 'We build lightning-fast, SEO-optimized websites using modern technologies like React, Next.js, and Django. Whether you need a simple landing page or a complex SaaS platform, our code is clean, scalable, and secure.', true, 'Custom Web Development Services in Bhubaneswar | Agile Web', 'Top-tier web development services using Python and React. We build fast, responsive, and SEO-friendly websites.'),
('Mobile App Development', 'mobile-app-development', 'smartphone', 'Native and Cross-platform mobile apps.', 'Turn your idea into a mobile reality. We specialize in Flutter and React Native to deliver smooth, native-like experiences on both iOS and Android from a single codebase.', true, 'Mobile App Development Agency | Agile Web', 'Build fast, responsive mobile apps for iOS and Android with our expert Flutter developers.'),
('Cloud & DevOps', 'cloud-devops', 'cloud', 'Scalable cloud infrastructure on AWS & Azure.', 'Stop worrying about server crashes. We set up robust CI/CD pipelines, Docker containers, and Kubernetes clusters to ensure your application scales automatically with traffic.', true, 'Cloud Infrastructure & DevOps Services | Agile Web', 'Expert DevOps services to scale your business infrastructure on AWS and Google Cloud.');


-- 5. Sub-Services (Specific Offerings)
-- Note: Assumes Service IDs are 1, 2, 3 based on insertion order
INSERT INTO main_subservice (service_id, title, description, icon_name) VALUES
(1, 'SaaS Platforms', 'Multi-tenant architecture for scalable software products.', 'layers'),
(1, 'E-Commerce', 'Custom Shopify and WooCommerce integrations for retail.', 'shopping_cart'),
(1, 'PWA Development', 'Progressive Web Apps that work offline and load instantly.', 'wifi_tethering'),
(2, 'Flutter Apps', 'Single codebase for iOS and Android deployment.', 'flutter_dash'),
(2, 'UI/UX Design', 'User-centric mobile interfaces that drive engagement.', 'brush'),
(3, 'AWS Migration', 'Move your legacy systems to the secure cloud.', 'cloud_upload'),
(3, 'CI/CD Pipelines', 'Automated testing and deployment workflows.', 'loop');


-- 6. Pricing Plans
INSERT INTO main_pricingplan (name, price, period, is_popular, features) VALUES
('Startup', '999', '/mo', false, 'Custom Landing Page,Basic SEO Setup,5 Social Media Posts,Email Support'),
('Growth', '2,499', '/mo', true, 'Full Web Application,Advanced SEO & Backlinks,15 Social Media Posts,Priority Support,Ads Management'),
('Enterprise', 'Custom', '', false, 'Dedicated Dev Team,24/7 SLA Support,Custom Cloud Architecture,Global SEO Strategy');


-- 7. Marketing Features
INSERT INTO main_marketingfeature (title, description, icon_url, is_image) VALUES
('SEO Dominance', 'Rank #1 on Google with our data-driven keyword strategy and schema markup.', 'search', false),
('Social Growth', 'Explode your following on Instagram and LinkedIn with organic content strategies.', 'trending_up', false),
('Paid Ads', 'High-ROI Facebook and Google ad campaigns targeted to your ideal audience.', 'attach_money', false);


-- 8. Tech Stack
INSERT INTO main_techtool (name, logo_url) VALUES
('React', 'https://cdn.worldvectorlogo.com/logos/react-2.svg'),
('Django', 'https://cdn.worldvectorlogo.com/logos/django.svg'),
('Python', 'https://cdn.worldvectorlogo.com/logos/python-5.svg'),
('AWS', 'https://cdn.worldvectorlogo.com/logos/aws-2.svg'),
('Docker', 'https://cdn.worldvectorlogo.com/logos/docker-4.svg'),
('PostgreSQL', 'https://cdn.worldvectorlogo.com/logos/postgresql.svg');


-- 9. Clients
INSERT INTO main_client (name, logo_url, website) VALUES
('TechCorp', 'https://cdn.worldvectorlogo.com/logos/google-1-1.svg', 'https://google.com'),
('FinStart', 'https://cdn.worldvectorlogo.com/logos/stripe-4.svg', 'https://stripe.com'),
('EduLearn', 'https://cdn.worldvectorlogo.com/logos/udemy-1.svg', 'https://udemy.com'),
('HealthPlus', 'https://cdn.worldvectorlogo.com/logos/blue-cross-blue-shield-1.svg', '#');


-- 10. Projects (Real Context)
INSERT INTO main_project (title, description, image_url, project_type, link) VALUES
('ExamNexus', 'A multi-tenant examination platform for universities handling 10k+ concurrent users with real-time results.', 'https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=500&q=60', 'IN_HOUSE', 'https://example.com'),
('Door2Cure', 'A modern pathology lab management system offering home sample collection and automated report generation in Bhubaneswar.', 'https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&fit=crop&w=500&q=60', 'ONGOING', 'https://door2cure.com'),
('BBM Dental', 'SEO-optimized website for Bibhuti Bhushan Memorial Centre, a premier NABH accredited dental clinic in Jaydev Vihar.', 'https://images.unsplash.com/photo-1588776814546-1ffcf4722e12?auto=format&fit=crop&w=500&q=60', 'ONGOING', 'https://bbmdental.com');


-- 11. Blog Posts (High Quality Content)
INSERT INTO main_blogpost (title, slug, category, image_url, excerpt, content, date_posted, meta_title, meta_description) VALUES
('The Future of AI in Web Development', 'future-of-ai-web-dev', 'Technology', 'https://images.unsplash.com/photo-1485827404703-89b55fcc595e?auto=format&fit=crop&w=500&q=60', 'How AI tools like ChatGPT and Copilot are changing the way we code forever.', 'Artificial Intelligence is not just a buzzword; it is rewriting the rules of software development. Tools like GitHub Copilot and ChatGPT are helping developers write code faster, while AI-driven UX design is personalizing user journeys in real-time.', NOW(), 'AI in Web Development | Agile Web', 'Learn how AI is revolutionizing web development workflows and improving efficiency.'),
('Why Your Business Needs a Mobile App', 'business-mobile-app', 'Business', 'https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?auto=format&fit=crop&w=500&q=60', 'Mobile traffic has surpassed desktop. Here is why you cannot afford to ignore mobile users.', 'In 2024, over 60% of all web traffic comes from mobile devices. Having a dedicated mobile app improves customer retention, allows for push notifications, and provides a smoother user experience than mobile websites.', NOW(), 'Mobile App Benefits | Agile Web', 'Discover why a mobile app is crucial for modern business growth and customer retention.');