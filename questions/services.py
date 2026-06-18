import os
import re
import json
import hashlib

from openai import OpenAI
from dotenv import load_dotenv

from .models import (
    Question,
    QuestionBank,
    Subject
)

from .utils import build_prompt


load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_questions(data):

    prompt = build_prompt(data)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert question generator. "
                    "Always return valid JSON."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7
    )

    content = response.choices[0].message.content

    content = re.sub(
        r"^```json\s*|\s*```$",
        "",
        content.strip(),
        flags=re.DOTALL
    )

    print("========== OPENAI RESPONSE ==========")
    print(content)
    print("====================================")

    try:

        questions = json.loads(content)

        print("PARSED QUESTIONS:")
        print(questions)

        return questions

    except Exception as e:

        print("JSON ERROR:", e)

        return []
    

def save_question_bank(subject_name, questions, concepts=None, bank_name=None):
    subject_obj, _ = Subject.objects.get_or_create(
        name=subject_name
    )

    questions_hash = hashlib.md5(
        json.dumps(questions, sort_keys=True).encode()
    ).hexdigest()

    existing_bank = QuestionBank.objects.filter(hash=questions_hash).first()
    if existing_bank:
        return existing_bank

    tags = ",".join(concepts or [])

    name = bank_name or f"{subject_name} Question Bank"

    bank = QuestionBank.objects.create(
        name=name,
        hash=questions_hash,
        tags=tags,
    )

    for q in questions:
        Question.objects.create(
            question_bank=bank,
            subject=subject_obj,
            question_text=q["question"],
            options=q["options"],
            answer=q["answer"]
        )

    return bank
