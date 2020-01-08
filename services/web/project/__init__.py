from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/", methods=["POST" ,"GET"])
def registrodeusuarios():
    s_usuarios = False
    up = False
    if request.form.get('alta'):
        u = Usuario(nombre=request.form.get('nombre'), apellido=request.form.get('apellido'), ci=int(request.form.get('ci')), email=request.form.get('email'), activo = True, con=request.form.get('con'), tipo=int(request.form.get('tipo')))
        db.session.add(u)
        db.session.commit()
        s_usuarios = True
    if request.form.get('baja'):
        u = Usuario.query.get(int(request.form.get('id')))
        u.activo = False
        db.session.commit()
        s_usuarios = True
    if request.form.get('modificacion'):
        up = Usuario.query.get(int(request.form.get('id')))
    if request.form.get('a_modificar') != None:
        u = Usuario.query.get(request.form.get('a_modificar'))
        u.nombre = request.form.get('nombre')
        u.apellido = request.form.get('apellido')
        u.ci = int(request.form.get('ci'))
        u.email = request.form.get('email')
        u.con = request.form.get('con')
        u.tipo = int(request.form.get('tipo'))
        db.session.commit()

    tipo_usuario = TipoUsuario.query.all()
    usuarios = Usuario.query.filter_by(activo=True).all()
    return render_template("registrodeusuarios.html", tipo_usuario=tipo_usuario, usuarios=usuarios, s_usuarios=s_usuarios, up=up)

@app.route("/reciboregistro", methods=["POST" ,"GET"])
def reciboregistro():
    u = Usuario(nombre=request.form.get('nombre'), apellido=request.form.get('apellido'), ci=int(request.form.get('ci')), email=request.form.get('email'), activo = True, con=request.form.get('con'), tipo=int(request.form.get('tipo')))
    db.session.add(u)
    db.session.commit()
    usuarios = Usuario.query.all()
    return render_template('table_usuarios.html', usuarios=usuarios)



















"""ESTOS SON LOS MODELOS"""

app.config.from_object("project.config.Config")
db = SQLAlchemy(app)

class TipoUsuario(db.Model):
    __tablename__ = "tipo_usuario"

    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(60), nullable=False)

    def __init__(self, descripcion):
        self.descripcion = descripcion


class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(60), nullable=False)
    apellido = db.Column(db.String(60), nullable=False)
    ci = db.Column(db.Integer, default=0,nullable=False)
    email = db.Column(db.String(128), nullable=False)
    activo = db.Column(db.Boolean(), default=True, nullable=False)
    con = db.Column(db.String(200), nullable=False)
    tipo = db.Column(db.Integer, db.ForeignKey("tipo_usuario.id"), nullable=False)

    #def __init__(self, nombre, apellido, ci, email, activo, con, tipo):
    #    self.nombre = email
    #    self.apellido = nombre
    #    self.ci = apellido
    #    self.email = ci
    #    self.activo = activo
    #    self.con = con
    #    self.tipo = tipo
