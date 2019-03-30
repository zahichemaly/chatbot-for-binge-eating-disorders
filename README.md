Chatbot to fight against binge eating disorders
=============

The purpose of this chatbot is to help people deal with binge eating disorders. 
The chatbot can do the following:

- Interrogate the user

- Analyze each episode

- Propose apporpriate prevention strategies in form of "emergency cards"

- Send funny pictures

- Send reminders

- Send useful statistics


Contents
-------

This repository contains 2 folders:

- Screenshots and videos of a typical conversation with the bot deployed on Telegram in the `preview/` directory.
- Everything you need to configure, edit or deploy the bot in the `code/` directory.


Prerequisites
---------

- **Python 3.6.5 (64-Bit)** (https://www.python.org/downloads/release/python-365/)
- **Visual C ++ Build Tools** (https://visualstudio.microsoft.com/visual-cpp-build-tools/)
- **Rasa Core 0.10.2** (http://rasa.com/docs/core/installation/)
- **Rasa NLU 0.12.13** (http://rasa.com/docs/nlu/installation/)
- **Ngrok** (https://ngrok.com/download)
- **Telegram** (https://telegram.org/)

Installation
------------

**1. Install Python 3.6.5**

**2. Install Visual C ++ Build Tools**

**3. Install Rasa Core through the command line**

    `pip install rasa_core == 0.10.2`

**4. Install Rasa NLU**

    `pip install rasa_nlu == 0.12.3`

**5. Add the spacy pipeline to the Rasa NLU**

    `pip install rasa_nlu [spacy]`

**5. Add the language model to spacy**

    `python -m spacy download en_core_web_md`

    `python -m spacy link en_core_web_md`

**6. Install Ngrok and specify your Authentication Token on https://dashboard.ngrok.com/auth**

    `ngrok authtoken <my_token>`

**7. Install plotly**

    `pip install plotly`


Configuration
------------

**1. First, create the database by launching (in the 'db' directory)**

    `python db_init.py`

**2. Modify the file "chart.py" by specifying your Username and API key of Plot.ly**


Training the bot
---------

**To generate the model after any modification of training data or domain**

    `python nlu_model.py`

**To train the model automatically**

    `python train_init.py`

**To train the model online (manual training)**

    `python train_online.py`


Test the bot
---------

**To test the bot on the command line**

    `python run_bot.py`


Accessing the bot via Telegram
------------

**1. Using Ngrok, open an HTTP connection on a given port**

    `ngrok http <port>`

**2. Launch the Python script by specifying the URL generated by Ngrok (as string) and the port number**

    `python run_telegram.py <URL> <port>`

**3. Access the bot "Max" on Telegram (example of username: @dr_max_bot)**