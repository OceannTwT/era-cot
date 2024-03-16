import json
import logging

# from config import args
prompt_prefix = '''Given a sentence, and all uncertain relationships within the sentence. 
Score the confidence level of each relationship.
The confidence score ranges from 0 to 10, where a higher score indicates a higher likelihood of the relationship being correct.
Every relationship stated as a triple: (E_A, E_B, Relation).\nSententence: '''

prompt_suffix = '''\Scores: '''

def get_discrimination_prompt(args, entities, relation_inf, sent):
    relation_prompt = (prompt_prefix + sent + "\nExplicit Relationships:: " + relation_inf
                                + "\nEntities: " + entities + prompt_suffix)
    return relation_prompt