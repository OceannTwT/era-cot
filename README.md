# ERA-CoT: Improving Chain-of-Thought through Entity Relationship Analysis

This is the codebase of the paper: [ERA-CoT: Improving Chain-of-Thought through Entity Relationship Analysis](https://arxiv.org/abs/2403.06932).

![Framework of ERA-CoT](era-cot.png)

ERA-CoT performs entity extraction on text and finds out all the explicit relationships mentioned in the text, gradually infers the possible implicit relationships involved between entities based on the explicit relationships, then scores and filters the reliability of these implicit relationships, and finally answers questions based on these entity relationships. 

🔥 We are releasing the version 1.0 for running on Llama2 model.

## How to Use

Update your environment for the required dependency. 

```shell
pip install -r requirement.txt
```

Get your Llama2 weight on https://huggingface.co/meta-llama/Llama-2-7b-chat-hf/tree/main, set up on default directory: /root/llama-2-7b-chat-hf (You can change the dir on era-cot/config.py)

Running the code:

```shell
python main.py --dataset gsm8k \
--engine llama2-7b \
--temperature 0.3
```


## Citation

If you ERA-CoT help your work, please cite:

```bibtex 
@misc{liu2024eracot,
      title={ERA-CoT: Improving Chain-of-Thought through Entity Relationship Analysis}, 
      author={Yanming Liu and Xinyue Peng and Tianyu Du and Jianwei Yin and Weihao Liu and Xuhong Zhang},
      year={2024},
      eprint={2403.06932},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}