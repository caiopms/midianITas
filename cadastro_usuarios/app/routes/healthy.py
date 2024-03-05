from flask import jsonify

def healthy_routes(app):
    # Define uma rota raiz que retorna uma mensagem de boas-vindas
    @app.route('/healthy')
    def hello_world():
        return "API de cadastro de Escalas está no ar!"

    # Define outra rota de exemplo que retorna dados em formato JSON
    @app.route('/api/data')
    def get_data():
        data = {"key": "value", "number": 42}
        return jsonify(data)