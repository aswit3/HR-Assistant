# HR_Interview_Bot
HR Interview bot: Bot will ask interview questions and get the answers and validate and show report to you and HR.

Create Virtual environment
* virtualenv --python=python3.6 env

* source env/bin/activate

install both Rasa and Rasa X using pip:

* pip3 install rasa-x --extra-index-url https://pypi.rasa.com/simple


### Train Own Custom Intent and Entities:

* Rasa NLU Training - build intent, entity classifier model
* Rasa Core Training - model will understand the conversations with the intent & entity

##### CREATE NEW PROJECT:

* rasa init --no-prompt

##### INSTALL RASA NLU TRAINER:

* sudo npm i -g rasa-nlu-trainer

##### RUN RASA NLU TRAINER:

* rasa-nlu-trainer --source data/data.json

##### TRAIN NLU MODEL:

* rasa train nlu

##### Test NLU MODEL:

* rasa shell nlu

##### TRAIN Dialogue Management:

* rasa train

##### TEST Dialogue Management:

* rasa shell

##### INTERACTIVE TRAIN:

* rasa interactive

##### Note:
before interactive if you have custom actions Actions.py, you must run on this comment in another terminal.

* rasa run actions 
* rasa interactive

####### Main Demo in terminal

* rasa run actions && rasa shell

### More Infromation:
###### Visualisation at 
* http://localhost:5006/visualization.html.

###### Add New Intent:
* domain.yml - intents to add new intent

###### Add New Entity:
* domain.yml - entities to add new entity

###### Add New Action:
* domain.yml - actions to add new action

###### Add New Action Template Text:
* domain.yml - templates to add new text for action

###### Add New Slot:
* domain.yml - slots to add new entity name with the type

