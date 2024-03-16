import torch
import time
import os
import json
from transformers import LlamaTokenizer, LlamaForCausalLM, AutoConfig
# from peft import PeftModel

def model_init(args):
    model_path = args.model_path # Replace to your model path
    # add_state_model_dir = "" # Option for PEFT
    device = torch.device("cuda:0")
    # adapter_len = 32
    # config = AutoConfig.from_pretrained(model_path, trust_remote_code=True, adapter_len = adapter_len)
    model = LlamaForCausalLM.from_pretrained(
        model_path,# config = config, 
        torch_dtype=torch.float16,
        # device_map='auto',
    ).to(device)
    tokenizer = LlamaTokenizer.from_pretrained(model_path, legacy=False)
    return model, tokenizer, device

def predict(args, prompt, model, tokenizer):
    # add_state_dict = torch.load(os.path.join(add_state_model_dir, "pytorch_model.bin"))
    # model.load_state_dict(add_state_dict, strict=False)
    inputs = tokenizer(prompt, return_tensors="pt").to('cuda')
    generate_ids = model.generate(**inputs, max_length=512, temperature=args.temperature)
    generate_ids = generate_ids[0][len(inputs["input_ids"][0]):-1]
    infer_res = tokenizer.decode(generate_ids)
    return infer_res
