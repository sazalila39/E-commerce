from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Customer, Product, Order, Payment

SQLALCHEMY_DATABASE_URL = "sqlite:///app/database.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_all_records(model):
    """Generic function to get all records from a given model."""
    db = SessionLocal()
    try:
        return db.query(model).all()
    except Exception as e:
        print(f"An error occurred while fetching {model.__tablename__}: {e}")
        return []
    finally:
        db.close()

def print_customers():
    customers = get_all_records(Customer)
    print("Customers:")
    for customer in customers:
        print(f"{customer.first_name} {customer.last_name} - {customer.email_id}")

def print_products():
    products = get_all_records(Product)
    print("Products:")
    for product in products:
        print(f"{product.product_name} - ${product.price:.2f}")

def print_orders():
    orders = get_all_records(Order)
    print("Orders:")
    for order in orders:
        print(f"Order ID: {order.id}, Product ID: {order.product_id}, Customer ID: {order.customer_id}")

def print_payments():
    payments = get_all_records(Payment)
    print("Payments:")
    for payment in payments:
        print(f"Payment ID: {payment.id}, Customer ID: {payment.customer_id}, Type: {payment.payment_type}")

def main():
    print_customers()
    print_products()
    print_orders()
    print_payments()

if __name__ == "__main__":
    main()
