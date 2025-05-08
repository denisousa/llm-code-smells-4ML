import pandas as pd
from prompts import get_chat_prompt1, get_chat_prompt2, get_user_prompt1, user_prompt2
from time_calc import time_it
from datetime import datetime
import pandas as pd
import gc
import re
from llm_connection import get_azure_client
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

pattern = r"\b[Yy][Ee][Ss]\b"


execution_context = {
    'client': get_azure_client,
    'model': 'gpt-4o'
    # 'model': "TheBloke/CodeLlama-7B-Instruct-GGUF"
}

# https://zenodo.org/records/12700065
df = pd.read_csv('code_blocks_sample_10_percent.csv')

@time_it
def main():
    for index, row in df.iterrows():
        if index == 5:
            break

        client = execution_context["client"]()

        user_prompt = get_user_prompt1(row['code_block'])

        start_time = datetime.now()
        completion = client.chat.completions.create(
            model=execution_context["model"],
            messages=get_chat_prompt1(user_prompt),
            temperature=0.7,
        )
        end_time = datetime.now()

        llm_complete_result = completion.choices[0].message.content
        print(str(end_time - start_time))
        print(llm_complete_result)

        matches = re.findall(pattern, llm_complete_result)
        if matches:
            completion = client.chat.completions.create(
                model=execution_context["model"],
                messages=get_chat_prompt2(user_prompt, llm_complete_result, user_prompt2),
                temperature=0.7,
            )
            llm_complete_result = completion.choices[0].message.content
            print(str(end_time - start_time))
            print(llm_complete_result)

            open('output.txt', 'w').write(row['code_block'] + '\n')


main()
