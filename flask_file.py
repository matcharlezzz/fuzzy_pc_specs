import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    budget = flask.request.form.get('budget')
    workload = flask.request.form.get('workload')
    storage = flask.request.form.get('storage')

    import main as fuzzy

    values = fuzzy.ezpc(budget, workload, storage)

    return flask.render_template('recos.html', value=values)

if __name__ == "__main__":
    app.run(debug=True)