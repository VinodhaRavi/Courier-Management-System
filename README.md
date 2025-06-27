# 📦 Courier Management System

A simple console-based Courier Management System built in **Python** using **Object-Oriented Programming (OOP)** and **MySQL database integration**.

This project was developed as part of an academic assignment to demonstrate key programming concepts across the following areas:
- OOP (Classes, Abstraction, Encapsulation)
- Interface design using abstract classes
- Exception handling
- Collections (Lists)
- MySQL database interaction

---

## 📁 Project Structure
courier_mgmt/
│
├── entity/ # Entity (model) classes
│ ├── user.py
│ ├── courier.py
│ ├── employee.py
│ ├── payment.py
│ ├── location.py
│ ├── courier_company.py
│ └── courier_company_collection.py
│
├── service/ # Service interfaces & implementations
│ ├── courier_user_service.py
│ ├── courier_admin_service.py
│ ├── courier_user_service_impl.py
│ ├── courier_admin_service_impl.py
│ ├── courier_user_service_coll_impl.py
│ └── courier_admin_service_coll_impl.py
│
├── db/ # Database connection and DAO
│ ├── db_connection.py
│ ├── courier_service_db.py
│ └── db.properties
│
├── exception/ # Custom exceptions
│ ├── tracking_number_not_found.py
│ └── invalid_employee_id.py
│
├── main.py # CLI driver for demo/testing
└── README.md # You're here!

---

## ✅ Features

- 📦 **Place new courier orders** with automatic tracking number generation  
- 🚚 **Check order status** by tracking number  
- ❌ **Cancel an order**  
- 👨‍💼 **Add courier staff** via admin service  
- 🧾 Store data to **MySQL database** (`CourierManagementdb`)  
- 🧯 Gracefully handle **missing tracking numbers or invalid employee IDs**  
- 💾 Dynamic in-memory **lists** and persistent **database storage**  

---

## 💽 Database Setup (MySQL)

1. Make sure MySQL is installed and running.
2. Create a database called:
   ```sql
   CREATE DATABASE CourierManagementdb;
Update your connection credentials in:

bash
db/db.properties
example :
[mysql]
host     = localhost
port     = 3306
user     = root
password = your_password
database = CourierManagementdb

On first run, required tables (courier, payment) are created automatically.

▶️ How to Run
Clone or download the project.

Install required package:

bash
pip install mysql-connector-python
Run the application:

bash
python main.py
Use the menu to:

Place courier orders

Track status

Exit safely

📌 Technologies Used
Python 3.x

MySQL

*mysql-connector-python
*Object-Oriented Design
*Abstract Classes (Interfaces)
*Custom Exceptions
*Console Menu System

📚 Learning Outcomes
✔ Encapsulation using private variables
✔ Class design with constructors, setters, getters
✔ Abstract method implementation
✔ Custom error handling
✔ Basic use of collections and SQL integration
✔ Project modularization and package structuring

🧑‍💻 Author
Vinodha Ravi
Created for academic assignment and OOP learning
Hexaware Technologies - Python MySQL Module

📎 License
This project is free to use for learning and educational purposes.
