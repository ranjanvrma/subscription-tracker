# Subscription Tracker (MySQL + Python CLI)

This project is a command-line based Subscription Tracker built using Python and MySQL.

It allows users to manage personal subscriptions, track renewal dates, and monitor monthly spending.

The goal of this project is to:
- Design a relational database schema
- Implement SQL queries for real-world use cases
- Integrate MySQL with Python
- Build a structured CLI-based application
- Practice backend development fundamentals

---

## 📊 Problem Statement

Many users subscribe to multiple services (Netflix, Spotify, software tools, gym memberships, etc.) and lose track of:

- Monthly expenses
- Renewal dates
- Active vs cancelled subscriptions
- Yearly spending impact

This project solves that problem using a structured database system.

---

## 🗄 Database Design

### Table: `subscriptions`

| Column | Description |
|--------|------------|
| id | Unique subscription ID |
| name | Subscription name |
| category | Type (Streaming, Software, Gym, etc.) |
| cost | Subscription cost |
| billing_cycle | Monthly / Yearly |
| start_date | Subscription start date |
| next_renewal | Next renewal date |
| status | Active / Cancelled |

The `next_renewal` field is stored explicitly to support realistic billing scenarios.

---

## 🛠 Tech Stack

- Python  
- MySQL  
- mysql-connector-python  
- MySQL Workbench  
- VS Code  

---

## 📈 Features Implemented

- Add new subscription  
- View active subscriptions  
- Automatic next renewal calculation  
- Structured CLI menu system  
- MySQL backend integration  

---

## 🔄 Workflow

1. Create MySQL database and schema  
2. Connect Python to MySQL  
3. Implement insert and fetch operations  
4. Build menu-driven CLI system  
5. Commit structured project to GitHub  

---

## 🚀 Future Enhancements

- Monthly spending summary  
- Upcoming renewals alert (next 7 days)  
- Cancel subscription feature  
- Category-wise spending analysis  
- Budget limit warnings  
- Streamlit web interface  
- Spending prediction model (ML integration)  

---

## 📌 Setup Instructions

1. Install dependencies:
   ```bash
   pip install mysql-connector-python