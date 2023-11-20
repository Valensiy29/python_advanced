import json
import logging


class JsonAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        json.dumps(msg,indent=4)
        return msg, kwargs



logger = logging.getLogger(__name__)
adapter = JsonAdapter(logger,logging.info('фывфыв'))