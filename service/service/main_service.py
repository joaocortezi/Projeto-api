import requests
import time
import json
from loguru import logger
from service.constants import mensagens
import pandas as pd



class AdressService():

    def __init__(self):
        logger.debug(mensagens.INICIO_LOAD_SERVICO)
        self.load_model()

    def load_model(self):
        """"
        Carrega o modelo Endereço a ser usado
        """

        self.model = Endereco()

        logger.debug(mensagens.FIM_LOAD_MODEL)

    def executar_rest(self, texts):
        response = {}

        logger.debug(mensagens.INICIO_PREDICT)
        start_time = time.time()

        response_endereco = self.buscar_endereco(texts['textoMensagem'])

        logger.debug(mensagens.FIM_PREDICT)
        logger.debug(f"Fim de todos endereços em {time.time()-start_time}")

        df_response = pd.DataFrame(texts, columns=['textoMensagem'])
        df_response['endereco'] = response_endereco

        df_response = df_response.drop(columns=['textoMensagem'])

        response = {
                     "Enderecos": json.loads(df_response.to_json(
                                                                            orient='records', force_ascii=False))}

        return response

    def buscar_endereco(self, texts):
        """
        Pega o modelo carregado e aplica em texts
        """
        logger.debug('Iniciando a Consulta CEP...')

        response = []
        for phrase in texts:
            translate_dict = self.model.translate(phrase, dest='pt')
            response.append(translate_dict.text)
        
        return response
 