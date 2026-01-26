document.addEventListener('DOMContentLoaded', function () {
    // 1. Init Animations
    AOS.init({ duration: 800, easing: 'ease-out', once: true });

    // 2. Init Materialize Components (Sidenav, Select, etc)
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems);
    
    var selectElems = document.querySelectorAll('select');
    M.FormSelect.init(selectElems);

    // 3. Theme Logic
    const html = document.documentElement;
    const savedTheme = localStorage.getItem('site-theme') || 'dark';
    html.setAttribute('data-theme', savedTheme);
    updateIcons(savedTheme);

    function toggleTheme(e) {
        e.preventDefault();
        const currentTheme = html.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        html.setAttribute('data-theme', newTheme);
        localStorage.setItem('site-theme', newTheme);
        updateIcons(newTheme);
    }

    function updateIcons(theme) {
        const iconName = theme === 'dark' ? 'light_mode' : 'dark_mode';
        const desktopIcon = document.querySelector('#theme-toggle i');
        const mobileIcon = document.querySelector('#theme-toggle-mobile i');
        if(desktopIcon) desktopIcon.textContent = iconName;
        if(mobileIcon) mobileIcon.textContent = iconName;
    }

    const desktopBtn = document.getElementById('theme-toggle');
    const mobileBtn = document.getElementById('theme-toggle-mobile');
    if(desktopBtn) desktopBtn.addEventListener('click', toggleTheme);
    if(mobileBtn) mobileBtn.addEventListener('click', toggleTheme);

    // 4. HERO CAROUSEL LOGIC (Fixed)
    // 4. HERO CAROUSEL LOGIC (With Dots)
    const heroCarouselEl = document.getElementById('hero-carousel');
    const dotsContainer = document.getElementById('hero-dots');

    if (heroCarouselEl && dotsContainer) {
        // 1. Generate Dots based on Slide Count
        const slides = heroCarouselEl.querySelectorAll('.carousel-item');
        dotsContainer.innerHTML = ''; // Clear existing
        
        slides.forEach((slide, index) => {
            const dot = document.createElement('div');
            dot.classList.add('dot');
            if (index === 0) dot.classList.add('active'); // First one active
            
            // Allow clicking dots to jump to slide
            dot.addEventListener('click', () => {
                heroInstance.set(index);
                stopAutoPlay(); // Pause auto-rotation if user interacts
            });
            
            dotsContainer.appendChild(dot);
        });

        // 2. Initialize Carousel with Callback
        const heroInstance = M.Carousel.init(heroCarouselEl, {
            fullWidth: true,
            indicators: false, // We use our own custom dots
            duration: 500,
            onCycleTo: function(currentSlide) {
                // Update active dot class
                const allDots = document.querySelectorAll('.dot');
                const slideIndex = [...slides].indexOf(currentSlide);
                
                allDots.forEach(d => d.classList.remove('active'));
                if (allDots[slideIndex]) {
                    allDots[slideIndex].classList.add('active');
                }
            }
        });

        // 3. Auto-Play Logic
        let autoPlayInterval = setInterval(() => { heroInstance.next(); }, 6000);

        function stopAutoPlay() {
            clearInterval(autoPlayInterval);
            // Restart after 10 seconds of inactivity
            autoPlayInterval = setInterval(() => { heroInstance.next(); }, 10000);
        }

        // 4. Global Control Functions
        window.moveHero = (direction) => {
            stopAutoPlay();
            if (direction === 'next') heroInstance.next();
            else heroInstance.prev();
        };
    }

    // 5. Smooth Scrolling
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            // Only scroll if it's NOT a carousel control
            if (!this.hasAttribute('onclick')) { 
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                // Close sidenav if open
                const sidenav = M.Sidenav.getInstance(document.querySelector('.sidenav'));
                if(sidenav && sidenav.isOpen) sidenav.close();

                if (target) {
                    window.scrollTo({
                        top: target.offsetTop - 70,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });
});