import os

SECRET_KEY = os.getenv("SECRET")

DESCRIPTION = """
SmartWallet API is the server part of the application for storing money in different currencies in electronic form.
The API provides powerful financial and wallet management capabilities.
The API provides a secure and efficient way to interact with your wallet,
 opening up a wide range of financial management functions in your application or service.
"""

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")