# 🛒 E-Commerce Backend API (Django + DRF)

A scalable backend system for an e-commerce platform built using Django and Django REST Framework.
This project demonstrates REST API design, authentication, authorization, and real-world business logic handling.

---

## 🚀 Features

* 🔐 JWT Authentication (Login / Register)
* 👥 Role-Based Access Control (Admin / Customer)
* 📦 Product Management (Full CRUD APIs)
* 🛒 Order Management System (Full CRUD APIs)
* 💰 Automatic Total Price Calculation
* 📉 Stock Management on Order Placement
* 🔒 Atomic Transactions & Row-Level Locking (Prevents overselling)
* 📄 Pagination Support
* 🔍 Product Filtering
* 📘 Swagger API Documentation

---

## 🛠 Tech Stack

* Python
* Django
* Django REST Framework
* MySQL
* JWT Authentication
* Postman (API Testing)
* Swagger (API Documentation)

---

## 📁 Project Structure

```bash
ecommerce_backend/
│
├── users/          # Authentication & user roles
├── products/       # Product management APIs
├── orders/         # Order processing & business logic
│
├── ecommerce_backend/
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
└── requirements.txt
```

---

## ⚙️ Setup Instructions

```bash
git clone https://github.com/shivakrishna-devloper/ecommerce-backend-django.git
cd ecommerce-backend-django

python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---

## 🔐 Authentication Flow

1. Register → `/api/auth/register/`
2. Login → `/api/token/`
3. Use token:

```http
Authorization: Bearer <your_access_token>
```

---

## 📡 API Endpoints

### 🔐 Authentication

* **POST** `/api/auth/register/` → Register user
* **POST** `/api/token/` → Get JWT token
* **POST** `/api/token/refresh/` → Refresh token

---

### 📦 Products (Admin-controlled write access)

* **GET** `/api/products/` → List all products
* **POST** `/api/products/` → Create product (Admin only)
* **GET** `/api/products/{id}/` → Get product details
* **PUT** `/api/products/{id}/` → Update product (Admin only)
* **PATCH** `/api/products/{id}/` → Partial update (Admin only)
* **DELETE** `/api/products/{id}/` → Delete product (Admin only)

---

### 🛒 Orders

* **GET** `/api/orders/` → List orders
* **POST** `/api/orders/` → Create order
* **GET** `/api/orders/{id}/` → Get order details
* **PUT** `/api/orders/{id}/` → Update order
* **PATCH** `/api/orders/{id}/` → Partial update
* **DELETE** `/api/orders/{id}/` → Delete order

---

### 🔍 Filtering Example

```bash
/api/products/?name=Phone
```

---

## 🧠 Key Concepts Implemented

* REST API Design
* JWT Authentication & Authorization
* Role-Based Access Control (RBAC)
* Django Model Relationships (ForeignKey)
* Nested Serializers
* Custom Permissions
* Pagination & Filtering
* Business Logic Handling in Serializer

---

## 🔒 Advanced Feature: Safe Order Processing

Implemented concurrency-safe order handling using:

* **Atomic Transactions (`transaction.atomic`)**
* **Row-Level Locking (`select_for_update`)**

### Benefits:

* Prevents race conditions
* Avoids overselling
* Ensures data consistency during concurrent requests

---

## ⚠️ Limitations

* Orders are not filtered per user (all users can view all orders)
* No payment gateway integration
* Limited validation for complex business rules
* No centralized logging or monitoring
* Not fully production-optimized deployment

---

## 📌 Future Enhancements

* Integrate payment gateway (Stripe / Razorpay)
* Implement user-specific order filtering
* Add centralized logging and monitoring
* Introduce caching (Redis)
* Deploy using Docker and cloud platforms (AWS / Render)
* Add API rate limiting and enhanced security
* Implement CI/CD pipeline

---

## 📘 API Documentation

Swagger UI:

```
http://127.0.0.1:8000/swagger/
```

---

## 👨‍💻 Author

**Shiva Krishna Koduri**
**GitHub:**(https://github.com/shivakrishna-devloper)

---
