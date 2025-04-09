from flask import Flask, render_template,request, redirect


app = Flask(__name__)

# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/makale')
def makale():
    return render_template('makale.html')

@app.route('/LA.html')
def LA():
    return render_template('LA.html')

@app.route('/GK.html')
def GK():
    return render_template('GK.html')

@app.route('/Sepet.html')
def sepet():
    return render_template('sepet.html')

@app.route('/Bagis.html')
def bagis():
    return render_template('bagis.html')

# Dinamik beceriler
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    return render_template('index.html', button_python=button_python)


if __name__ == "__main__":
    app.run(debug=True)
