from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date
from app.models import Customer, Payment, Product, Order


def get_session():
    engine = create_engine('sqlite:///app/database.db')
    Session = sessionmaker(bind=engine)
    return Session()


def seed_data(session):
    session.query(Order).delete()
    session.query(Payment).delete()
    session.query(Product).delete()
    session.query(Customer).delete()

    customers = [
        Customer(first_name='John', last_name='Doe', address='123 Elm St', city='New York', state='NY', country='USA', zipcode='10001', phone_number='555-123-4567', email_id='john.doe@example.com'),
        Customer(first_name='Jane', last_name='Smith', address='456 Oak St', city='Los Angeles', state='CA', country='USA', zipcode='90001', phone_number='555-987-6543', email_id='jane.smith@example.com'),
        Customer(first_name='Emily', last_name='Clark', address='789 Pine St', city='Chicago', state='IL', country='USA', zipcode='60601', phone_number='555-456-7890', email_id='emily.clark@example.com'),
    ]
    session.bulk_save_objects(customers)

    payments = [
        Payment(customer_id=1, payment_type='Credit Card', expiration_date=date(2025, 12, 31), email_id='john.doe@example.com'),
        Payment(customer_id=2, payment_type='PayPal', expiration_date=date(2026, 6, 30), email_id='jane.smith@example.com'),
        Payment(customer_id=3, payment_type='Debit Card', expiration_date=date(2025, 11, 30), email_id='emily.clark@example.com'),
    ]
    session.bulk_save_objects(payments)

    products = [
        Product(product_name='Wireless Mouse', product_type='Electronics', price=25.99),
        Product(product_name='Bluetooth Speaker', product_type='Electronics', price=50.00),
    ]
    session.bulk_save_objects(products)

    orders = [
        Order(product_id=1, customer_id=1, payment_id=1, shipping_address='123 Elm St', shipping_city='New York', shipping_state='NY', shipping_country='USA', delivered=False),
        Order(product_id=2, customer_id=2, payment_id=2, shipping_address='456 Oak St', shipping_city='Los Angeles', shipping_state='CA', shipping_country='USA', delivered=False),
        Order(product_id=1, customer_id=3, payment_id=3, shipping_address='789 Pine St', shipping_city='Chicago', shipping_state='IL', shipping_country='USA', delivered=False),
    ]
    session.bulk_save_objects(orders)

    session.commit()
    print("✅ Database seeded successfully!")


if __name__ == "__main__":
    session = get_session()
    try:
        seed_data(session)
    finally:
        session.close()
