import logging
from typing import Any

from dataclay import DataClayObject, activemethod
from dataclay.contrib.mqtt import MQTTMixin

logger = logging.getLogger(__name__)


class MqttSubs(DataClayObject, MQTTMixin):

    data: dict[str, Any]
    topic: str
    temperature: str

    @activemethod
    def __init__(self):
        self = self
        self.data = ""
        self.topic = ""
        self.temperature = "NO DATA"

    """ 
    Here you will have to modify the message_handling function, which is just a placeholder in the 
    MQTTMixin class.
    The message has an encoded payload with the data that was sent. (HINT: check the function produce_mqtt_msg 
    from MQTTMixin)
        -If the temperature is lower than 5°, we will save the temperature as "freezing" with the (temperature)
        -If the temperature is between 5° and lower than 17°, we will save the temperature as "cold" 
         and the (temperature)
        -If the temperature is higher than 17°, we will save the temperature as "warm" with the (temperature)

        Example: tmp is 7° -> self.temperature = cold(7)
    """
    @activemethod
    def message_handling(self, client, userdata, msg):
        from json import loads

        tmp = loads(...)

        ...

    @activemethod
    def set_topic(self, topic):
        self.topic = topic

    @activemethod
    def set_data(self, data):
        self.data = data

    @activemethod
    def get_temp(self):
        return self.temperature
