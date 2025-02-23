from flask import Blueprint, jsonify, request

event_route_bp = Blueprint("event_route", __name__)

from src.http_types.http_response import HttpsResponse
from src.http_types.http_request import HttpsRequest

@event_route_bp.route("/event", methods=["POST"])
def create_new_event():
    http_request = HttpsRequest(body=request.json)
    print(http_request.body)

    http_response = HttpsResponse(body={ "estou": "aqui" }, status_code=201)

    return jsonify(http_response.body), http_response.status_code