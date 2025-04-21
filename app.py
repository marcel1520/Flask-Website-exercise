from flask import Flask, render_template


app = Flask(__name__)


JOBS = [
    {
        'id': 1,
        'title': 'Web Design',
        'location': "Paris, France",
        'salary': "€100000"
    },
{
        'id': 2,
        'title': 'Frontend Engineer',
        'location': "Wien, Austria",
        'salary': "€90000"
    },
{
        'id': 3,
        'title': 'Backend Engineer',
        'location': "Remote",
        'salary': "€110000"
    },
{
        'id': 4,
        'title': 'Cloud Engineer',
        'location': "San Fransisco",
        'salary': "$120000"
    },
]

@app.route("/")
def home():
    return render_template("home.html", jobs=JOBS, company_name="My Company")


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5001, debug=True)