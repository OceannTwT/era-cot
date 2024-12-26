import json
import logging

# from config import args
prompt_prefix = '''Remember your job: 
1、Following the input and output format, aligning with the length and context.

Example:

1:
Input: The answer choice is (E) house.

Output: E

2:
Input: Answer: (C) have lunch

Output: C

3:
Input: (B)

Output: B

4:
Input: A) new perspective

Output: A

'''

prompt_suffix = '''Your task: \nInput: {real_input} \n\nOutput: '''

def get_formulate_prompt(not_formulated_form):
    this_suffix = prompt_suffix
    this_suffix = this_suffix.replace("{real_input}", not_formulated_form)
    relation_prompt = (prompt_prefix + this_suffix)
    return relation_prompt