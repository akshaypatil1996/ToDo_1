from flask import Flask, render_template, request, redirect, url_for
from model import connectToDB, insertDB, viewData, updateData, deleteData

app = Flask(__name__)

@app.route('/')
def index():
    connectToDB()
    test = viewData()
    return render_template('base.html', test=test)

@app.route('/add', methods =["GET", "POST"])
# def add():
#     if request.method == "POST":
#         title = request.form.get("title")
#         connectToDB()
#         insertDB(title)
#         return redirect(url_for("index"))
#     elif request.method == "GET":
#         return redirect(url_for('index'))
def add():
    if request.method == "POST":
        title = request.form.get("title")
        title_another = request.form.get("title_another")
        connectToDB()
        insertDB(title,title_another)
        # insertDB(title_another)  # Insert the second todo as well
        return redirect(url_for("index"))
    elif request.method == "GET":
        return redirect(url_for('index'))

@app.route('/update/<int:id>')
def update(id):
    connectToDB()
    updateData(id)
    return redirect(url_for("index"))

@app.route('/delete/<int:id>')
def delete(id):
    connectToDB()
    deleteData(id)
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)