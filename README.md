# HR_Interview_Bot
HR Interview bot: Bot will ask interview questions and get the answers and validate and show report to you and HR.

Create Virtual environment
* virtualenv --python=python3.6 env

* source env/bin/activate

install both Rasa and Rasa X using pip:

* pip3 install rasa-x --extra-index-url https://pypi.rasa.com/simple

Start Conversation:

* rasa run actions & rasa shell

### Train Own Custom Intent and Entities:

(1) Rasa NLU Training - build intent, entity classifier model
(2) Rasa Core Training - model will understand the conversations with the intent & entity

##### Add New Intent:
* domain.yml - intents to add new intent

##### Add New Entity:
* domain.yml - entities to add new entity

##### Add New Action:
* domain.yml - actions to add new action

##### Add New Action Template Text:
* domain.yml - templates to add new text for action

##### Add New Slot:
* domain.yml - slots to add new entity name with the type

##### Start Training
* rasa train

##### Test bot
* rasa shell

