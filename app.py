from flask import Flask, render_template

skills_app = Flask(__name__)

my_skills=[("html", 80), ("css", 50), ("python", 20)]

@skills_app.route("/")
def home():
    return render_template("home.html", title="Home", custom_css="home")

@skills_app.route("/skills")
def skills():
    return render_template("skills.html", title="Skills", custom_css="skills", page_head="My Skills", skills=my_skills)

@skills_app.route("/about")
def about():
    return render_template("about.html", title="About", custom_css="about")

if __name__ == '__main__':
    skills_app.run()