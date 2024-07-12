# ERA-CoT: Improving Chain-of-Thought through Entity Relationship Analysis

<p align="center">
<img src='https://img.shields.io/badge/Code%20License-Apache_2.0-green.svg'></a>
<img src='https://img.shields.io/badge/python-3.9+-blue.svg'>
<img src='https://img.shields.io/badge/Data%20License-CC%20By%20NC%204.0-red.svg'>
</p>

This is the codebase of the paper: [ERA-CoT: Improving Chain-of-Thought through Entity Relationship Analysis](https://arxiv.org/abs/2403.06932).

![Framework of ERA-CoT](era-cot.png)


[2024/07/12]🔥 We are releasing the version 1.1 for running on GPT3.5 model.

[2024/05/17]🔥 We are happy to announce ERA-CoT has been accepted to ACL 2024 main conference!

[2024/03/28]🔥 We are releasing the version 1.0 for running on Llama2 model.

## How to Use

Update your environment for the required dependency. 

```shell
pip install -r requirement.txt
```

Get your Llama2 weight on https://huggingface.co/meta-llama/Llama-2-7b-chat-hf/tree/main, set up on default directory: /root/llama-2-7b-chat-hf (You can change the dir on era-cot/config.py)

Running the code on `Llama2`:

```shell
export PYTHONPATH=./

python main.py --dataset CommonsenseQA \
    --engine llama2-7b \
    --temperature 0.3 \
```

Running the code on `GPT3.5`:

```shell
export OPENAI_KEY=""
export PYTHONPATH=./

python main.py --dataset CommonsenseQA \
    --engine gpt-3.5 \
    --temperature 0.3 \
    --api_key $OPENAI_KEY \
```

## Set up for your dataset

* Upload your json version of dataset on era-cot/dataset.

* Setting for loading your dataset on utils.

### Example

```shell
if args.dataset.lower() == 'commonsenseqa':
      json_res = decoder.raw_decode(line)[0]
      choice = "Answer Choices:"
      for c in json_res["question"]["choices"]:
            choice += " ("
            choice += c["label"]
            choice += ") "
            choice += c["text"]
            q = json_res["question"]["stem"].strip() + " " + choice
            a = json_res["answerKey"]
            id = 'temp_{}'.format(idx)
      questions.append(q)
      answers.append(a)
      ids.append(id)
```

## Different Dataset Results

✨ERA-CoT

* Entity extraction on text and finds out all the explicit relationships mentioned in the text.
* Gradually infers the possible implicit relationships involved between entities based on the explicit relationships.
* Scores and filters the reliability of these implicit relationships.
* Finally answers questions based on these entity relationships. 

![Result](result.png)

## Citation

If you found that ERA-CoT helps your work, please cite:

```bibtex 
@article{liu2024era,
  title={ERA-CoT: Improving Chain-of-Thought through Entity Relationship Analysis},
  author={Liu, Yanming and Peng, Xinyue and Du, Tianyu and Yin, Jianwei and Liu, Weihao and Zhang, Xuhong},
  journal={arXiv preprint arXiv:2403.06932},
  year={2024}
}

```

## License
For academic and non-commercial use only.The whole project is under the CC-BY-NC 4.0 license. See [LICENSE](https://creativecommons.org/licenses/by-nc-sa/4.0/) for additional details.
