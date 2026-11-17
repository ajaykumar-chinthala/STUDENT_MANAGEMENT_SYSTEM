# 🎓 Student Management System

A web-based **Student Management System** developed using Python, FastAPI, SQLite, HTML, and Jinja2. This application helps manage student information efficiently by providing features to add, view, update, and delete student records through a user-friendly interface.

## 🚀 Features

- **Add Students:** Register new students with details such as name, age, gender, marks, course, image, and status.
- **View Students:** Display all registered students.
- **Student Details:** View individual student information using their unique ID.
- **Update Students:** Edit and modify existing student records.
- **Delete Students:** Remove student records from the database.
- **Data Validation:** Validate student information using Pydantic.
- **Database Integration:** Store and manage student records using SQLite.
- **Dynamic Web Pages:** Render HTML pages using Jinja2 templates.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| FastAPI | Web framework |
| SQLite | Database management |
| HTML | Frontend structure |
| Jinja2 | Dynamic HTML templates |
| Pydantic | Data validation |

## 📂 Project Structure

```text
STUDENT_MANAGEMENT_SYSTEM/
│
├── templates/
│   ├── home.html
│   ├── add-std.html
│   ├── singlestd.html
│   └── update.html
│
├── main.py
├── students.db
├── LICENSE
└── README.md
```

## ⚙️ Installation and Setup

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/ajaykumar-chinthala/STUDENT_MANAGEMENT_SYSTEM.git
```

### 2. Navigate to the Project Directory

```bash
cd STUDENT_MANAGEMENT_SYSTEM
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

### 5. Install Required Dependencies

```bash
pip install fastapi uvicorn jinja2 python-multipart
```

### 6. Run the Application

```bash
uvicorn main:app --reload
```

### 7. Open in Browser

Visit the following URL:

```text
http://127.0.0.1:8000/
```

## 🔄 Application Operations

| Operation | Description |
|---|---|
| Create | Add new student records |
| Read | View all students and individual details |
| Update | Modify existing student information |
| Delete | Remove student records |

## 🗄️ Database Structure

The application uses an SQLite database named `students.db`.

**Students Table:**

| Column | Data Type |
|---|---|
| Id | INTEGER (Primary Key) |
| Name | TEXT |
| Age | INTEGER |
| Gender | TEXT |
| Marks | INTEGER |
| Course | TEXT |
| Image | TEXT |
| Status | INTEGER |

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Building web applications using FastAPI.
- Implementing CRUD operations.
- Connecting Python applications with SQLite.
- Handling HTML forms and HTTP requests.
- Validating input data using Pydantic.
- Integrating Jinja2 templates with backend functionality.
- Organizing backend logic and database operations.

## 👨‍💻 Author

**Chinthala Ajay Kumar**

- GitHub: [ajaykumar-chinthala](https://github.com/ajaykumar-chinthala)
- Project Repository: [Student Management System](https://github.com/ajaykumar-chinthala/STUDENT_MANAGEMENT_SYSTEM)

---

⭐ If you find this project useful, consider giving it a star!
