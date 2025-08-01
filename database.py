import os
from sqlalchemy import create_engine, text

string_conexao = os.environ['db_connection_string']

engine = create_engine(string_conexao, connect_args={"sslmode": "require"})


def carrega_vagas_db():
  with engine.connect() as conn:
    resultado = conn.execute(text("select * from vagas"))
    vagas = []

  for vaga in resultado.all():
    vagas.append(vaga._asdict())

  return vagas


def carrega_vaga_db(id):
  with engine.connect() as conn:
    resultado = conn.execute(text("SELECT * FROM vagas WHERE id = :val"),
                             {'val': id})
    registro = resultado.mappings().all()
    if len(registro) == 0:
      return None
    else:
      return dict(registro[0])


def adiciona_inscricao(vaga_id, dados):
  with engine.connect() as conn:
    query = text(
        f"INSERT INTO inscricoes (vaga_id, nome, email, linkedin, experiencia) VALUES(:vaga_id, :nome, :email, :linkedin, :experiencia)"
    )
    conn.execute(
        query, {
            'vaga_id': vaga_id,
            'nome': dados['nome'],
            'email': dados['email'],
            'linkedin': dados['linkedin'],
            'experiencia': dados['experiencia']
        })
    conn.commit()
