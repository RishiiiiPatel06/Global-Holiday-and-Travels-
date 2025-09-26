# db.py
import psycopg2
import psycopg2.extras
import streamlit as st

def get_connection():
    conn = psycopg2.connect(
        host=st.secrets["DB_HOST"],
        database=st.secrets["DB_NAME"],
        user=st.secrets["DB_USER"],
        password=st.secrets["DB_PASS"],
        port=st.secrets["DB_PORT"],
        sslmode="require"
    )
    return conn

def create_tables():
    conn = get_connection()
    cur = conn.cursor()

    # Users table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id SERIAL PRIMARY KEY,
        email VARCHAR(255) UNIQUE NOT NULL,
        password_hash VARCHAR(255) NOT NULL
    );
    """)

    # Contacts table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        contact_id SERIAL PRIMARY KEY,
        full_name VARCHAR(150) NOT NULL,
        contact_number VARCHAR(15) NOT NULL,
        email VARCHAR(255) NOT NULL,
        linkedin_account VARCHAR(255),
        github_account VARCHAR(255),
        message TEXT
    );
    """)

    # Feedback table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS feedbacks (
        feedback_id SERIAL PRIMARY KEY,
        name VARCHAR(150) NOT NULL,
        email VARCHAR(255) NOT NULL,
        feedback TEXT NOT NULL,
        rating NUMERIC(2,1) CHECK (rating >= 0 AND rating <= 5)
    );
    """)

    conn.commit()
    cur.close()
    conn.close()
