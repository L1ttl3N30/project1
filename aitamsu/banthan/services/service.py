from openai import OpenAI

from django.conf import settings

from grading.prompts.task2_prompt import PROMPT

client = OpenAI(api_key=settings.OPENAI_API_KEY)


def grade_essay(question, essay):

    completion = client.chat.completions.create(

        model="gpt-5",

        messages=[

            {
                "role": "system",
                "content": PROMPT
            },

            {
                "role": "user",
                "content":
                f"Question:\n{question}\n\nEssay:\n{essay}"
            }

        ],

        temperature=0.2
    )

    return completion.choices[0].message.content