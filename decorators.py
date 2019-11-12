from functools import wraps
from http import HTTPStatus
from uuid import UUID

from Crypto.Hash import SHA256
from flask import request
from werkzeug.exceptions import abort


def verify_uuid():
    def internal_verify_uuid(func):
        @wraps(func)
        def wrapper(identifier, *args, **kwargs):
            try:
                identifier = UUID(identifier)
            except ValueError:
                abort(HTTPStatus.BAD_REQUEST)
            return func(identifier, *args, **kwargs)
        return wrapper
    return internal_verify_uuid


def generate_sha():
    def internal_verify_uuid(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            content = request.data

            digest = SHA256.new()
            digest.update(content)
            return func(*args, **{"digest": digest, **kwargs})
        return wrapper
    return internal_verify_uuid
