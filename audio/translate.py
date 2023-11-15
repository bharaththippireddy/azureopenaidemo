import os
import openai

openai.api_type = "azure"
openai.api_base = "https://neyaheurope.openai.azure.com/"
openai.api_version = "2023-09-01-preview"
openai.api_key = os.getenv("OPENAI_API_KEY")

audio_file=open("sample_french.mp3","rb")

response=openai.Audio.translate(
  model="whisper-1",
  deployment_id="audio_demo",
  file=audio_file
)

print(response)



