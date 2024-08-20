from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# URL de conexão com o banco de dados (ajuste conforme necessário)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Exemplo usando SQLite para simplicidade

# Cria o motor de conexão com o banco de dados
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Cria uma fábrica de sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos
Base = declarative_base()

def get_db() -> Session:
    """Função para obter uma sessão do banco de dados."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
