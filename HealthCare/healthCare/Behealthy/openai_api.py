
# chatbot/openai_api.py
import openai

# Set your OpenAI API key
openai.api_key = "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"

def generate_response(prompt):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()
