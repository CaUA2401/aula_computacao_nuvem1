from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Olá, Nuvem! Esta é minha primeira aplicação web no Render.'

if __name__ == '__main__':
    # A porta é definida dinamicamente pela plataforma de nuvem.
    port = int(os.environ.get('PORT', 5000))
    # O host '0.0.0.0' permite que a aplicação seja acessível de fora do container.
    app.run(host='0.0.0.0', port=port)