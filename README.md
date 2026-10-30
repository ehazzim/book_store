# 📚 Book Store App (Practice)

A full-stack containerized web application built with Python (Flask) and PostgreSQL, configured for test-driven development (TDD) and deployed to an AWS EC2 instance using Docker Compose.

---

## 🎯 Goals & Architecture

* **Framework:** Flask
* **Database:** PostgreSQL
* **Containerization:** Docker
* **Testing:** Pytest & Playwright
* **Deployment:** AWS EC2 Cloud Instance

---

## 📂 Project Structure

```text
book_store/
├── lib/
│   ├── book_repository.py
│   ├── book.py
│   ├── user_repository.py
│   ├── user.py
│   └── database_connection.py
├── seeds/
│   ├── book_store.sql
│   └── book_store_test.sql
├── static/
│   └── styles.css
├── templates/
│   ├── index.html
│   ├── books.html
│   ├── users.html
│   ├── quotes.html
│   └── team.html
├── tests/
│   ├── test_app.py
│   ├── test_users.py
│   └── test_books.py
├── app.py
├── Dockerfile
└── requirements.txt