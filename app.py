from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Banco de dados temporário (Lista de dicionários)
usuarios = []

@app.route('/')
def index():
    # Requisito: Laço de repetição será usado no HTML para ler esta lista
    return render_template('index.html', lista=usuarios)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        
        # Requisito: If/Else para validação simples
        if nome and email:
            usuarios.append({'nome': nome, 'email': email})
            return redirect('/')
            
    return render_template('cadastro.html')

if __name__ == '__main__':
    app.run(debug=True)