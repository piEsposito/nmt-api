from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import os

# downloads the model during build to speed up scaling from 59 sec to 16 sec

from dotenv import load_dotenv
load_dotenv()

mname = os.getenv("MODEL_NAME")

model = AutoModelForSeq2SeqLM.from_pretrained(mname)
tokenizer = AutoTokenizer.from_pretrained(mname)