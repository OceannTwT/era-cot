export OPENAI_KEY=""
export PYTHONPATH=./

python main.py --dataset CommonsenseQA \
    --engine gpt-3.5 \
    --temperature 0.3 \
    --api_key $OPENAI_KEY \