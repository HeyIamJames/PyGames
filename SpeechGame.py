import sys
from wit import Wit

#actions dict > undefined 

actions = {
    'say': say,
    'merge': merge,
    'error': error,
}


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
