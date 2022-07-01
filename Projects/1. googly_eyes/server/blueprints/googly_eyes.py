from flask import Blueprint, jsonify, request, abort
from server.custom.client_exception import ClientException
from server.process_image.process_image import Googlyfier


googly_eyes_bp = Blueprint('googly_eyes', __name__)


@googly_eyes_bp.route('/api/home', methods=['GET', ])
def home():
    return jsonify({"response": "hello world"}), 200


@googly_eyes_bp.route('/api/images', methods=['POST', ])
def googly_eye():
    googlyfier = Googlyfier()

    try:
        data = request.get_json().get('data')
        image = googlyfier.convert_from_base64(data)
        generated_image = googlyfier.generator(image)
        base64_string = googlyfier.convert_to_base64(generated_image)
    except ClientException as err:
        return abort(err.status_code, description=err.message)
    except Exception as err:
        return abort(500, description='Error: ' + str(err))

    return jsonify({'response': base64_string}), 200



