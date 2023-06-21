from config import *
# import poe
import module.deepai as deepai
import random
import json

class gptModel:
    def __init__(self, model, token, timeout = 30, max_retry = 5):
        self.model = model
        self.token = token
        self.timeout = timeout
        self.max_retry = max_retry

        try:
            # self.client = poe.Client(token)
            self.client = deepai.ChatCompletion()
        except:
            raise Exception("Can't connect to GPT server")
        
    def send(self, prompt):
        res = ""
        for _ in range(self.max_retry):
            try:
                # self.client.send_chat_break(self.model)
                # for chunk in self.client.send_message(self.model, prompt, timeout=poeTimeout):
                #     pass

                # x = chunk['text']
                x = ""
                messages = [
                    {"role": "user", "content": prompt}
                ]
                for chunk in self.client.create(messages):
                    x += chunk
                
                x = x.split("@finish")
                if len(x) < 2:
                    continue
                
                res = x[0]

                break
            except:
                raise Exception("Can't send message to GPT server")
        return res
