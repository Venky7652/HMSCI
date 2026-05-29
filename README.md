# HMSCI
Hopital management System 
# Hospital Management System

## Project Description

Hospital Management System is a web-based application developed using PHP 5, Microsoft SQL Server, and Power BI.

The system helps manage:

- Patient Records
- Doctor Records
- Appointment Scheduling
- Billing Information
- Hospital Data Analysis
- Interactive Power BI Dashboard

---

## Technologies Used

- PHP 5
- HTML
- CSS
- JavaScript
- Microsoft SQL Server
- Power BI

---

## Software Requirements

Before running the project, install:

1. XAMPP (PHP 5 supported version)
2. Microsoft SQL Server
3. SQL Server Management Studio (SSMS)
4. Power BI Desktop

---

## Database Setup

### Step 1

Open SQL Server Management Studio (SSMS).

### Step 2

Create a database:

```sql
CREATE DATABASE HospitalDB;
```

### Step 3

Import the provided SQL file:

```
hospital.sql
```

### Step 4

Verify all tables are created successfully.

---

## Configure Database Connection

Open:

```php
db_connect.php
```

Update database credentials:

```php
$serverName = "localhost";
$database = "HospitalDB";
$username = "your_username";
$password = "your_password";
```

Save the file.

---

## Running the Project

### Step 1

Install XAMPP.

### Step 2

Copy project folder into:

```
xampp/htdocs/
```

Example:

```
xampp/htdocs/HospitalManagementSystem
```

### Step 3

Start:

- Apache
- SQL Server

### Step 4

Open browser:

```
http://localhost/HospitalManagementSystem
```

---

## Power BI Dashboard

### Step 1

Open:

```
HospitalDashboard.pbix
```

using Power BI Desktop.

### Step 2

Update SQL Server connection if needed.

### Step 3

Refresh data.

### Step 4

View reports and analytics.

---

## Project Structure

HospitalManagementSystem/

├── css/

├── js/

├── images/

├── database/

│ └── hospital.sql

├── dashboard/

│ └── HospitalDashboard.pbix

├── db_connect.php

├── index.php

└── README.md

---

## Author

Venkata Reddy Talla

B.Tech Project

Hospital Management System using PHP, Microsoft SQL Server, and Power BI
