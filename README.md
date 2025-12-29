# 🎓 Student Management System (Python CLI)

A simple **Student Management System** built with Python.  
This project focuses on core Python syntax, clean structure, and basic backend-style logic.

---

## 🚀 Features

- Add, update, and delete students
- Store student data persistently using JSON
- Automatic ID generation
- Case-insensitive student lookup
- Score validation (0–100)
- Pass / Fail status calculation
- Statistics report:
  - Average score
  - Maximum score
  - Minimum score
  - Number of passed students

---

## 🧱 Project Structure

```
student-management/
├── app.py              # CLI application (menu, input/output)
├── students_data.json   # Persistent data storage (JSON)
└── README.md            # Project documentation
```

---

## 🛠 Technologies Used

- Python 3
- JSON (for data persistence)
- No external libraries required.

---

## ▶️ How to Run the Application

1. Clone the repository:

```bash
  git clone https://github.com/azizbekpyd/student-management.git
```

Navigate to the project folder:

```bash
cd student-management
```

Run the application:

```bash
python app.py
```

📊 Example Menu

1. Add student
2. Update student score
3. Delete student
4. Show all students
5. Show statistics
6. Exit

🧠 Design Notes

Simple and beginner-friendly design

Focus on Python fundamentals

Uses file-based persistence (JSON)

Easy to extend with tests, database, or a web framework

🚀 Possible Improvements

Add unit tests using unittest or pytest

Separate business logic from CLI

Replace JSON with SQLite or PostgreSQL

Convert to REST API using FastAPI or Django

Improve input validation and error handling

👤 Author

Azizbek Kayratdinov |
Python Developer (Backend-focused) |
📍 Uzbekistan
