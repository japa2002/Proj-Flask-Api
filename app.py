from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Renderiza a página corretamente

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Debug ativado para ver erros
