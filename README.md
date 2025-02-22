# 🛍️ E-commerce Database Management System

This project is designed to manage an e-commerce platform's backend database, facilitating customer management, product inventory, order processing, and payment handling. The system utilizes SQLAlchemy for ORM capabilities, allowing for efficient database interactions, and Alembic for handling database migrations.

## Key Features

1. **Customer Management**: 
   - Stores customer information including name, address, email, and phone number.
   - Supports relationships with orders and payments.

2. **Product Inventory**:
   - Maintains a catalog of products, including their names, types, and prices.
   - Integrates with an inventory system to track product quantities.

3. **Order Processing**:
   - Records customer orders linked to specific products and payment methods.
   - Manages shipping details and delivery status.

4. **Payment Handling**:
   - Records various payment methods for customers, including credit cards and PayPal.
   - Ensures data integrity with cascading deletions on customer or order removal.

5. **Database Migrations**:
   - Utilizes Alembic to manage schema changes over time, ensuring version control and ease of updates.

## Technologies Used

- **Python**: Programming language for backend development.
- **SQLAlchemy**: ORM for database interactions.
- **Alembic**: Migration tool for handling database schema changes.
- **SQLite**: Lightweight database for development and testing.

## Installation Instructions:

**1) Set Up a Virtual Environment (Optional but Recommended):**  
It's a good practice to use a virtual environment to manage dependencies. Run the following commands:
```bash
# On Mac and Linux
python3 -m venv venv
source venv/bin/activate 

# On Windows
python -m venv venv
venv\Scripts\activate
```

**2) Install Required Packages:**
```bash
pip install sqlalchemy alembic
```

**3) Set Up the Database:**

- For `SQLite`, the database file will be created automatically when you run the application.
- For `MySQL` or `PostgreSQL`, create a database using your preferred database management tool or run:
```bash
CREATE DATABASE your_database_name;
```

**4) Configure Alembic:** 
Initialize Alembic to set up the migration environment:
```bash
alembic init alembic
```

**5) Run Database Migrations:** Apply existing migration scripts to set up the database schema:
```bash
alembic upgrade <span style="color: yellow;">head</span>
```

**6) Start the Application:** 
Run the application:
```bash
python app.py
```
Or any other command relevant to your setup.

## SQLAlchemy and Alembic

**SQLAlchemy** is chosen for its powerful ORM capabilities that simplify database interactions and schema management. It supports multiple backends and allows for easy migration between different database systems. Key benefits include:

- **Object-Relational Mapping (ORM):** Interact with the database using Python objects, making code more readable and maintainable.
- **Schema Management:** Define database schemas with Python classes, integrating seamlessly with Alembic for migrations.
- **Query Building:** Construct complex queries programmatically without cumbersome SQL strings.
- **Community and Documentation:** A large, active community provides extensive support and resources.

Alembic complements SQLAlchemy by effectively managing database schema migrations, ensuring version control with migration histories. Its key advantages include:

- **Migration Management:** Simplifies applying incremental changes to the database schema.
- **Automatic Generation:** Generates migration scripts based on model changes, reducing human error.
- **Flexibility:** Accommodates both simple and complex changes in schema.

## SQLAlchemy Imports

Below are the necessary components imported from SQLAlchemy for building the ORM and managing database interactions:

| Import Statement | Description |
|------------------|-------------|
| `create_engine`  | Connects to the database. |
| `Column`         | Defines a column in the ORM model class. |
| `Integer`        | Specifies the data type for integer columns. |
| `String`         | Specifies the data type for string columns. |
| `ForeignKey`     | Establishes a foreign key relationship in the ORM model. |
| `declarative_base` | Creates a base class for ORM models, allowing the definition of database schemas. |
| `sessionmaker`   | A factory for creating new session objects for database interaction. |
| `relationship`   | Defines relationships between different ORM models. |
| `Session`        | Manages database transactions within a session. |


## Why Alembic?

**Alembic** handles database migrations efficiently and effectively. Here are the key reasons for using Alembic:

1. **Migration Management**:
   - Alembic is specifically designed for managing database schema migrations in SQLAlchemy projects. It simplifies the process of applying incremental changes to the database schema, ensuring that the database structure can evolve alongside the application.

2. **Version Control**:
   - Alembic allows for version control of database schemas, making it easy to track changes over time. Each migration is stored as a versioned file, which helps maintain a clear history of modifications and enables easy rollback to previous states if needed.

