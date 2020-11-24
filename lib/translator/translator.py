from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import time

class Translator:
    def __init__(self,
                 mname="Helsinki-NLP/opus-mt-en-roa"):
        self.model = AutoModelForSeq2SeqLM.from_pretrained(mname)
        self.tokenizer = AutoTokenizer.from_pretrained(mname)

    def translate(self,
                  text):
        tac = time.time()

        as_tensor = self.tokenizer.prepare_seq2seq_batch(src_texts=[text])
        gen = self.model.generate(**as_tensor)
        translated = self.tokenizer.batch_decode(gen, skip_special_tokens=True)[0]

        tic = time.time()

        return {
            'translation': translated,
            'elapsed_time': tic - tac
        }
