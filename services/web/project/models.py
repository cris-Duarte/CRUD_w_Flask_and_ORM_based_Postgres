import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from project import app


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

    def __init__(self, nombre, apellido, ci, email, activo, tipo):
        self.nombre = email
        self.apellido = nombre
        self.ci = apellido
        self.email = ci
        self.tipo = tipo.id
