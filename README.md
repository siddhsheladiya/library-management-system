Modular CLI Library Management System with Relational Database Integration

## Overview
The Library Management System (LMS) is a modular, command-line software solution integrated with a relational MySQL database. It automates core library workflows including book catalog management, tier-based lending quotas, loan duration tracking, and dynamic overdue fee computations. The project is built following a decoupled three-tier architecture separating the terminal presentation layer, domain business logic, and database persistence.

## Features
* **Catalog Management**: Stores and queries a diverse collection of 50 books with dynamic availability states (`Available` vs `Checked Out`).
* **Tier-Based Lending**: Supports three membership tiers—Silver (1 book, 14 days, ₹10/day fine), Gold (3 books, 21 days, ₹5/day fine), and Platinum (5 books, 30 days, fee waiver).
* **Automated Due Date & Quota Validation**: Checks active loan limits against membership perks before issuing a book and computes loan due dates automatically].
* **Late Fee Calculation Engine**: Compares return dates against due dates to determine overdue periods and assesses exact penalty amounts or waivers.
* **Patron Profiles & History**: Tracks transaction logs, active checkouts, return timestamps, and compensation notes per member.
* **Safe Database Operations**: Uses parameterized SQL queries to prevent SQL injection and transaction commits to guarantee ACID consistency.

## Technologies & Tools Used
* **Programming Language**: Python 3.9+
* **Database Engine**: MySQL Server 8.0
* **Database Connector**: `mysql-connector-python`
* **Testing Framework**: Python standard `unittest` 
* **User Interface**: Pure Command-Line Interface (CLI / Headless)
* **Version Control**: Git & GitHub


## Repository Structure
```text
library-management-system/
├── README.md               # Setup instructions, features, and documentation
├── statement.md            # Problem statement, scope, and target audience
├── requirements.txt        # Required Python packages
├── database.sql            # Schema definitions and initial 50-book dataset
├── main.py                 # CLI interface and main application execution loop
│
├── database/
│   ├── __init__.py         # Package identifier[cite: 2]
│   └── connection.py       # MySQL database connection handler
│
├── models/
│   ├── __init__.py         # Package identifier[cite: 2]
│   ├── book.py             # Catalog querying and availability toggling
│   ├── membership.py       # Membership tiers, perks, and upgrades
│   └── borrower.py         # Book checkout, check-in, and fine processing
│
└── tests/
    ├── __init__.py         # Package identifier[cite: 2]
    └── test_library.py     # Automated unit test suite





## Steps to Install & Run

### 1. Prerequisites
- Python 3.9+ installed
- MySQL Server installed and running locally

### 2. Clone the Repository
```bash
git clone [https://github.com/siddhsheladiya/library-management-system.git](https://github.com/siddhsheladiya/library-management-system.git)
cd library-management-system
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup
Import the database schema and 50-book dataset:
```bash
mysql -u root -p < database.sql
```

### 5. Run the Application
```bash
python main.py
```
