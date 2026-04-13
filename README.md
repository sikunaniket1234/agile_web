# Agile Web Agency Platform

A high-performance, premium Django-based agency website featuring glassmorphism design, a powerful blog engine, and technical service showcases.

## 🚀 Recent Major Updates
- **Stable Environment:** Migrated from Python 3.14 (experimental) to **Python 3.12 (Stable)**.
- **Blog Engine 2.0:**
  - Added dedicated `/blog/` list and detail pages.
  - Full **Markdown support** for articles (Headers, Bold, Links, Lists).
  - Internal **View Counter** and Author Attribution.
  - **Image Upload System:** Support for both external URL images and local file uploads with Admin previews.
- **Design Overhaul:**
  - Unified CSS Grid architecture (removed legacy float grids).
  - Recalibrated **Light Mode** (Soft Slate palette) for professional readability.
  - Optimized Hero Carousel and Pricing table UX.

## 🛠️ Setup Instructions (v3.12)
1. **Clone the repository:**
   ```bash
   git clone [your-repo-url]
   ```
2. **Create a Virtual Environment (Python 3.12 required):**
   ```bash
   py -3.12 -m venv venv_312
   source venv_312/Scripts/activate
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Environment Variables:**
   Ensure your `.env` file is configured with:
   - `DEBUG=True`
   - `SECRET_KEY=...`
   - `EMAIL_HOST_USER=...` (Optional for contact form)

5. **Run Migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Start Server:**
   ```bash
   python manage.py runserver
   ```

## 📂 Project Structure
- `main/`: Core application logic, models, and views.
- `main/templates/`: Optimized Django templates with custom components.
- `main/static/`: Premium CSS and Vanilla JS interactions.
- `media/`: Local storage for user-uploaded blog imagery (Git ignored).

## 🛑 Production Note
The `db.sqlite3` and `.env` are excluded from version control to prevent data corruption and security leaks. For production deployment, ensure `DEBUG=False` and set up a PostgreSQL database.
