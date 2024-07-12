import json
import logging
import re

from config import args
from utils import write_json, print_now, load_data, print_exp, mkpath
from src.format.entity_extraction_prompt import get_ner_list, get_ner_prompt, ner_sentence
from src.model.llama2_predict import predict, model_init
from src.format.relation_extract import get_extract_prompt
from src.format.relation_infer import get_infer_prompt
from src.format.discrimination import get_discrimination_prompt
from src.format.qa import get_qa_prompt
from src.model.GPTFactory.GPTFactory import GPTFactory
from transformers import LlamaTokenizer, LlamaForCausalLM, AutoConfig

def run_llama():
    ner_prompt = get_ner_prompt(args.type_list_file)
    question, answer, ids = load_data(args)
    model, tokenizer, device = model_init(args)
    for idx, element in enumerate(question):
        prompt = ner_sentence(ner_prompt, element)
        entities = predict(args, prompt, model, tokenizer)
        prompt = get_extract_prompt(entities, element)
        relation_ext = predict(args, prompt, model, tokenizer)
        prompt = get_infer_prompt(args, entities, relation_ext, element)
        relation_inf = predict(args, prompt, model, tokenizer)
        relation = relation_ext
        try: # single evaluate for better performance
            valid_relation = ""
            ralation_inf_list = re.findall(r'[(](.*?)[)]', relation_inf) 
            for rk, item in enumerate(ralation_inf_list):
                item = "(" + item + ")"
                prompt = get_discrimination_prompt(args, entities, relation_inf, element)
                scores = predict(args, prompt, model, tokenizer)
                if int(scores[0]) >= 6:
                    valid_relation = valid_relation + item
            relation = relation +valid_relation
        except Exception as e: 
            relation = relation_ext
        prompt = get_qa_prompt(args, entities, relation, element)
        answer = predict(args, prompt, model, tokenizer)
        print(answer)

def run_gpt():
    ner_prompt = get_ner_prompt(args.type_list_file)
    question, answer, ids = load_data(args)
    gpt_interface = GPTFactory("gpt-3.5-turbo", args.api_key)
    # model, tokenizer, device = model_init(args)
    for idx, element in enumerate(question):
        prompt = ner_sentence(ner_prompt, element)
        gpt_interface.add_user_conv(prompt)
        entities = gpt_interface.predict()
        gpt_interface.clear_conv()

        prompt = get_extract_prompt(entities, element)
        gpt_interface.add_user_conv(prompt)
        relation_ext = gpt_interface.predict()
        gpt_interface.clear_conv()

        prompt = get_infer_prompt(args, entities, relation_ext, element)
        gpt_interface.add_user_conv(prompt)
        relation_inf = gpt_interface.predict()
        gpt_interface.clear_conv()

        relation = relation_ext
        try: # single evaluate for better performance
            valid_relation = ""
            ralation_inf_list = re.findall(r'[(](.*?)[)]', relation_inf) 
            for rk, item in enumerate(ralation_inf_list):
                item = "(" + item + ")"
                prompt = get_discrimination_prompt(args, entities, relation_inf, element)
                gpt_interface.add_user_conv(prompt)
                scores = gpt_interface.predict()
                gpt_interface.clear_conv()
                if int(scores[0]) >= 6:
                    valid_relation = valid_relation + item
            relation = relation +valid_relation
        except Exception as e: 
            relation = relation_ext
        prompt = get_qa_prompt(args, entities, relation, element)
        gpt_interface.add_user_conv(prompt)
        answer = gpt_interface.predict()
        gpt_interface.clear_conv()
        print(answer)

if __name__ == '__main__':
    print_exp(args) 
    if args.engine == 'llama2-7b':
        run_llama()
    elif args.engine == "gpt-3.5":
        run_gpt()