3. **Automatic Generation of Migrations**:
   - With Alembic, I can automatically generate migration scripts based on changes to my SQLAlchemy models. This feature saves time and reduces the risk of human error, as it ensures that the migration reflects the current state of the models.

4. **Flexibility**:
   - Alembic provides flexibility in defining migrations, allowing for both simple and complex changes. Whether adding new columns, modifying existing ones, or creating new tables, Alembic accommodates a wide range of schema adjustments.

5. **Integration with SQLAlchemy**:
   - Since Alembic is built to work seamlessly with SQLAlchemy, it fits naturally into the project’s architecture. This integration makes it easy to manage migrations and maintain consistency between the application code and the database schema.

## Important Alembic Commands

Below is a summary of key Alembic commands:

### 1. Initialize Alembic
```bash
alembic init <directory>
```
Run the following command to create a new Alembic environment.

### 2. Create a migration script
```bash
alembic revision -m "<message>"
```
Use this command to create a new migration script. Replace <message> with a descriptive message about the changes in this migration. This is typically done when you have made changes to your SQLAlchemy models that require a corresponding change in the database schema.

### 3. Generate Migration Script Automatically
```bash
alembic revision --autogenerate -m "<message>"
```
This command automatically generates a migration script based on changes detected in your SQLAlchemy models compared to the current database schema. Use this when you have made changes to your models and want Alembic to handle the migration generation.

### 4. Upgrade the Database
```bash
alembic upgrade <revision>
```
Use this command to apply the migration scripts to the database and upgrade it to a specific revision. If you want to apply all pending migrations, you can use `alembic upgrade head`.

### 5. Downgrade the Database
```bash
alembic downgrade <revision>
```
This command is used to revert the database schema to a previous revision. Use this if you need to undo changes made by a migration or if you encounter issues after an upgrade.

### 6. Show Current Revision
```bash
alembic current
```
Use this command to display the current database revision. This is helpful for understanding the state of the database schema before performing upgrades or downgrades.

### 7. History of Migrations
```bash
alembic history
```
This command shows the list of all migration revisions in the database. Use this command to view the history of migrations applied to your database.

### 8. Edit Migration Script
```bash
alembic edit <revision>
```

## Database Seeding

To seed the database with initial data, you can use the following Python code:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Customer, Payment, Product, Order

def get_session():
    engine = create_engine('sqlite:///app/database.db')  # Adjust the connection string for your database
    Session = sessionmaker(bind=engine)
    return Session()

def seed_data(session):
    # Clear existing data
    session.query(Order).delete()
    session.query(Payment).delete()
    session.query(Product).delete()
    session.query(Customer).delete()

    # Seed customers
    customers = [
        Customer(first_name='John', last_name='Doe', address='123 Elm St', city='New York', state='NY', country='USA', zipcode='10001', phone_number='555-123-4567', email_id='john.doe@example.com'),
        Customer(first_name='Jane', last_name='Smith', address='456 Oak St', city='Los Angeles', state='CA', country='USA', zipcode='90001', phone_number='555-987-6543', email_id='jane.smith@example.com'),
        Customer(first_name='Emily', last_name='Clark', address='789 Pine St', city='Chicago', state='IL', country='USA', zipcode='60601', phone_number='555-456-7890', email_id='emily.clark@example.com'),
    ]
    
    # Bulk save customer data
    session.bulk_save_objects(customers)

    # Commit the session
    session.commit()
    print("✅ Database seeded successfully!")

if __name__ == "__main__":
    session = get_session()
    try:
        seed_data(session)
    finally:
        session.close()
```

## Explanation
**Create an Engine and Session:** This code initializes a new SQLAlchemy engine and creates a session for interacting with the database.

**Define the Customers:** A list of new Customer objects is created with the required fields. You can adjust the values accordingly to represent the customer information you want to add.

**Bulk Add the Customers:** The `session.bulk_save_objects()` method is used to add multiple customers to the session at once.

**Commit the Session:** The `session.commit()` method saves all changes to the database in a single transaction.

**Output Confirmation:** A confirmation message is printed to the console showing how many customers have been successfully added.

**Close the Session:** The session is closed to free up resources.

## 🤝 Contributing
**Contributions are welcome! Please follow these steps:**

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Commit your changes (git commit -m "Added a new feature").
4. Push to the branch (git push origin feature-branch).
5. Open a Pull Request.















