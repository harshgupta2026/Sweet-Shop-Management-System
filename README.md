# Sweet-Shop-Management-System
TDD- based Sweet Shop Management System built as part of a Software Craftsperson internship assessment. 

Sweet Shop Management System

A full-stack Sweet Shop Management System built as part of an assignment to demonstrate backend API design, frontend integration, and CRUD operations with authentication and role-based access.

📌 Project Overview

This application allows users to view and purchase sweets, while admin users can manage the sweet inventory.
The system follows a modern SPA architecture with a React-based frontend and a FastAPI backend.

🛠 Tech Stack
Frontend

React (Single Page Application)

JavaScript (ES6)

Fetch API for backend communication

Backend

FastAPI (Python)

JWT-based Authentication

RESTful API design

JSON-based data storage (for simplicity)

✨ Features Implemented
👤 User Features

User registration and login

View all available sweets

Search and filter sweets

Purchase sweets (disabled when quantity is zero)

Admin Features

Update existing sweets

Delete sweets

Secure admin-only access to inventory management

🔗 Frontend – Backend Integration

Frontend communicates with backend using REST APIs

Backend endpoints serve data in JSON format

Role-based access ensures admin actions are protected

📂 Project Structure (Logical)

Due to submission time constraints, frontend and backend files are present at the root level.
Logically, the project follows this structure:
Sweet-Shop-Management-System/
│
├── frontend/   → React SPA (UI, dashboard, user interaction)
├── backend/    → FastAPI (APIs, auth, business logic)


---

# API Documentation (Swagger)

This project includes an interactive Swagger UI for exploring and testing the backend REST APIs.

# Swagger URL (Local)
http://127.0.0.1:8000/docs


> Note: Run the backend locally using FastAPI to access the Swagger documentation.

# Swagger Preview

(swagger.png)<img width="1366" height="768" alt="swagger" src="https://github.com/user-attachments/assets/0cabce5a-30c8-47e8-a790-4156e8125095" />


The Swagger UI provides complete visibility of all available endpoints including authentication, sweets management, inventory operations, and role-based access control.
