# ServiceScheduler

A web application built using **Django** that allows users to schedule services, manage appointments, and streamline booking processes efficiently.

## 🚀 Features
- User Authentication System (Login/Signup)
- Service Booking with Date and Time Selection
- Admin Panel for Managing Appointments
- Email Notifications for Booking Confirmations
- Responsive Design for Better User Experience

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/ServiceScheduler.git
cd ServiceScheduler
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (Admin Access)
```bash
python manage.py createsuperuser
```

### 6. Run the Server
```bash
python manage.py runserver
```

### 7. Access the Website
- [Click-Here](https://fckutony.pythonanywhere.com/)

## 📋 Configuration

Ensure you set the following environment variables in your `.env` file:
```
SECRET_KEY=your_django_secret_key
DEBUG=True
DATABASE_URL=your_database_url
EMAIL_HOST=your_email_host
EMAIL_PORT=your_email_port
EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_email_password
```

## 🖥️ Usage
1. Users can sign up and log in to manage their bookings.
2. Admin can log in to manage service records and appointments.
3. Booking confirmation emails are automatically sent to users.

## 🧑‍💻 Technologies Used
- **Django** (Backend Framework)
- **HTML/CSS/Bootstrap** (Frontend)
- **SQLite** (Database)
- **Email Services** for notifications



## 📧 Contact
For inquiries or collaboration opportunities, reach out via:
- Email: [sidhusidharth7075@gmail.com](mailto:sidhusidharth7075@gmail.com)
- LinkedIn: [LohithSappa](https://www.linkedin.com/in/lohith-sappa-aab07629a/)

---
⭐ Don't forget to **star** this repository if you found it helpful!

