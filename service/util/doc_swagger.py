from flask_restplus import fields
from service.restplus import api

INPUT_MAIN_SERVICE = api.model(
  'input_main_service', {
    'textoMensagem': fields.List(fields.String(), required=True, description="CEP a ser localizado")})
