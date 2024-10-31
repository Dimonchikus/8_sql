import mysql.connector
from mysql.connector import Error
from faker import Faker
import random
import os


def create_connection():
    connection = None
    retries = 5
    for attempt in range(retries):
        try:
            connection = mysql.connector.connect(
                host=os.getenv('DB_HOST', 'localhost:3306'),
                user=os.getenv('DB_USER', 'testuser'),
                password=os.getenv('DB_PASSWORD', 'testpassword'),
                database=os.getenv('DB_NAME', 'testdb')
            )
            if connection.is_connected():
                print("Connection to MySQL DB successful")
                return connection
        except Error as e:
            print(f"Attempt {attempt + 1}/{retries} failed: {e}")
    raise Exception("Failed to connect to MySQL after multiple attempts.")

def insert_users(connection, batch_size=10000):
    """Insert users into the database in batches"""
    cursor = connection.cursor()
    faker = Faker()
    total_users = 40_000_000

    insert_query = """
    INSERT INTO users (name, email, date_of_birth)
    VALUES (%s, %s, %s)
    """

    for i in range(0, total_users, batch_size):
        users = []
        for _ in range(batch_size):
            name = faker.name()
            email = faker.email()
            date_of_birth = faker.date_of_birth(minimum_age=18, maximum_age=90)
            users.append((name, email, date_of_birth))

        cursor.executemany(insert_query, users)
        connection.commit()
        print(f"Inserted {i + batch_size} users")

    print("Insertion complete")

def main():
    connection = create_connection()
    if connection:
        insert_users(connection)
        connection.close()

if __name__ == "__main__":
    main()