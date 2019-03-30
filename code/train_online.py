from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RegexInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.policies.fallback import FallbackPolicy
from rasa_core.interpreter import RasaNLUInterpreter

from rasa_core.channels import UserMessage
from rasa_core.events import SlotSet

import logging
import ruamel.yaml
import warnings
warnings.simplefilter('ignore', ruamel.yaml.error.UnsafeLoaderWarning)

logger = logging.getLogger(__name__)

# custom fallback policy
fallback = FallbackPolicy(fallback_action_name="utter_default",
                          core_threshold=0.3,
                          nlu_threshold=0.3)

def run_train_online(input_channel, interpreter,
                          domain_file="crisis_domain.yml",
                          training_data_file='data/stories.md'):

    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(max_history=2), KerasPolicy(), fallback],
                  interpreter=interpreter)
                  
    agent.train_online(training_data_file,
                       input_channel=input_channel,
                       batch_size=50,
                       epochs=400,
                       max_training_samples=400)

    return agent

if __name__ == '__main__':
    logging.basicConfig(level="INFO")
    nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/datanlu')
    run_train_online(ConsoleInputChannel(), nlu_interpreter)
