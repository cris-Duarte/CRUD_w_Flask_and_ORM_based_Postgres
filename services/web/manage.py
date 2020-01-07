from flask.cli import FlaskGroup
from project import app, db, Usuario, TipoUsuario

cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command("seed_db")
def seed_db():
    db.session.add(TipoUsuario(descripcion="Administrador"))
    db.session.add(TipoUsuario(descripcion="Coordinador"))
    db.session.add(TipoUsuario(descripcion="Profesor"))
    db.session.add(TipoUsuario(descripcion="Alumno"))

    db.session.commit()



if __name__ == "__main__":
    cli()
