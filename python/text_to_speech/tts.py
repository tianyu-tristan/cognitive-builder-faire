import os
import json
from os.path import join, dirname, expanduser
from dotenv import load_dotenv
from watson_developer_cloud import TextToSpeechV1
import yaml

def convert_to_audio(tts, text):
  with open('output.wav', 'wb') as audio_file:
    audio_file.write(
      tts.synthesize(
        text,
        accept="audio/wav",
        voice="en-US_AllisonVoice"))

def main():
  credentials = yaml.load(open(expanduser('~/.ssh/api_cred.yml')))['watson']
  tts = TextToSpeechV1(
    username=credentials['TTS_USERNAME'],
    password=credentials['TTS_PASSWORD'],
    x_watson_learning_opt_out=True)  # Optional flag

  text = "Watson loves galvanize and Seattle"
  convert_to_audio(tts, text)

if __name__ == '__main__':
  main()
