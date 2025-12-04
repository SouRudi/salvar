from google import genai
import textwrap

FUNDO = "\033[1;107m"
VERMELHO = "\033[91m"
AZUL = "\033[94m"
NEGRITO = "\033[1m"
RESET = "\033[0m"

client = genai.Client(api_key="AIzaSyBgNxR1UUjcUK6P01uZEjroSGWICw4uogg")

while True:
    pergunta = input(f"   Digite sua pergunta para o modelo Gemini-2.5 (ou 'sair' para encerrar): {VERMELHO+NEGRITO}")

    if pergunta.lower() in ["sair", "exit", "quit"]:
        print(f"{RESET}Encerrando...")
        break

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config={
            "system_instruction": "Responda sempre de forma aleatória."
        },
        contents=pergunta
    )


    print(f"\n{RESET}Resposta do modelo Gemini-2.5:\n")
    print(f"{AZUL+NEGRITO}      ",response.text,f"{RESET}\n")
    print("-" * 100)
