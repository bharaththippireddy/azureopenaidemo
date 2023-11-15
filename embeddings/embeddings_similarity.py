import os
import openai
import numpy as np

openai.api_type = "azure"
openai.api_base = "https://neyahopenai.openai.azure.com/"
openai.api_version = "2023-06-01-preview"
openai.api_key = os.environ["OPENAI_API_KEY"]

response = openai.Embedding.create(
    input=["you are good","you are awesome"],
    engine="embed_demo"
)

embedding_1 = response['data'][0]['embedding']
embedding_2 = response['data'][1]['embedding']

similarity_score = np.dot(embedding_1,embedding_2)

print(similarity_score*100,'%')
