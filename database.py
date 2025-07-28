from sqlalchemy import create_engine, text
import os

string_conexao = os.environ['db_connection_string']

engine = create_engine(string_conexao, connect_args={"sslmode": "require"})


def carrega_vagas_db():
  with engine.connect() as conn:
    resultado = conn.execute(text("select * from vagas"))
    vagas = []

  for vaga in resultado.all():
    vagas.append(vaga._asdict())

  return vagas
