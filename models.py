import logging
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, String, Float, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Configure logging settings
logging.basicConfig(
    level=logging.INFO,
    filename='logs.log',
    filemode='a', 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

try:
    # Load environment variables from .env file
    logging.info("Loading environment variables...")
    load_dotenv()

    # Retrieve environment variables
    DB_USER = os.getenv('POSTGRES_USER')
    DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')
    DB_NAME = os.getenv('POSTGRES_DB')

    # Check if all necessary environment variables are set
    if None in [DB_USER, DB_PASSWORD, DB_NAME]:
        error_msg = "One or more environment variables are not set."
        logging.error(error_msg)
        raise ValueError(error_msg)
    
    logging.info("Environment variables loaded successfully.")

    # Database URL
    DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@localhost:5432/{DB_NAME}'
    logging.info("Connecting to the database...")

    # Create database engine
    ENGINE = create_engine(DATABASE_URL)
    logging.info("Database connection established.")

    # Create a configured "Session" class
    SessionLocal = sessionmaker(bind=ENGINE)

    # Base class for declarative class definitions
    Base = declarative_base()

    # Define the Product model class
    class Product(Base):
        __tablename__ = 'products'

        _id = Column(Integer, primary_key=True, autoincrement=True)
        name = Column(String, nullable=False)
        price = Column(Float, nullable=False)
        rating = Column(Float, nullable=True)
        review_count = Column(Integer, nullable=True)
        url = Column(String, nullable=False)
    
    logging.info("Model class 'Product' created.")

except OSError as os_error:
    error_msg = f'Error occurred while creating model: {os_error}. This is a system error and most likely not a problem with the script.'
    logging.error(error_msg)
    raise OSError(error_msg)

except ValueError as value_error:
    logging.error(f'Value error occurred: {value_error}')
    raise ValueError(value_error)

except ModuleNotFoundError as module_error:
    error_msg = f'Module not found: {module_error}\nPlease make sure all the modules are imported correctly [Hint: Use "pip install -r requirements.txt" in your terminal]'
    logging.error(error_msg)
    raise ModuleNotFoundError(error_msg)

except Exception as e:
    error_msg = f'An unexpected error occurred: {e}'
    logging.error(error_msg)
    raise Exception(error_msg)
