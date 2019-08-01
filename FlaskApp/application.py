from flask import Flask, render_template, request, url_for
import datetime

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")
def present_date():
    now = datetime.datetime.now().date()
    # tasks = extract tasks from README.md file to here.
    # schedule = embed g calendar on the right hand side on this page.
    return render_template("index.html", date=now)


if __name__ == '__main__':
    app.run(debug=True)
