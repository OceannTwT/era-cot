import json
import logging

# from config import args
prompt_prefix = '''Given a sentence, all entities, and all explicit relationships within the sentence. 
Infer all possible implicit relationships between entities.
For each pair of entities, infer up to '''

prompt_mid = ''' implicit relationships.
Every relationship stated as a triple: (E_A, E_B, Relation)\nSentence: '''

prompt_suffix = '''\nRelation: '''

def get_infer_num(args):
    return args.infer_num

def get_infer_prompt(args, entities, relation_ext, sent):
    relation_prompt = (prompt_prefix + get_infer_num(args) + prompt_mid
                            + sent + "\nExplicit Relationships:: " + relation_ext
                                + "\nEntities: " + entities + prompt_suffix)
    return relation_prompt