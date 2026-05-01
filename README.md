# 🛒 E-Commerce Backend API (Django + DRF)

A scalable backend system for an e-commerce platform built using Django and Django REST Framework.
This project demonstrates REST API design, authentication, authorization, and core business logic.

---

## 🚀 Features

* 🔐 JWT Authentication (Login / Register)
* 👥 Role-Based Access Control (Admin / Customer)
* 📦 Product Management (CRUD APIs)
* 🛒 Order Management System
* 💰 Automatic Total Price Calculation
* 📉 Stock Management on Order Placement
* 📄 Pagination Support
* 🔍 Product Filtering
* 🔒 Atomic order processing with transaction management
* 🛑 Prevents overselling using row-level locking (select_for_update)

---

## 🛠 Tech Stack

* Python
* Django
* Django REST Framework
* MySQL
* JWT Authentication

---

## 📁 Project Structure

```
ecommerce_backend/
│
├── users/        # User authentication & roles
├── products/     # Product APIs
├── orders/       # Order & business logic
├── ecommerce_backend/
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
└── requirements.txt
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/shivakrishna-devloper/ecommerce-backend-django.git
cd ecommerce-backend-django
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\\Scripts\\activate   # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure database (MySQL)

Update `settings.py` with your DB credentials.

---

### 5. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 6. Start server

```bash
python manage.py runserver
```

---

## 🔐 Authentication Flow

1. Register user → `/api/auth/register/`
2. Login → `/api/token/`
3. Use token in header:

```
Authorization: Bearer <your_token>
```

---

## 📡 API Endpoints

### 🔹 Authentication

* POST `/api/auth/register/`
* POST `/api/token/`

---

### 🔹 Products

* GET `/api/products/`
* POST `/api/products/` (Admin only)
* PUT `/api/products/{id}/` (Admin only)
* DELETE `/api/products/{id}/` (Admin only)

---

### 🔹 Orders

* POST `/api/orders/`
* GET `/api/orders/`

---

## 🧠 Key Concepts Implemented

* Django Model Relationships (ForeignKey)
* Nested Serializers
* Custom Permissions
* JWT Authentication
* Business Logic in Serializer (Order creation)
* Pagination & Filtering

---

## ⚠️ Limitations / Improvements

* User ID is passed manually in orders (can use `request.user`)
* No payment gateway integration
* Basic validation (can be enhanced)

---

## 📌 Future Enhancements

* Payment integration (Stripe / Razorpay)
* Docker deployment
* API documentation (Swagger)
* Caching with Redis

---


