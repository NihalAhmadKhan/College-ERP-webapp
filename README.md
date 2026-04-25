# College ERP Web Application

A comprehensive Enterprise Resource Planning (ERP) system for **IEC College of Engineering and Technology**, Greater Noida. The application provides separate portals for students, faculty, and administrators to manage academic operations.

## Tech Stack

| Component | Technology |
|-----------|------------|
| Backend | Python Flask |
| Database | MySQL |
| Templating | Jinja2 |
| PDF Generation | pdfkit + wkhtmltopdf |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Icons | Font Awesome (CDN) |
| Fonts | Google Fonts (Poppins) |

## Features

### Student Portal
- Login with Roll Number and Password
- Dashboard with course info, attendance, and subjects
- View personal profile and enrollment details
- Check attendance records
- Download Admit Cards (PDF)
- View examination results
- Registration form access

### Faculty Portal
- Login with Username and Password
- Dashboard with faculty ID and department info
- Profile management
- Upload student attendance
- Manage lecture schedules
- Upload student marks

### Admin Portal
- Dashboard overview
- Student records management
- Faculty records management
- Lectures management
- Admission request processing
- Registration request processing

### Admission Portal
- Full admission form with personal details
- Guardian/parent information
- Academic history (10th and 12th)
- Course selection: B.Tech, B.Pharma, BCA, D.Pharma, MBA, M.Pharma, M.Tech, MCA
- Stream selection: EE, EC, ME, CE, CSE

### Registration Portal
- Continuing student registration
- Course and year selection

## Project Structure

```
College-ERP-webapp/
├── College ERP Portal/
│   ├── app.py                 # Main Flask application (entry point)
│   ├── static/
│   │   └── css/               # Stylesheets
│   │       ├── admission.css
│   │       ├── student.css
│   │       ├── styles.css
│   │       ├── ui.css
│   │       └── uix.css
│   └── templates/             # Jinja2 HTML templates
│       ├── join.html          # Home/landing page
│       ├── student.html       # Student login
│       ├── faculty.html       # Faculty login
│       ├── admin.html         # Admin login
│       ├── admission.html     # Admission form
│       ├── registration.html  # Registration form
│       ├── student-ui.html    # Student dashboard shell
│       ├── faculty-ui.html   # Faculty dashboard shell
│       ├── admin-ui.html      # Admin dashboard shell
│       └── *.html             # Various portal pages
└── README.md
```

## Setup

### Prerequisites

- Python 3.x
- MySQL Server
- wkhtmltopdf (for PDF generation)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/NihalAhmadKhan/College-ERP-webapp.git
   cd College-ERP-webapp/project
   ```

2. Install Python dependencies:
   ```bash
   pip install flask mysql-connector-python pdfkit
   ```

3. Install wkhtmltopdf:
   - **Windows**: Download from https://wkhtmltopdf.org/downloads.html
   - **Linux**: `sudo apt-get install wkhtmltopdf`
   - **macOS**: `brew install wkhtmltopdf`

4. Configure database connection in `app.py`:
   ```python
   db_config = {
       'host': 'localhost',
       'user': 'root',
       'password': 'your_password',
       'database': 'project'
   }
   ```

5. Update PDF path in `app.py`:
   ```python
   config = pdfkit.configuration(wkhtmltopdf=r'path/to/wkhtmltopdf')
   ```

6. Run the application:
   ```bash
   python app.py
   ```

7. Open `http://localhost:5000` in your browser

## Database Schema

The application uses the following main tables:
- `studentusers` - Student login credentials
- `studentprofile` - Student personal data
- `studentdata` - Student academic data
- `facultyusers` - Faculty login credentials
- `facultyprofile` - Faculty personal data
- `adminusers` - Admin login credentials
- `5semsubjects` - Semester subjects data

## Key Routes

| Route | Purpose |
|-------|---------|
| `/` | Home page |
| `/studentportal` | Student login |
| `/facultyportal` | Faculty login |
| `/adminportal` | Admin login |
| `/admissionportal` | Admission form |
| `/registrationportal` | Registration form |
| `/studentui/<username>` | Student dashboard |
| `/facultyui/<username>` | Faculty dashboard |
| `/adminui/<username>` | Admin dashboard |
| `/download-admitcard` | Generate and download admit card PDF |

## Notes

- The application uses server-side rendering with Flask routing
- PDF admit cards are generated using pdfkit and wkhtmltopdf
- Session-based authentication is used for all portals
- College name: IEC College of Engineering and Technology
- College address: Plot no. 4, Knowledge Park - 1, Greater Noida (UP), 201310

## License

This project is available for educational use.
