
-- create a table for the user login and sign up detail store.
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- create a table for the save contact info. of users.
CREATE TABLE contacts (
    contact_id SERIAL PRIMARY KEY,
    full_name VARCHAR(150) NOT NULL,
    contact_number VARCHAR(15) NOT NULL,
    email_id VARCHAR(255) NOT NULL,
    linkedin_account TEXT,
    github_account TEXT,
    message TEXT,
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- create a table for save feedbacks.
CREATE TABLE feedbacks (
    feedback_id SERIAL PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    email_id VARCHAR(255) NOT NULL,
    feedback TEXT NOT NULL,
    rating NUMERIC(2,1) CHECK (rating >= 0 AND rating <= 5),
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


select * from users;
select * from contacts;
select * from feedbacks;

