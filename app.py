from flask import Flask, render_template, jsonify, request
from database import carrega_vagas_db, carrega_vaga_db, adiciona_inscricao

app = Flask(__name__)


@app.route('/')
def hello():
    vagas = carrega_vagas_db()
    return render_template('home.html', vagas=vagas)


@app.route('/vagas')
def lista_vagas():
    vagas = carrega_vagas_db()
    return jsonify(vagas)


@app.route('/vaga/<id>')
def mostra_vaga(id):
    vaga = carrega_vaga_db(id)
    if not vaga:
        return "Não há vagas com esse id", 404

    return render_template('detalhe_vaga.html', vaga=vaga)


@app.route('/vaga/<id>/inscricao', methods=['POST', 'GET'])
def inscricao_vaga(id):
    vaga = carrega_vaga_db(id)
    data = request.form
    adiciona_inscricao(id, data)
    return render_template('inscricao_concluida.html',
                           inscricao=data,
                           id=id,
                           vaga=vaga)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
