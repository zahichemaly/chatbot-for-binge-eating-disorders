from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter

# function to train data into model
def train_nlu(data, configs, model_dir):
	training_data = load_data(data)
	trainer = Trainer(config.load(configs))
	trainer.train(training_data)
	model_directory = trainer.persist(model_dir, fixed_model_name = 'datanlu')

# function to run the trained model
def run_nlu():
    interpreter = Interpreter.load('./models/nlu/default/datanlu')
    print(interpreter.parse("My name is Zahi. I'm listening to music."))

if __name__ == '__main__':
    train_nlu('./data/data.json', 'config_spacy.json', './models/nlu')