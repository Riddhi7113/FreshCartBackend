
# **Grocery App Backend**

This is the backend for the Grocery App built using Django. It serves as the API layer, managing data, user authentication, and business logic for the application.

---

## **Features**

- **User Authentication**: 
  - Secure login and registration.
- **Grocery Management**: 
  - Add, update, delete, and fetch grocery items.
- **Category Management**: 
  - Categorize groceries for better organization.
- **Budget Tracking**: 
  - API endpoints for setting and retrieving user budgets.
- **Red Flagged Items**: 
  - Mark items exceeding the budget for client-side processing.
- **Responsive API**: 
  - Optimized for React Native frontend integration.

---

## **Installation**

### **Prerequisites**
Ensure the following are installed on your system:
- Python 3.8+
- pip (Python package manager)
- PostgreSQL (or your database of choice)

### **Setup Steps**

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd grocery-app-backend
   ```

2. **Create a Virtual Environment**
   ```bash
   python3 -m venv env
   source env/bin/activate  # Linux/Mac
   env\Scripts\activate     # Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the Database**
   - Update `DATABASES` in `settings.py` with your database credentials.
   - Example:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'grocery_db',
             'USER': 'your_username',
             'PASSWORD': 'your_password',
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }
     ```

5. **Apply Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

7. **Access the API**
   - API Root: `http://127.0.0.1:8000/api/`
   - Admin Panel: `http://127.0.0.1:8000/admin/`

---

## **API Endpoints**

| **Endpoint**             | **Method** | **Description**                     |
|---------------------------|------------|-------------------------------------|
| `/api/groceries/`         | GET        | Fetch all groceries.               |
| `/api/groceries/<id>/`    | GET        | Fetch a single grocery item.       |
| `/api/groceries/`         | POST       | Add a new grocery item.            |
| `/api/groceries/<id>/`    | PUT        | Update a grocery item.             |
| `/api/groceries/<id>/`    | DELETE     | Delete a grocery item.             |
| `/api/categories/`        | GET        | Fetch all categories.              |
| `/api/budget/`            | GET/POST   | Get or set user budget.            |

---

## **Folder Structure**

```
grocery-app-backend/
│
├── grocery_app/            # Main Django app
│   ├── migrations/         # Database migrations
│   ├── models.py           # Database models
│   ├── serializers.py      # API serializers
│   ├── views.py            # API views
│   ├── urls.py             # URL routes
│
├── grocery_project/        # Project settings
│   ├── settings.py         # Configuration
│   ├── urls.py             # Root URL routing
│
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
├── README.md               # Documentation
```

---

## **Contributing**

1. Fork the repository.
2. Create your feature branch:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add Your Feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/YourFeature
   ```
5. Submit a pull request.

---

## **License**

This project is licensed under the MIT License.
