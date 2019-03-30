from rasa_core.channels import HttpInputChannel
from telegram_channel import TelegramInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter

from rasa_core.channels.rest import HttpInputComponent

import sys
import ruamel.yaml
import warnings
warnings.simplefilter('ignore', ruamel.yaml.error.UnsafeLoaderWarning)

nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/datanlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

URL = sys.argv[1] + "/app/webhook"
PORT = int(sys.argv[2])

input_channel = TelegramInput(
  access_token = "123456789:xxxxxxxxxxxxxxxxx_xxxxxxxxxx-xxxxxx", # you get this when setting up a bot
  verify = "your_bot_username", # this is your bots username
  webhook_url = URL # the url your bot should listen for messages
)

agent.handle_channel(HttpInputChannel(PORT, "/app", input_channel))

