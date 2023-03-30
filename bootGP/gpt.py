import openai
import audio 

openai.api_key = "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"

def generete_response(prompt):
    model_engine = "text-davinci-003"
    prompt = (f"{prompt}")

    completions = openai.Completion.create(
        engine = model_engine,
        prompt = prompt,
        max_tokens=1024,
        n = 1,
        stop = None,
        temperature = 0.5,
    )

    message = completions.choices[0].text
    return message.strip()

prompt = input("Coloque sua pergunta aqui: ")
response = generete_response(prompt)

print(response)