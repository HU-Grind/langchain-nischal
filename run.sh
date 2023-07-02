#!/bin/bash

python3 -m venv env
source env/bin/activate
pip install langchain openai python-dotenv
python3 quickStartGuide.py