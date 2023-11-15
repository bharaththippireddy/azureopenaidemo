import os
import openai
openai.api_type = "azure"
openai.api_base = "https://neyahopenai.openai.azure.com/"
openai.api_version = "2023-06-01-preview"
openai.api_key = os.environ["OPENAI_API_KEY"]

response = openai.Embedding.create(
    input="learn share grow",
    engine="embed_demo"
)

print(response)
print(response['data'][0]['embedding'])