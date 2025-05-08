from prompts import get_chat_prompt, get_user_prompt
from llm_connection import get_client_lm_studio
from time_calc import time_it
from datetime import datetime
import pandas as pd
from prompts import assistant_prompt
import datetime

messages = [
    {"role": "system", "content": assistant_prompt}
]

execution_context = {
    'client': get_client_lm_studio,
    'model': "TheBloke/CodeLlama-7B-Instruct-GGUF"
}


def chat_with_llm(user_prompt):
    messages.append({"role": "user", "content": user_prompt})


    client = execution_context["client"]()

    user_prompt = get_user_prompt(row['code_block'])

    start_time = datetime.now()
    completion = client.chat.completions.create(
        model=execution_context["model"],
        messages=get_chat_prompt(user_prompt),
        temperature=0.7,
    )
    end_time = datetime.now()

    llm_complete_result = completion.choices[0].message.content

    print(str(end_time - start_time))
    print(llm_complete_result)

    assistant_reply = response['choices'][0]['message']['content']
    messages.append({"role": "assistant", "content": assistant_reply})

    return assistant_reply

while True:
    response = chat_with_llm(user_input)
    print(f"Assistant: {response}")