# 🚀 LeetTrack

A full-stack web application that helps users track their coding practice, organize solved problems, and visualize their progress through an interactive dashboard.

🌐 **Live Demo:** https://leettrack-p27k.onrender.com

---

## 📖 About

LeetTrack is designed for students and developers preparing for coding interviews. Users can securely create an account, log in, record solved coding problems, and monitor their progress using visual analytics.

---

## ✨ Features

- 🔐 User Authentication (Register & Login)
- 🔒 Secure password hashing using Werkzeug
- ➕ Add coding problems
- ✏️ Edit problem details
- 🗑️ Delete problems
- 📋 View all solved problems
- 📊 Dashboard with statistics
- 📈 Interactive Charts using Chart.js
- 🗃️ PostgreSQL Database
- 🌐 Live Deployment on Render

---

# 🛠 Tech Stack

### Frontend
- HTML5
- CSS3
- Jinja2
- Chart.js

### Backend
- Python
- Flask
- Flask-SQLAlchemy

### Database
- PostgreSQL

### Deployment
- Render
- GitHub

---

# 📂 Project Structure

```text
leettrack/
│
├── assets/
│   └── images/
│       ├── homepage1.png
│       ├── homepage2.png
│       ├── homepage3.png
│       ├── homepage4.png
│       ├── login.png
│       ├── register.png
│       ├── dashboard.png
│       ├── add_problems.png
│       └── problems.png
│
├── static/
│   ├── css/
│   └── js/
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── add_problems.html
│   ├── problems.html
│   └── analytics.html
│
├── app.py
├── config.py
├── database.py
├── models.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📸 Application Screenshots

## 🏠 Home Page

![Home Page](assets/images/homepage1.png)

![Home Page](assets/images/homepage2.png)

![Home Page](assets/images/homepage3.png)

![Home Page](assets/images/homepage4.png)

---

## 🔐 Login Page

![Login](assets/images/login.png)

---

## 📝 Register Page

![Register](assets/images/register.png)

---

## 📊 Dashboard

![Dashboard](assets/images/dashboard.png)

---

## ➕ Add Problem

![Add Problem](assets/images/add_problems.png)

---

## 📋 Problems

![Problems](assets/images/problems.png)

---

# ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/biyalhimani/leetTrack.git
```

Move into the project directory

```bash
cd leetTrack
```

Install dependencies

```bash
pip install -r requirements.txt
```

Configure your PostgreSQL database in `config.py`:

```python
DATABASE_URL= postgresql://leettrack_user:dPtOzCYp0dSKXAEd2aN2E4IWyYdDNU0b@dpg-d97uh9pkh4rs73dk4if0-a.singapore-postgres.render.com/leettrack
```

Run the application

```bash
python app.py
```

Visit

```
http://127.0.0.1:5000
```

---

# 📊 Future Improvements

- Search and filter problems
- Difficulty-wise analytics
- Coding streak tracker
- User profile page
- Dark mode
- Export progress as CSV/PDF

---

# 📚 What I Learned

During this project, I gained practical experience with:

- Flask application development
- SQLAlchemy ORM
- PostgreSQL integration
- Authentication and session management
- CRUD operations
- Chart.js data visualization
- Git & GitHub workflow
- Deploying full-stack applications on Render

---

# 👩‍💻 Author

**Himani Biyal**

GitHub: https://github.com/biyalhimani

LinkedIn: https://www.linkedin.com/in/himanibiyal/

---

# ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub!