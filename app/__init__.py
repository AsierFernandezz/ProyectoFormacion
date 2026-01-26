from app.models.user import Base
from app.db.session import engine
from app.models.user import User  # tu modelo de usuario

# Crea todas las tablas definidas en Base
Base.metadata.create_all(bind=engine)

print("Base de datos y tablas creadas correctamente")
