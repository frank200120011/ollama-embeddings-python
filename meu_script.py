import ollama

response = ollama.embeddings(
    model='nomic-embed-text',
    prompt='Testando geração de embeddings no Windows'
)

print("Vetor de Embedding gerado:")
print(response['embedding'])


def gerar_embeddings():
    # 1. Definir o texto simples para teste
    texto = "Tecnologia em Sistemas para Internet no IFRN"
    modelo = "nomic-embed-text"  # Modelo de embeddings carregado no Ollama

    print(f"Conectando ao Ollama local e gerando embeddings...")
    print(f"Texto fornecido: '{texto}'")
    print(f"Modelo utilizado: {modelo}\n")

    try:
        # 2. Conectar ao Ollama localmente e gerar os embeddings
        resposta = ollama.embeddings(
            model=modelo,
            prompt=texto
        )

        # 3. Extrair o vetor numérico da resposta
        vetor_embedding = resposta['embedding']

        # 4. Exibir o sumário e as informações do vetor gerado
        tamanho_vetor = len(vetor_embedding)
        primeiros_valores = vetor_embedding[:5]  # Pega os 5 primeiros elementos

        print("=== RESULTADO DO EMBEDDING ===")
        print(f" Dimensão/Tamanho do vetor: {tamanho_vetor} números")
        print(f" Primeiros 5 valores: {primeiros_valores}")
        print(" Status: Embeddings gerados com sucesso!")

    except Exception as e:
        print(f"Erro ao conectar ou gerar embeddings: {e}")

if __name__ == "__main__":
    gerar_embeddings()