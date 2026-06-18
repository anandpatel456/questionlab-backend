import json


def build_prompt(data):

    return f"""
Generate {data['count']} questions.

Subject:
{data['subject']}

Concepts:
{', '.join(data['concepts'])}

Difficulty:
{data['difficulty']}

Question Type:
{data['question_type']}

Additional Instructions:
{data.get('instructions', '')}

Return ONLY valid JSON.

Format:

[
    {{
        "question": "Question text",
        "options": [
            "Option A",
            "Option B",
            "Option C",
            "Option D"
        ],
        "answer": "Correct Answer"
    }}
]
"""