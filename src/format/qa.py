import json
import logging

# from config import args
prompt_prefix = '''Given a sentence, all entities and all relationships within the sentence. 
Answering the question.
Every relationship stated as a triple: (E_A, E_B, Relation)\nSentence: '''

prompt_suffix = '''Please only give the only answer choice as (A,B,C,D,E). \nAnswer: '''

def get_qa_prompt(args, entities, relation, sent):
    relation_prompt = (prompt_prefix + sent + "\Entities: " + entities
                            + "\nRelationships:: " + relation
                                + "\nQuestion: " + sent + prompt_suffix)
    return relation_prompt