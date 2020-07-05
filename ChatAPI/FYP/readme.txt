Welcome

python3 -m venv venv

To activate Virtual environment
-- source venv/bin/activate

To deactivcate
-- deactivate

to know volume used in ec2
- df -hT /dev/xvda1 

#https://forum.rasa.com/t/rest-api-implementation/12624/

Running Rasa
- rasa train
- rasa run actions & rasa shell

  for api
- rasa run -m models --enable-api --cors “*” --debug
- http://localhost:5005/webhooks/rest/webhook
- POST => body -> {"sender":"Patil92","message":"Hi"} 

nlu.md
Keywords Must be written in nlu.md like this
## intent:Patil
- Patil
- xxx   ==> these are keywords for intent Patil

--------------------------------------------
to know ports running
-- netstat -ltnp
-- kill -9 'PID'

--------------------------------------------
stories.md
## PatilsWorld
* Patil
  - utter_welcomePatil

-name anything for our convinience
-intent must be started with *
- the answer we are going to reply must be written in domain.yml with utter_xxxx


domain.yml
- intent and actions must be added
- utter must be added in responses

utter_welcomePatil:
  - text: "Welcome To Patil92 World..!!"




