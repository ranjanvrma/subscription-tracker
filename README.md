# Subscription Tracker (Python + MySQL CLI)

A command-line based Subscription Tracker built using Python and MySQL to manage and analyze personal subscription data.

---

## 📌 Overview

This project allows users to store, manage, and track their subscriptions efficiently using a structured database system.

It focuses on **backend development, database design, and data handling**, making it relevant for data analytics and software development roles.

---

## 🎯 Objectives

* Design and implement a relational database schema
* Perform SQL-based CRUD operations
* Integrate Python with MySQL
* Build a structured CLI-based application
* Practice real-world data handling and backend logic

---

## 📊 Problem Statement

Users often subscribe to multiple services (Netflix, Spotify, software tools, gym memberships, etc.) and lose track of:

* Total spending
* Renewal dates
* Active subscriptions
* Unused subscriptions

This project helps organize subscription data and provides a centralized system for managing it.

---

## 🗄 Database Schema

### Table: `subscriptions`

| Column        | Description                           |
| ------------- | ------------------------------------- |
| id            | Primary key (AUTO_INCREMENT)          |
| name          | Subscription name                     |
| category      | Type (Streaming, Software, Gym, etc.) |
| cost          | Subscription cost                     |
| billing_cycle | Monthly / Yearly                      |
| start_date    | Subscription start date               |
| next_renewal  | Next renewal date                     |

---

## 🛠 Tech Stack

* Python
* MySQL
* mysql-connector-python
* Git & GitHub
* VS Code

---

## 🚀 Current Features (v1.0.0)

* Add new subscriptions
* View all subscriptions
* Remove subscriptions
* Automatic renewal date calculation
* Input validation for cost and billing cycle
* MySQL database integration
* Menu-driven CLI interface

---

## 🔄 Project Workflow

1. Design database schema in MySQL
2. Establish Python–MySQL connection
3. Execute SQL queries for data operations
4. Process user input through CLI
5. Display structured subscription data

---

## 📈 Planned Enhancements (v1.1.0+)

* Monthly spending summary (SQL aggregation)
* Category-wise expense analysis
* Upcoming renewal alerts
* CSV export using Pandas
* Data visualization (Matplotlib)
* Web dashboard (Streamlit)

---

## ⚙️ Setup Instructions

### 1️⃣ Install dependencies

```
pip install mysql-connector-python
```

### 2️⃣ Setup database

Run the SQL schema file:

```
schema.sql
```

### 3️⃣ Configure database connection

Update credentials in:

```
db.py
```

### 4️⃣ Run the application

```
python main.py
```

---

## 🧠 Key Learnings

* Writing and executing SQL queries (CRUD operations)
* Designing relational databases
* Integrating Python with MySQL
* Handling structured data in applications
* Building CLI-based systems

---

## 🏷 Version

Current Version: **v1.0.0**

---

## 👤 Author

Ranjan Verma
B.Tech Artificial Intelligence & Machine Learning