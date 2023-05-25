from flask import Flask , render_template
app = Flask(__name__)   

@app.route('/')
@app.route('/<int:x>/<int:y>/<color_1>/<color_2>')
def checkerboard(x=8, y=8 , color_1='red', color_2='black'):
    return render_template('index.html', x=x, y=y, color_1=color_1, color_2=color_2 )

if __name__=="__main__":   
    app.run(debug=True) 