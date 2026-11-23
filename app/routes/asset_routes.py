from flask import Blueprint
from app.controllers import asset_controller as c

bp = Blueprint('assets', __name__)

bp.add_url_rule('', 'list_assets', c.list_assets, methods=['GET'])
bp.add_url_rule('', 'create_asset', c.create_asset, methods=['POST'])
bp.add_url_rule('/<int:id>', 'get_asset', c.get_asset, methods=['GET'])
bp.add_url_rule('/<int:id>', 'update_asset', c.update_asset, methods=['PUT'])
bp.add_url_rule('/<int:id>', 'delete_asset', c.delete_asset, methods=['DELETE'])
