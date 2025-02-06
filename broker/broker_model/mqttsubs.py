import logging
from typing import Any

from dataclay import DataClayObject, activemethod
from dataclay.contrib.mqtt import MQTTMixin

logger = logging.getLogger(__name__)


class MqttSubs(DataClayObject, MQTTMixin):

    data: dict[str, Any]
    topic: str
    temperature: str

    def __init__(self):
        self = self
        self.data = ""
        self.topic = ""
        self.temperature = "NO DATA"

    @activemethod
    def message_handling(self, client, userdata, msg):
        # To illustrate a message handling, we will be generating human-friendly string as follows:
        #     -If the temperature is lower than 5°, we will save the temperature as "freezing" with the (temperature)
        #     -If the temperature is between 5° and lower than 17°, we will save the temperature as "cold" 
        #      and the (temperature)
        #     -If the temperature is higher than 17°, we will save the temperature as "warm" with the (temperature)
        #
        # Example: If temperature ("tmp") is 7° -> self.temperature = "cold(7)"
        tmp = float(msg.payload.decode("utf-8"))

        if tmp < 5:
            self.temperature = "freezing(%.2f)" % tmp
        elif tmp < 17:
            self.temperature = "cold(%.2f)" % tmp
        else:
            self.temperature = "warm(%.2f)" % tmp

        logger.debug("Temperature is %s [tmp=%s]", self.temperature, tmp)        

    @activemethod
    def set_topic(self, topic):
        self.topic = topic

    @activemethod
    def set_data(self, data):
        self.data = data

    @activemethod
    def get_temp(self):
        return self.temperature
