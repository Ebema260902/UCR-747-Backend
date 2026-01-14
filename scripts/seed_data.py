"""
Script para poblar la base de datos con datos de ejemplo
"""
from datetime import date
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.database import Base
from app.models.category import Category
from app.models.creator import Creator
from app.models.project import Project
from app.models.games import Games
from app.models.academic_material import AcademicMaterial

# Crear las tablas si no existen
Base.metadata.create_all(bind=engine)

def seed_data(force=False):
    db: Session = SessionLocal()
    
    try:
        # Verificar si ya hay datos
        if db.query(Category).count() > 0 and not force:
            print("La base de datos ya tiene datos.")
            print("Si quieres regenerar los datos, ejecuta: python scripts/seed_data.py --force")
            return
        
        # Limpiar datos existentes si force=True
        if force:
            print("Limpiando datos existentes...")
            db.query(AcademicMaterial).delete()
            db.query(Games).delete()
            db.query(Project).delete()
            db.query(Creator).delete()
            db.query(Category).delete()
            db.commit()
            print("Datos limpiados.")
        
        # 1. Crear Categorías
        print("Creando categorias...")
        categorias = [
            Category(name_category="Desarrollo Web"),
            Category(name_category="Diseño UI/UX"),
            Category(name_category="Programación"),
            Category(name_category="Bases de Datos"),
            Category(name_category="Aplicaciones Móviles"),
            Category(name_category="Juegos Educativos"),
        ]
        db.add_all(categorias)
        db.commit()
        print(f"{len(categorias)} categorias creadas")
        
        # 2. Crear Creadores
        print("Creando creadores...")
        creadores = [
            Creator(
                name_creator="Emanuel Agüero",
                career="Informática y Tecnología Multimedio",
                state="Activo",
                photo_creator="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=400&q=60"
            ),
            Creator(
                name_creator="Kevin Morera",
                career="Ingeniería de Software",
                state="Activo",
                photo_creator="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=400&q=60"
            ),
            Creator(
                name_creator="Stefano Sánchez",
                career="Diseño Digital",
                state="Activo",
                photo_creator="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?auto=format&fit=crop&w=400&q=60"
            ),
            Creator(
                name_creator="María Rodríguez",
                career="Ingeniería en Sistemas",
                state="Activo",
                photo_creator="https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=400&q=60"
            ),
        ]
        db.add_all(creadores)
        db.commit()
        print(f"{len(creadores)} creadores creados")
        
        # Refrescar para obtener los IDs
        categorias = db.query(Category).all()
        creadores = db.query(Creator).all()
        
        # 3. Crear Proyectos
        print("Creando proyectos...")
        proyectos = [
            Project(
                creator_id=creadores[0].creator_id,
                category_id=categorias[0].category_id,
                name_project="Ticolancer",
                description="Plataforma para conectar emprendedores nacionales con clientes locales. Sistema completo de gestión de proyectos y pagos.",
                photo_project="https://images.unsplash.com/photo-1521737604893-d14cc237f11d?auto=format&fit=crop&w=800&q=60",
                date=date(2024, 1, 15),
                state="Activo"
            ),
            Project(
                creator_id=creadores[0].creator_id,
                category_id=categorias[0].category_id,
                name_project="Kimchis",
                description="Sitio web inspirado en la gastronomía coreana. E-commerce moderno con sistema de reservas y menú interactivo.",
                photo_project="https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=800&q=60",
                date=date(2024, 2, 20),
                state="Activo"
            ),
            Project(
                creator_id=creadores[1].creator_id,
                category_id=categorias[1].category_id,
                name_project="Jint",
                description="Plataforma para asignación de tareas entre profesores y estudiantes. Sistema de notificaciones y seguimiento.",
                photo_project="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=800&q=60",
                date=date(2024, 3, 10),
                state="Activo"
            ),
            Project(
                creator_id=creadores[2].creator_id,
                category_id=categorias[0].category_id,
                name_project="Madera Art",
                description="Tienda online de productos artesanales en madera. Catálogo completo con sistema de pedidos personalizados.",
                photo_project="https://images.unsplash.com/photo-1519710164239-da123dc03ef4?auto=format&fit=crop&w=800&q=60",
                date=date(2024, 1, 28),
                state="Activo"
            ),
            Project(
                creator_id=creadores[3].creator_id,
                category_id=categorias[0].category_id,
                name_project="LoopMarket",
                description="Marketplace para comprar y vender loops musicales. Plataforma con reproductor integrado y sistema de licencias.",
                photo_project="https://images.unsplash.com/photo-1511379938547-c1f69419868d?auto=format&fit=crop&w=800&q=60",
                date=date(2024, 2, 5),
                state="Activo"
            ),
            Project(
                creator_id=creadores[1].creator_id,
                category_id=categorias[4].category_id,
                name_project="FitTrack",
                description="App de registro de progreso físico y nutricional. Seguimiento de ejercicios, dieta y metas personales.",
                photo_project="https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?auto=format&fit=crop&w=800&q=60",
                date=date(2024, 3, 22),
                state="Activo"
            ),
        ]
        db.add_all(proyectos)
        db.commit()
        print(f"{len(proyectos)} proyectos creados")
        
        # 4. Crear Juegos
        print("Creando juegos...")
        juegos = [
            Games(
                creator_id=creadores[0].creator_id,
                category_id=categorias[5].category_id,
                name_game="Code Combat",
                description="Aprendé programación jugando como un héroe en un mundo de fantasía. Ideal para aprender Python o JavaScript.",
                photo_game="https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=800&q=60",
                link="https://codecombat.com/",
                date=date(2024, 1, 10),
                state="Activo"
            ),
            Games(
                creator_id=creadores[1].creator_id,
                category_id=categorias[5].category_id,
                name_game="TypingClub",
                description="Mejorá tu velocidad y precisión al escribir mientras completás misiones divertidas.",
                photo_game="https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=800&q=60",
                link="https://www.typingclub.com/",
                date=date(2024, 2, 15),
                state="Activo"
            ),
            Games(
                creator_id=creadores[2].creator_id,
                category_id=categorias[5].category_id,
                name_game="Kahoot!",
                description="Participá en quizzes interactivos para repasar conocimientos y competir con tus compañeros.",
                photo_game="https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=800&q=60",
                link="https://kahoot.com/",
                date=date(2024, 2, 20),
                state="Activo"
            ),
            Games(
                creator_id=creadores[0].creator_id,
                category_id=categorias[5].category_id,
                name_game="Scratch",
                description="Creá tus propios juegos y animaciones con bloques de código. Perfecto para principiantes.",
                photo_game="https://images.unsplash.com/photo-1580894908361-967195033215?auto=format&fit=crop&w=800&q=60",
                link="https://scratch.mit.edu/",
                date=date(2024, 3, 1),
                state="Activo"
            ),
        ]
        db.add_all(juegos)
        db.commit()
        print(f"{len(juegos)} juegos creados")
        
        # 5. Crear Materiales Académicos
        print("Creando materiales academicos...")
        materiales = [
            AcademicMaterial(
                creator_id=creadores[0].creator_id,
                category_id=categorias[2].category_id,
                name_material="Introducción a la Programación",
                description="Conceptos básicos de programación y lógica. Guía completa desde cero hasta estructuras de control avanzadas.",
                photo_material="https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=800&q=60",
                date=date(2024, 1, 5),
                state="Activo"
            ),
            AcademicMaterial(
                creator_id=creadores[1].creator_id,
                category_id=categorias[1].category_id,
                name_material="Diseño UX/UI",
                description="Principios fundamentales del diseño centrado en el usuario. Wireframes, prototipos y pruebas de usabilidad.",
                photo_material="https://images.unsplash.com/photo-1607746882042-944635dfe10e?auto=format&fit=crop&w=800&q=60",
                date=date(2024, 1, 12),
                state="Activo"
            ),
            AcademicMaterial(
                creator_id=creadores[2].creator_id,
                category_id=categorias[3].category_id,
                name_material="Bases de Datos",
                description="Guía práctica para aprender SQL y modelado de datos. Desde consultas básicas hasta diseño de esquemas complejos.",
                photo_material="https://images.unsplash.com/photo-1556761175-5973dc0f32e7?auto=format&fit=crop&w=800&q=60",
                date=date(2024, 2, 1),
                state="Activo"
            ),
            AcademicMaterial(
                creator_id=creadores[0].creator_id,
                category_id=categorias[0].category_id,
                name_material="Desarrollo Web",
                description="HTML, CSS y JavaScript desde cero. Construcción de aplicaciones web modernas con frameworks actuales.",
                photo_material="https://images.unsplash.com/photo-1517430816045-df4b7de11d1d?auto=format&fit=crop&w=800&q=60",
                date=date(2024, 2, 8),
                state="Activo"
            ),
            AcademicMaterial(
                creator_id=creadores[3].creator_id,
                category_id=categorias[2].category_id,
                name_material="Inteligencia Artificial",
                description="Introducción al aprendizaje automático con Python. Algoritmos, redes neuronales y aplicaciones prácticas.",
                photo_material="https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&w=800&q=60",
                date=date(2024, 2, 15),
                state="Activo"
            ),
            AcademicMaterial(
                creator_id=creadores[1].creator_id,
                category_id=categorias[2].category_id,
                name_material="Redes y Seguridad",
                description="Conceptos clave sobre redes informáticas y ciberseguridad. Protocolos, firewalls y mejores prácticas.",
                photo_material="https://images.unsplash.com/photo-1563013544-824ae1b704d3?auto=format&fit=crop&w=800&q=60",
                date=date(2024, 3, 1),
                state="Activo"
            ),
            AcademicMaterial(
                creator_id=creadores[2].creator_id,
                category_id=categorias[1].category_id,
                name_material="Animación y Multimedia",
                description="Técnicas básicas para crear contenido animado. Motion graphics, video y elementos interactivos.",
                photo_material="https://images.unsplash.com/photo-1626785774573-4b799315345d?auto=format&fit=crop&w=800&q=60",
                date=date(2024, 3, 5),
                state="Activo"
            ),
            AcademicMaterial(
                creator_id=creadores[3].creator_id,
                category_id=categorias[4].category_id,
                name_material="Desarrollo Móvil",
                description="Curso básico de apps móviles con React Native. Navegación, state management y APIs nativas.",
                photo_material="https://images.unsplash.com/photo-1551650975-87deedd944c3?auto=format&fit=crop&w=800&q=60",
                date=date(2024, 3, 10),
                state="Activo"
            ),
            AcademicMaterial(
                creator_id=creadores[0].creator_id,
                category_id=categorias[0].category_id,
                name_material="Emprendimiento Digital",
                description="Cómo lanzar un proyecto tecnológico exitoso. Planes de negocio, marketing digital y financiamiento.",
                photo_material="https://images.unsplash.com/photo-1522205408450-add114ad53fe?auto=format&fit=crop&w=800&q=60",
                date=date(2024, 3, 15),
                state="Activo"
            ),
        ]
        db.add_all(materiales)
        db.commit()
        print(f"{len(materiales)} materiales academicos creados")
        
        print("\nDatos de ejemplo agregados exitosamente!")
        print("\nResumen:")
        print(f"   - {len(categorias)} categorías")
        print(f"   - {len(creadores)} creadores")
        print(f"   - {len(proyectos)} proyectos")
        print(f"   - {len(juegos)} juegos")
        print(f"   - {len(materiales)} materiales académicos")
        
    except Exception as e:
        db.rollback()
        print(f"Error al agregar datos: {e}")
        raise
    finally:
        db.close()

if __name__ == "__main__":
    import sys
    force = "--force" in sys.argv or "-f" in sys.argv
    seed_data(force=force)

