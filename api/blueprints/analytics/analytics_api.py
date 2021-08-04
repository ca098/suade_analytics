from flasgger import swag_from
from flask import Blueprint, jsonify

ANALYTICS_BLUEPRINT = Blueprint('analytics_blueprint', __name__)


@ANALYTICS_BLUEPRINT.route('/get_analytics_report', methods=['GET'])
@swag_from('swagger/get_analytics_report.yml')
def get_analytics_report():

    return jsonify(True)