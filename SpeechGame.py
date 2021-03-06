import sys
from wit import Wit
import logging
client = Wit(token, actions)
client.logger.setLevel(logging.WARNING)

#actions dict > undefined 

actions = {
    'say': say,
    'merge': merge,
    'error': error,
    'send': send,
    'getForecast': get_forecast,
}
resp = client.message('action')

session_id = '1'
context0 = {}
context1 = client.run_actions(session_id, 'who are you?', context0)
print('name: ' + str(context1))

resp = client.converse('1')

from chatterbot import ChatBot
chatbot = ChatBot("Bot1")
from chatterbot.training.trainers import ListTrainer

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

response = chatbot.get_response("Good morning!")


chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)

client = Wit(access_token=access_token, actions=actions)
client.interactive()

#params

--user-agent 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.77 Safari/535.7' \

audio/x-flac; rate=16000;

$ cat speech.py
import urllib2
url = "https://www.google.com/speech-api/v1/recognize?xjerr=1&client=chromium&lang=en-US"
audio = open('rainspain.flac','rb').read()
headers={'Content-Type': 'audio/x-flac; rate=16000', 'User-Agent':'Mozilla/5.0'}
request = urllib2.Request(url, data=audio, headers=headers)
response = urllib2.urlopen(request)
print response.read()


"permissions": {
  "audio-capture" : {
    "description" : "Audio capture"
  },
  "speech-recognition" : {
    "description" : "Speech recognition"
  }
}

<form>
  <input type="text" class="txt">
  <div>
    <label for="rate">Rate</label><input type="range" min="0.5" max="2" value="1" step="0.1" id="rate">
    <div class="rate-value">1</div>
    <div class="clearfix"></div>
  </div>
  <div>
    <label for="pitch">Pitch</label><input type="range" min="0" max="2" value="1" step="0.1" id="pitch">
    <div class="pitch-value">1</div>
    <div class="clearfix"></div>
  </div>
  <select>

  </select>
</form>

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
print (sum(arr))


