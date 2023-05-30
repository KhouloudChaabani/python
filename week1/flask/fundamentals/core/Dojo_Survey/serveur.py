from flask import Flask , render_template,redirect,request,session
app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/result')
def result():
    return render_template('result.html')


@app.route('/process', methods=["POST"])
def process():
    session['username'] = request.form['ninja']
    session['loc'] = request.form['Location']
    session['lan'] = request.form['Language']
    session['tex'] = request.form['textarea']
    print(request.form)
    return redirect('/result')




if __name__=="__main__":
    app.run(debug=True) 