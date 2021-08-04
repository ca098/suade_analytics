from flasgger import swag_from
from flask import Blueprint, jsonify

from services.service_engine import ServiceEngine

ANALYTICS_BLUEPRINT = Blueprint('analytics_blueprint', __name__)

SE = ServiceEngine()


@ANALYTICS_BLUEPRINT.route('/get_analytics_report/<string:date>', methods=['GET'])
@swag_from('swagger/get_analytics_report.yml')
def get_analytics_report(date):

    files = SE.csv_service.parse_data()

    return jsonify(True)