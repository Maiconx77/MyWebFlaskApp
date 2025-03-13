from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Cria uma conexão com o banco de dados SQLite chamado 'myapp.db'
db = create_engine('sqlite:///myapp.db', connect_args={"check_same_thread": False})

# Cria uma sessão para interagir com o banco de dados
Session = sessionmaker(bind=db)  # O parâmetro 'bind' especifica a conexão do banco de dados
session = Session()

# Cria uma classe base para as tabelas do banco de dados
Base = declarative_base()

# Importa os módulos necessários para definir as tabelas
from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship, validates

# Define a tabela 'user' com suas colunas e relacionamentos
class Project(Base):
    __tablename__ = 'projects'  # Nome da tabela no banco de dados
    id = Column(Integer, primary_key=True, autoincrement=True)  # Coluna 'id' como chave primária
    code = Column(String, length=5, nullable=False)  # Coluna 'name' que não pode ser nula
    title = Column(String, nullable=False)  # Coluna 'email' que não pode ser nula
    description = Column(String)  # Coluna 'description' que pode ser nula
    deliverables = relationship('Deliverable', back_populates='project')  # Relacionamento com a tabela 'deliverable'

    @validates('code')
    def validate_code(self, key, code):
        if len(code) < 3:
            raise ValueError("O código deve ter pelo menos 3 caracteres.")
        return code

# Define a tabela 'deliverable' com suas colunas e relacionamentos
class Deliverable(Base):
    __tablename__ = 'deliverables'  # Nome da tabela no banco de dados
    id = Column(Integer, primary_key=True, autoincrement=True)  # Coluna 'id' como chave primária
    title = Column(String, nullable=False)  # Coluna 'title' que não pode ser nula
    client_number = Column(String)  # Coluna 'client_number' que pode ser nula
    weight = Column(Integer, nullable=False, default=0)  # Coluna 'weight' que não pode ser nula
    is_completed = Column(Boolean, default=False)  # Coluna 'is_completed' com valor padrão 'False'
    project_id = Column(Integer, ForeignKey('projects.id'))  # Coluna 'project_id' com chave estrangeira
    project = relationship('Project', back_populates='deliverables')  # Relacionamento com a tabela 'project'


# Define a tabela 'progress' com suas colunas e relacionamentos
class Progress(Base):
    __tablename__ = 'progresses'  # Nome da tabela no banco de dados
    id = Column(Integer, primary_key=True, autoincrement=True)  # Coluna 'id' como chave primária
    milestone = Column(String, nullable=False)  # Coluna 'milestone' que não pode ser nula
    milestone_value = Column(Integer, nullable=False, default=0)  # Coluna 'milestone_value' que não pode ser nula
    planned_date = Column(Date, nullable=False)  # Coluna 'planned_date' que não pode ser nula
    forecast_date = Column(Date, nullable=False)  # Coluna 'forecast_date' que não pode ser nula
    actual_date = Column(Date)  # Coluna 'actual_date' que pode ser nula
    weight = Column(Integer, nullable=False, default=0)  # Coluna 'weight' que não pode ser nula
    earned_value = Column(Integer, nullable=False, default=0)  # Coluna 'earned_value' que não pode ser nula
    is_completed = Column(Boolean, default=False)  # Coluna 'is_completed' com valor padrão 'False'
    deliverable_id = Column(Integer, ForeignKey('deliverables.id'))  # Coluna 'deliverable_id' com chave estrangeira
    deliverable = relationship('Deliverable', back_populates='progresses')  # Relacionamento com a tabela 'deliverable'


# Cria todas as tabelas definidas no banco de dados
Base.metadata.create_all(db)  # O objeto 'db' é passado diretamente como argumento