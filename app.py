from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "success": "true",
        "message": "Seja Bem-Vindo(a) ao mundo Docker!",
        "version": "1.0.0"
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print(f"Aplicação executando na porta: {port}")
    app.run(host='0.0.0.0', port=port)
