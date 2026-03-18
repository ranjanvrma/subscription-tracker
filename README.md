# Subscription Tracker (MySQL + Python CLI)

This project is a command-line based Subscription Tracker built using Python and MySQL.

It allows users to manage personal subscriptions, track renewal dates, and monitor subscription details through a simple CLI interface.

The goal of this project is to:
- Design a relational database schema
- Implement SQL queries for real-world use cases
- Integrate MySQL with Python
- Build a structured CLI-based application
- Practice backend development fundamentals

---

## 📊 Problem Statement

Many users subscribe to multiple services (Netflix, Spotify, software tools, gym memberships, etc.) and often lose track of:

- Monthly expenses
- Renewal dates
- Active subscriptions
- Unused subscriptions that still charge money

This project helps users organize and manage subscriptions using a structured database system.

---

## 🗄 Database Design

### Table: `subscriptions`

| Column | Description |
|------|-------------|
| id | Unique subscription ID |
| name | Subscription name |
| category | Type (Streaming, Software, Gym, etc.) |
| cost | Subscription cost |
| billing_cycle | Monthly / Yearly |
| start_date | Subscription start date |
| next_renewal | Next renewal date |

The `next_renewal` field is stored explicitly to support easier renewal tracking.

---

## 🛠 Tech Stack

- Python
- MySQL
- mysql-connector-python
- MySQL Workbench
- VS Code

---

## 📈 Features Implemented

- Add a new subscription
- View all subscriptions
- Remove a subscription
- Automatic next renewal date calculation
- Menu-driven CLI interface
- MySQL database integration
- Input validation for user entries

---

## 🔄 Project Workflow

1. Create MySQL database and schema
2. Connect Python to MySQL using `mysql-connector`
3. Implement SQL queries for inserting, deleting, and retrieving data
4. Build a CLI menu system for user interaction
5. Structure project for GitHub with proper documentation

---

## 🚀 Future Enhancements

- Monthly spending summary
- Upcoming renewal alerts (next 7 days)
- Category-wise spending analysis
- Budget tracking
- Streamlit web dashboard
- Machine learning model for spending prediction

---

## 📌 Setup Instructions

### 1️⃣ Install dependencies

```
pip install mysql-connector-python
```

### 2️⃣ Create the database

Run the SQL file provided in `schema.sql` using MySQL Workbench.

### 3️⃣ Update database credentials

Edit `db.py` with your MySQL username and password.

### 4️⃣ Run the application

```
python main.py
```
---
## 👤 Author

Ranjan Verma | B.Tech Artificial Intelligence & Machine Learning
