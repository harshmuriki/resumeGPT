import requests
# from .. import secrets
# api_key = "687d53640c0fb0375cec6a0e04112f87712813e28c41dda231c7683620139f70"
api_key = "d538cfc64fdf6a835c9249d59ada38062b784ad2b37d5cf9f70fe4b98eef001d"
# model = "llama-2-7b-chat"
CONTEXT_STORED = 5


class LlamaThread:
    def __init__(self, model):
        self.model = model
        self.stored_messages = []

    def start(self):
        url = f"https://api.together.xyz/instances/start?model=togethercomputer%2F{self.model}"
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        response = requests.post(url, headers=headers)

    def stop(self):
        url = f"https://api.together.xyz/instances/stop?model=togethercomputer%2F{self.model}"
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        requests.post(url, headers=headers)
        print("EXECUTION STOPPED")

    def ask_question(self, question):
        url = "https://api.together.xyz/inference"

        payload = {
            "model": f"togethercomputer/{self.model}",
            "prompt": f"{question}",
            "max_tokens": 512,
            "stop": "",
            "temperature": 0.7,
            "top_p": 0.7,
            "top_k": 50,
            "repetition_penalty": 1
        }
        headers = {
            "Authorization": f"Bearer {api_key}"
        }
        # response = requests.post(url, json=payload, headers=headers)

        # answer = str(response.json()["output"]["choices"][0]["text"])

        # return answer

        try:
            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 200 and "choices" in response.json()["output"]:

                answer = str(response.json()["output"]["choices"][0]["text"])
                # if "<|END|>" in answer:
                #     answer.replace("<|END|>", "")

                # # Try to adjust context size dynamically
                # if len(self.stored_messages) > CONTEXT_STORED:
                #     self.stored_messages.pop(0)
                self.stored_messages.append((question, answer))
                return answer
            else:
                print("error:", response.json()["output"])

        except requests.exceptions.RequestException as e:
            print(f"An exception was thrown {e}")
            self.stop()

    def format_prompt(self, question, context):
        documentation_text = context
        prompt = f"Answer questions based on this context:\n{documentation_text}"

        # prompt += "\n\nThe following is the chat history:\n"
        # for (question_past, answer) in self.stored_messages:

        #     prompt += f"Question: {question_past}\n"
        #     prompt += f"Answer: {answer}\n"

        prompt += f"Question: {question}<|END|>"

        return prompt.strip()

    def get_chat_history(self):
        history_string = ""
        for (question_past, answer) in self.stored_messages:
            history_string += f"{question_past}\n"
            answer = str(answer)
            if "<|END|>" in answer:
                answer.replace("<|END|>", "")
            history_string += f"{answer}\n"
        return history_string

    def clear_chat_history(self):
        self.stored_messages = []


def get_chat_history(self):
    history_string = ""
    for (question_past, answer) in self.stored_messages:
        history_string += f"{question_past}\n"
        history_string += f"{answer}\n"
    return history_string


def clear_chat_history(self):
    self.stored_messages = []
