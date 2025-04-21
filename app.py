from flask import Flask, render_template, jsonify


app = Flask(__name__)


JOBS = [
    {
        'id': 1,
        'title': 'Web Design',
        'location': "Paris, France",
        'salary': "€100.000"
    },
{
        'id': 2,
        'title': 'Frontend Engineer',
        'location': "Wien, Austria",
        'salary': "€90.000"
    },
{
        'id': 3,
        'title': 'Backend Engineer',
        'location': "Remote",

    },
{
        'id': 4,
        'title': 'Cloud Engineer',
        'location': "San Fransisco",
        'salary': "$120.000"
    }
]


@app.route("/")
def home():
    return render_template("home.html", jobs=JOBS, company_name="My Company")


@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5001, debug=True)