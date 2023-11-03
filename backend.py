import openai

class Chatbot:
    def __init__(self):
        openai.api_key = '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'

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine = "text-davinci-003",
            prompt=user_input,
            max_tokens=2000,
            temperature=0.5
        ).choice[0].text
        return response

if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a joke about birds")
    print(response)
