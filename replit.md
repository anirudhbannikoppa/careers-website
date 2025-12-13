# Careers Website

A Flask-based careers/job listing website.

## Overview

This is a simple web application that displays job listings. Users can browse available positions and view job details.

## Project Structure

```
/
├── app.py              # Main Flask application
├── templates/          # Jinja2 HTML templates
│   ├── home.html       # Homepage with job listings
│   └── job.html        # Individual job detail page
├── static/             # Static assets
│   └── style.css       # Stylesheet
├── pyproject.toml      # Python dependencies
└── README.md           # Project description
```

## Running the Application

The application runs on port 5000:

```bash
python app.py
```

## Technologies

- Python 3.11
- Flask 3.x
- Jinja2 templating
