from st2reactor.sensor.base import PollingSensor
import requests
import json

class Poll(PollingSensor):
    def __init__(self, sensor_service,  config=None, poll_interval=5) -> None:
        super(Poll, self).__init__(sensor_service=sensor_service, 
                                    config=config, 
                                    poll_interval=poll_interval
                                )
        self._logger = self.sensor_service.get_logger(name= self.__class__.__name__)
        self._trigger_name = 'example_trigger'
        self._trigger_pack = 'polling_sesnor'
        self._trigger_ref = '.'.join([self._trigger_pack, self._trigger_name])
        self._stop = False

    def setup(self):
        pass

    def poll(self):
        data = requests.get("http://127.0.0.1:5000/orders/pending")
        data = data.json()
        if not 'res' in data:
            self._dispatch_trigger(data)
                    

    def cleanup(self):
        pass

    def add_trigger(self, trigger):
        pass

    def update_trigger(self, trigger):
        pass

    def remove_trigger(self, trigger):
        pass
    
    def _dispatch_trigger(self, payload):
        trigger = self._trigger_ref
        self._logger.debug('Found the api level Dispatching trigger: %s', payload)
        self._sensor_service.dispatch(trigger, payload)



