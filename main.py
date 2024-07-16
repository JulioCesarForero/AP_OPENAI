import os
from dotenv import load_dotenv
from openai import OpenAI

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener las variables de entorno
api_key = os.getenv('api_key')
api_base = os.getenv('api_base')

client = OpenAI(api_key=api_key, base_url=api_base)

response = client.chat.completions.create(
  model="gpt-3.5-turbo-0125",
  response_format={ "type": "json_object" },
  messages=[
    {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
    {"role": "user", "content": "Who won the last two futboll soccer world cup series ?"}
  ]
)
print(response.choices[0].message.content)