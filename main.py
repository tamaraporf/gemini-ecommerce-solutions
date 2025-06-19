import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

CHAVE_API_GOOGLE = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=CHAVE_API_GOOGLE)
MODELO_ESCOLHIDO = "gemini-1.5-flash"

# interação com o gemini
prompt_sistema = "liste o nome dos produtos, e ofereça uma breve descrição"

# ajusta configs
# aqui vou configurar quanto objetivo ou não será meu modelo
configuracao_modelo = {
    "temperature": 0.1,  # criatividade do modelo
    "top_p": 1,  # critérioso ou n
    "top_k": 2,  # numero de palavras mais proximas
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# config da interação com a API
# construtor - define o modelo e a instrução
llm = genai.GenerativeModel(
    model_name=MODELO_ESCOLHIDO,
    system_instruction=prompt_sistema,
    generation_config=configuracao_modelo,
)

pergunta = "Liste três produtos de moda sustentável para ir ao shopping"

resposta = llm.generate_content(pergunta)

print(f"A resposta gerada para pergunta é: {resposta.text}")
