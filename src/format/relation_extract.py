import json
import logging

# from config import args
prompt_prefix = '''Given a sentence, and all entities within the sentence. 
Extract all relationships between entities which directly stated in the sentence.
Every relationship stated as a triple: (E_A, E_B, Relation).\nSentence: '''

prompt_suffix = '''\nRelation: '''

def get_extract_prompt(entities, sent):
    relation_prompt = prompt_prefix + sent + "\nEntities: " + entities + prompt_suffix
    return relation_prompt