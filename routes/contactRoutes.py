from flask import Flask , jsonify, request
from flask import Blueprint
import controllers.contactController as contactController

contact_api = Blueprint('contact_api', __name__)

@contact_api.route('/contactos', methods = ['GET'])
def getContactos():
    paramentros = request.args
    id_usuario = paramentros['id_usuario']
    campo = paramentros['campo']
    orden = paramentros['orden']
    contactos = contactController.seleccionar_contactos(id_usuario, campo, orden)

    return jsonify(contactos)

