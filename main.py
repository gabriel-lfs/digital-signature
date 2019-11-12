import os
import uuid
from http import HTTPStatus

from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from decouple import config
from flask import Flask, abort, jsonify, config

from decorators import verify_uuid, generate_sha

app = Flask(__name__)


@app.route('/sign', methods=['POST'])
@generate_sha()
def sign(**kwargs):
    with open(f'./private_rsa_{config("KEY")}.pem') as file:
        chave_privada = RSA.importKey(file.read())
        assinador_privado = PKCS1_v1_5.new(chave_privada)

    identifier = uuid.uuid4()
    with open(f'./certs/{identifier}.pem', 'wb+') as f:
        f.write(assinador_privado.sign(kwargs['digest']))
    return jsonify({'verificationIdentifier': str(identifier)}), HTTPStatus.OK


@app.route('/verify-private/<identifier>', methods=['POST'])
@verify_uuid()
@generate_sha()
def verify_private(identifier, **kwargs):
    with open(f'./private_rsa_{config("KEY")}.pem') as file:
        chave_privada = RSA.importKey(file.read())
        assinador_privado = PKCS1_v1_5.new(chave_privada)

    try:
        identifier = uuid.UUID(identifier, kwargs['digest'])
    except ValueError:
        abort(HTTPStatus.BAD_REQUEST)

    with open(f'./certs/{identifier}.pem', "rb") as f:
        if not assinador_privado.verify(kwargs['digest'], f.read()):
            abort(HTTPStatus.FORBIDDEN)
        return "The content is authentic", HTTPStatus.OK


@app.route('/verify-public/<identifier>', methods=['POST'])
@verify_uuid()
@generate_sha()
def verify_public(identifier, **kwargs):
    with open(f'./public_rsa_{config("KEY")}.pem') as file:
        chave_publica = RSA.importKey(file.read())
        assinador_publico = PKCS1_v1_5.new(chave_publica)

    with open(f'./certs/{identifier}.pem', "rb") as f:
        if not assinador_publico.verify(kwargs['digest'], f.read()):
            abort(HTTPStatus.FORBIDDEN)
        return "The content is authentic", HTTPStatus.OK


if __name__ == '__main__':
    app.run()
