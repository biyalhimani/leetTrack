from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from config import Config
from database import db
from models import User, Problem

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)


# -------------------------
# Home
# -------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -------------------------
# Register
# -------------------------
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        full_name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        hashed_password = generate_password_hash(password)

        new_user = User(
            full_name=full_name,
            email=email,
            password=hashed_password
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("login"))

    return render_template("register.html")


# -------------------------
# Login
# -------------------------
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):

            session["user_id"] = user.id
            session["user_name"] = user.full_name

            return redirect(url_for("dashboard"))

        return "Invalid Email or Password"

    return render_template("login.html")


# -------------------------
# Logout
# -------------------------
@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("home"))


# -------------------------
# Dashboard
# -------------------------
@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect(url_for("login"))

    total = Problem.query.filter_by(user_id=session["user_id"]).count()

    easy = Problem.query.filter_by(
        user_id=session["user_id"],
        difficulty="Easy"
    ).count()

    medium = Problem.query.filter_by(
        user_id=session["user_id"],
        difficulty="Medium"
    ).count()

    hard = Problem.query.filter_by(
        user_id=session["user_id"],
        difficulty="Hard"
    ).count()

    problems = Problem.query.filter_by(
        user_id=session["user_id"]
    ).all()

    topics = {}

    for problem in problems:

        if problem.topic in topics:
            topics[problem.topic] += 1
        else:
            topics[problem.topic] = 1

    return render_template(
        "dashboard.html",
        total=total,
        easy=easy,
        medium=medium,
        hard=hard,
        topics=topics
    )
# -------------------------
# Add Problem
# -------------------------
@app.route("/add_problem", methods=["GET", "POST"])
def add_problem():

    if "user_id" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":

        title = request.form["title"]
        difficulty = request.form["difficulty"]
        topic = request.form["topic"]

        date_solved = datetime.strptime(
            request.form["date_solved"],
            "%Y-%m-%d"
        ).date()

        time_taken = int(request.form["time_taken"])

        notes = request.form["notes"]

        new_problem = Problem(
            title=title,
            difficulty=difficulty,
            topic=topic,
            date_solved=date_solved,
            time_taken=time_taken,
            notes=notes,
            user_id=session["user_id"]
        )

        db.session.add(new_problem)
        db.session.commit()

        return redirect(url_for("dashboard"))

    return render_template("add_problem.html")

@app.route("/problems")
def problems():

    if "user_id" not in session:
        return redirect(url_for("login"))

    problems = Problem.query.filter_by(
        user_id=session["user_id"]
    ).order_by(Problem.date_solved.desc()).all()

    return render_template(
        "problems.html",
        problems=problems
    )

@app.route("/delete_problem/<int:problem_id>")
def delete_problem(problem_id):

    if "user_id" not in session:
        return redirect(url_for("login"))

    problem = Problem.query.filter_by(
        id=problem_id,
        user_id=session["user_id"]
    ).first()

    if problem:

        db.session.delete(problem)
        db.session.commit()

    return redirect(url_for("problems"))



@app.route("/edit_problem/<int:problem_id>", methods=["GET", "POST"])
def edit_problem(problem_id):

    if "user_id" not in session:
        return redirect(url_for("login"))

    problem = Problem.query.filter_by(
        id=problem_id,
        user_id=session["user_id"]
    ).first()

    if not problem:
        return "Problem Not Found"

    if request.method == "POST":

        problem.title = request.form["title"]
        problem.difficulty = request.form["difficulty"]
        problem.topic = request.form["topic"]

        problem.date_solved = datetime.strptime(
            request.form["date_solved"],
            "%Y-%m-%d"
        ).date()

        problem.time_taken = int(request.form["time_taken"])
        problem.notes = request.form["notes"]

        db.session.commit()

        return redirect(url_for("problems"))

    return render_template(
        "edit_problem.html",
        problem=problem
    )


# -------------------------
# Run Application
# -------------------------
if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True)