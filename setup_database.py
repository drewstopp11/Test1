#!/usr/bin/env python3
"""Script to set up database tables and load seed data"""

import pymysql
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database configuration
config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME'),
    'port': int(os.getenv('DB_PORT', 3306))
}

def execute_sql_file(cursor, filepath):
    """Execute SQL statements from a file"""
    with open(filepath, 'r') as f:
        sql_content = f.read()

    # Remove comments and split by semicolon
    lines = []
    for line in sql_content.split('\n'):
        line = line.strip()
        if line and not line.startswith('--'):
            lines.append(line)

    sql_content = ' '.join(lines)
    statements = sql_content.split(';')

    for statement in statements:
        statement = statement.strip()
        if statement:
            cursor.execute(statement)

def main():
    print("Connecting to database...")
    connection = pymysql.connect(**config)

    try:
        cursor = connection.cursor()

        # Drop existing tables if they exist
        print("Dropping existing tables if they exist...")
        cursor.execute("DROP TABLE IF EXISTS tasks")
        cursor.execute("DROP TABLE IF EXISTS projects")
        cursor.execute("DROP TABLE IF EXISTS books")
        cursor.execute("DROP TABLE IF EXISTS authors")
        cursor.execute("DROP TABLE IF EXISTS sample_table")
        connection.commit()
        print("✓ Existing tables dropped")

        # Execute schema
        print("Creating tables from schema.sql...")
        execute_sql_file(cursor, 'database/schema.sql')
        connection.commit()
        print("✓ Tables created successfully")

        # Execute seed data
        print("Loading seed data from seed_data.sql...")
        execute_sql_file(cursor, 'database/seed_data.sql')
        connection.commit()
        print("✓ Seed data loaded successfully")

        # Verify data
        cursor.execute("SELECT COUNT(*) FROM projects")
        project_count = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM tasks")
        task_count = cursor.fetchone()[0]

        print(f"\nDatabase setup complete!")
        print(f"- Projects: {project_count}")
        print(f"- Tasks: {task_count}")

    except Exception as e:
        print(f"Error: {e}")
        connection.rollback()
        raise
    finally:
        cursor.close()
        connection.close()

if __name__ == '__main__':
    main()
