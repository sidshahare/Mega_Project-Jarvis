import os
import openai

# Fetch the API key from environment variable or use the default value provided
openai.api_key = os.getenv("OPENAI_API_KEY", "sk-PRRRp3noUQ1QMbA8dOIf_t5s75q9I3t2u8MBZi0TTUT3BlbkFJbpi7nYbayWx6Thw27da6rZJTmbDujzS1MTMVe6bjoA")

# Create the completion
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud"},
        {"role": "user", "content": "What is coding?"}
    ]
)

# Print the response
print(response.choices[0].message['content'])
