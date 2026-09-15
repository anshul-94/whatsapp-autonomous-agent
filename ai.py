import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_reply(chat_history):

    response = client.chat.completions.create(

        model="openai/gpt-oss-20b",

        include_reasoning=False,

        reasoning_effort="low",

        temperature=0.6,

        max_completion_tokens=300,

        messages=[
            {
                "role": "system",
                "content": """
You are replying to a WhatsApp friend.

Reply naturally like a real Indian person.

Understand Hindi, Hinglish and English.

Rules:
- Read the whole conversation.
- Reply specifically to the LAST incoming message.
- Keep the reply short.
- Be casual and natural.
- Do not repeat the same generic reply.
- Do not invent locations, timings or facts.
- If the person asks for a specific time, answer only if the conversation gives enough information.
- If information is missing, ask a short clarification.
- Return ONLY the WhatsApp reply.
"""
            },
            {
                "role": "user",
                "content": chat_history
            }
        ]
    )

    reply = response.choices[0].message.content

    if reply is None:
        return ""

    return reply.strip()
