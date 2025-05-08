system_prompt = '''
You are an expert system in finding code smells for Machine Learning.
'''

assistant_prompt = '''
NaN Equivalence Comparison Misused
**The NaN equivalence comparison is different from None comparison.**  
The result of `NaN == NaN` is False (40).

**Context**  
NaN equivalence comparison behaves differently from None equivalence comparison.

**Problem**  
While `None == None` evaluates to True, `np.nan == np.nan` evaluates to False in NumPy. Since Pandas treats `None` like `np.nan` for simplicity and performance reasons, a comparison of DataFrame elements with `np.nan` always returns False [4]. If developers are unaware of this, it may lead to unintended behavior in the code.

**Solution**  
Developers need to be cautious when using NaN comparisons.
'''

code = '''
data = {
    'A': [1, 2, np.nan, 4],
    'B': [None, 2, 3, 4]
}

df = pd.DataFrame(data)

# Problematic comparison: NaN and None are treated differently
for index, row in df.iterrows():
    if row['A'] == row['B']:
        print(f"Row {index}: A and B are equal")
    else:
        print(f"Row {index}: A and B are not equal")
'''

def get_user_prompt1(block_code):
    return f'''Could this code snippet be experiencing the code smell "NaN Equivalence Comparison Misused"?
    Answer with: yes or no

    code: {block_code}
    '''

user_prompt2 =  f'''What is the code snippet?'''

def get_chat_prompt1(user_prompt1):
    return [
            {"role": "system", "content": system_prompt},
            {"role": "assistant", "content": assistant_prompt},
            {"role": "user", "content": user_prompt1},
        ]

def get_chat_prompt2(user_prompt1, assistant_prompt2, user_prompt2):
    return [
            {"role": "system", "content": system_prompt},
            {"role": "assistant", "content": assistant_prompt},
            {"role": "user", "content": user_prompt1},
            {"role": "assistant", "content": assistant_prompt2},
            {"role": "user", "content": user_prompt2},
        ]