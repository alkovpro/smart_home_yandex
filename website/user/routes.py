from uuid import uuid4

from flask import Blueprint
from flask import jsonify, request
from authlib.integrations.flask_oauth2 import current_token

from ..oauth2 import require_oauth

bp_user = Blueprint('user', __name__)


@bp_user.route('/devices')
@require_oauth('smart_home')
def devices():
    request_id = request.environ.get('HTTP_X_REQUEST_ID', None) or uuid4().hex
    payload = {
        "user_id": str(current_token.user.id),
        "devices": [{
            "id": uuid4().hex,  # Тут каждый раз новый id, поэтому будет новое устройство
            "name": "device_1",
            "description": "device_1 description",
            "room": "room_1",
            "type": "devices.types.light",
            "custom_data": {},
            "capabilities": [{
                "type": "devices.capabilities.on_off"
            }],
            "properties": [],
            "device_info": {
                "manufacturer": "me",
                "model": "model_1",
                "hw_version": "1.0",
                "sw_version": "1.0.0",
            }
        }]
    }
    return jsonify(request_id=request_id, payload=payload)
