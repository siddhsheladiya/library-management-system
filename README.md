Modular CLI Library Management System with Relational Database Integration

## Overview
The Library Management System (LMS) is a modular, command-line software solution integrated with a relational MySQL database[cite: 2, 3, 10]. It automates core library workflows including book catalog management, tier-based lending quotas, loan duration tracking, and dynamic overdue fee computations[cite: 3, 10]. The project is built following a decoupled three-tier architecture separating the terminal presentation layer, domain business logic, and database persistence[cite: 2, 10].

## Features
* **Catalog Management**: Stores and queries a diverse collection of 50 books with dynamic availability states (`Available` vs `Checked Out`)[cite: 3, 10].
* **Tier-Based Lending**: Supports three membership tiers—Silver (1 book, 14 days, ₹10/day fine), Gold (3 books, 21 days, ₹5/day fine), and Platinum (5 books, 30 days, fee waiver)[cite: 3, 10].
* **Automated Due Date & Quota Validation**: Checks active loan limits against membership perks before issuing a book and computes loan due dates automatically[cite: 3, 10].
* **Late Fee Calculation Engine**: Compares return dates against due dates to determine overdue periods and assesses exact penalty amounts or waivers[cite: 3, 10].
* **Patron Profiles & History**: Tracks transaction logs, active checkouts, return timestamps, and compensation notes per member[cite: 3, 10].
* **Safe Database Operations**: Uses parameterized SQL queries to prevent SQL injection and transaction commits to guarantee ACID consistency[cite: 3, 10].

## Technologies & Tools Used
* **Programming Language**: Python 3.9+
* **Database Engine**: MySQL Server 8.0
* **Database Connector**: `mysql-connector-python`
* **Testing Framework**: Python standard `unittest` 
* **User Interface**: Pure Command-Line Interface (CLI / Headless)
* **Version Control**: Git & GitHub


## Repository Structure[cite: 2]
```text
library-management-system/
├── README.md               # Setup instructions, features, and documentation[cite: 2]
├── statement.md            # Problem statement, scope, and target audience[cite: 2]
├── requirements.txt        # Required Python packages[cite: 2]
├── database.sql            # Schema definitions and initial 50-book dataset[cite: 3]
├── main.py                 # CLI interface and main application execution loop[cite: 3]
│
├── database/
│   ├── __init__.py         # Package identifier[cite: 2]
│   └── connection.py       # MySQL database connection handler[cite: 3]
│
├── models/
│   ├── __init__.py         # Package identifier[cite: 2]
│   ├── book.py             # Catalog querying and availability toggling[cite: 3]
│   ├── membership.py       # Membership tiers, perks, and upgrades[cite: 3]
│   └── borrower.py         # Book checkout, check-in, and fine processing[cite: 3]
│
└── tests/
    ├── __init__.py         # Package identifier[cite: 2]
    └── test_library.py     # Automated unit test suite[cite: 2, 10]
