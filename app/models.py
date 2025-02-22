from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean, Date
from sqlalchemy.orm import relationship
from app.database import Base


class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    address = Column(String(200), nullable=True)
    city = Column(String(45), nullable=True)
    state = Column(String(45), nullable=True)
    country = Column(String(45), nullable=True)
    zipcode = Column(String(10), nullable=True)
    phone_number = Column(String(15), nullable=True)
    email_id = Column(String(100), unique=True, nullable=False)

    payments = relationship("Payment", back_populates="customer", cascade="all, delete")
    orders = relationship("Order", back_populates="customer", cascade="all, delete")


class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id", ondelete="CASCADE"), nullable=False)
    payment_type = Column(String(45), nullable=True)
    expiration_date = Column(Date, nullable=True)
    email_id = Column(String(100), nullable=True)

    customer = relationship("Customer", back_populates="payments")


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    product_name = Column(String(200), nullable=False)
    product_type = Column(String(45), nullable=True)
    price = Column(Float, nullable=False)

    orders = relationship("Order", back_populates="product", cascade="all, delete")
    inventory = relationship("Inventory", back_populates="product", cascade="all, delete")


class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id", ondelete="CASCADE"), nullable=False)
    payment_id = Column(Integer, ForeignKey("payments.id", ondelete="CASCADE"), nullable=False)
    shipping_address = Column(String(100), nullable=True)
    shipping_city = Column(String(100), nullable=True)
    shipping_state = Column(String(2), nullable=True)
    shipping_country = Column(String(45), nullable=True)
    delivered = Column(Boolean, default=False)

    customer = relationship("Customer", back_populates="orders")
    product = relationship("Product", back_populates="orders")
    payment = relationship("Payment")


class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)

    product = relationship("Product", back_populates="inventory")
