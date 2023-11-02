import openai
import os
import click

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_sql(user_input, model_no):

    completion = openai.ChatCompletion.create(
      model= openai.FineTuningJob.list(limit=3)["data"][model_no-1]['fine_tuned_model'],
      messages=[
        {"role": "system", "content": "Jaarus is SQL Parser who learns scghema and generates mysql query"},
        {"role": "user", "content": user_input}
      ],
      temperature=0.45,
      max_tokens=2048,
      top_p=0.49,
      frequency_penalty=0,
      presence_penalty=0
    )
    
    return completion.choices[0].message["content"].strip()
