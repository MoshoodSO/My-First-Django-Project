# My First Django Project

This is my first hands-on project using the Django web framework. It demonstrates the basic structure of a Django project, including apps, views, models, and templates. The goal is to understand the fundamental concepts of Django web development.

---

## 🚀 Features

- ✅ Django project setup and configuration  
- ✅ Simple app with views and URL routing  
- ✅ Use of templates for dynamic HTML rendering  
- ✅ Basic understanding of models and database setup  
- ✅ Admin interface setup and usage

---

## 🛠️ Technologies Used

- **Python 3.x** - Programming language
- **Django** - Web framework
- **HTML & CSS** - Frontend markup and styling
- **SQLite** - Default Django database

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.x
- pip (Python package manager)

---

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/MoshoodSO/My-First-Django-Project.git
   cd My-First-Django-Project
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

---

## 🚀 Running the Project

1. **Start the development server**
   ```bash
   python manage.py runserver
   ```

2. **Access the application**
   - Open your browser and navigate to `http://127.0.0.1:8000/`

3. **Access the admin panel**
   - Navigate to `http://127.0.0.1:8000/admin/`
   - Use the superuser credentials to log in

---

## 📁 Project Structure

```
My-First-Django-Project/
├── manage.py              # Django project management script
├── requirements.txt       # Project dependencies
├── db.sqlite3             # SQLite database file
├── project_name/          # Main project directory
│   ├── __init__.py
│   ├── settings.py        # Project settings
│   ├── urls.py            # URL configuration
│   ├── asgi.py
│   └── wsgi.py
└── app_name/              # Django app directory
    ├── migrations/        # Database migrations
    ├── templates/         # HTML templates
    ├── models.py          # Database models
    ├── views.py           # View functions/classes
    ├── urls.py            # App URL routing
    ├── admin.py           # Admin configuration
    └── tests.py           # Test cases
```

---

## 📚 Learning Resources

- [Django Official Documentation](https://docs.djangoproject.com/)
- [Django for Beginners](https://django-for-beginners.readthedocs.io/)
- [Real Python Django Tutorials](https://realpython.com/tutorials/django/)

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository and submit a pull request with your improvements.

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**MoshoodSO** - [GitHub Profile](https://github.com/MoshoodSO)

---

## 📞 Support

If you have any questions or issues, feel free to open an issue on the [GitHub Issues](https://github.com/MoshoodSO/My-First-Django-Project/issues) page.

---

**Last Updated:** 2026-05-16
