# app/init_db.py
from app.db.database import SessionLocal, engine, Base
from app.models import User
from app.models.role import Role
from app.core.security import hash_password
from datetime import datetime


def init_db():
    # Eliminar y volver a crear todas las tablas
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()

    try:
        # Crear usuarios de prueba
        users = [
            User(
                name="Admin",
                username="admin",
                email="admin@email.com",
                password=hash_password("admin123"),
                role=Role.ADMIN.value,
                created_at=datetime.utcnow()
            ),
            User(
                name="John Doe",
                username="john",
                email="john@email.com",
                password=hash_password("user123"),
                role=Role.USER.value,
                created_at=datetime.utcnow()
            ),
            User(
                name="Jane Smith",
                username="jane",
                email="jane@email.com",
                password=hash_password("user123"),
                role=Role.USER.value,
                created_at=datetime.utcnow()
            ),
            User(
                name="Bob Wilson",
                username="bob",
                email="bob@email.com",
                password=hash_password("user123"),
                role=Role.USER.value,
                created_at=datetime.utcnow()
            ),
        ]

        db.add_all(users)
        db.commit()

        print("✅ Base de datos inicializada con datos de prueba")
        print(f"✅ {len(users)} usuarios creados")
        print("\nCredenciales de prueba:")
        print("Admin: admin@email.com / admin123")
        print("User: john@email.com / user123")

        for user in users:
            print(f"{user.username} - {user.email} - {user.password}")

    except Exception as e:
        print(f"❌ Error: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    init_db()