from flask import Flask, request, render_template, redirect, url_for

from forms import TitleAuthorForm
from models import home_library

app = Flask(__name__)
app.config["SECRET_KEY"] = "zyrafyidadoszafy"

@app.route("/homelibrary/", methods=["GET", "POST"])
def books():
    form = TitleAuthorForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            home_library.create(form.data)
            home_library.save_all()
        return redirect(url_for("books"))

    return render_template("homelibrary.html", form=form, home_library=home_library.all(), error=error)


@app.route("/homelibrary/<int:book_id>/", methods=["GET", "POST"])
def book_details(book_id):
    book = home_library.get(book_id - 1)
    form = TitleAuthorForm(data=book)

    if request.method == "POST":
        if form.validate_on_submit():
            home_library.update(book_id - 1, form.data)
        return redirect(url_for("books"))
    return render_template("readbook.html", form=form, book_id=book_id)


if __name__ == "__main__":
    app.run(debug=True)