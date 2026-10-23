# Geração de Embeddings com Ollama e Python

Este repositório contém um script Python para conexão com o **Ollama** local e geração de vetores de *embeddings* utilizando um modelo aberto.

---

## 📋 Pré-requisitos

1. **Python 3.10+**
2. **Ollama** instalado e em execução

---

## 🚀 Como Executar o Projeto

### 1. Baixar o Modelo no Ollama
No terminal, certifique-se de baixar o modelo de embeddings:
```bash
ollama pull nomic-embed-text
```

### 2. Instalar as Dependências
Com o ambiente Python ativo, instale as dependências:
```bash
pip install -r requirements.txt
```

### 3. Executar o Script
Para gerar os embeddings e visualizar os resultados no terminal:
```bash
python meu_script.py
```

---

## 📊 Exemplo de Saída Esperada

```text
Conectando ao Ollama local e gerando embeddings...
Texto fornecido: 'Tecnologia em Sistemas para Internet no IFRN'
Modelo utilizado: nomic-embed-text

=== RESULTADO DO EMBEDDING ===
 Dimensão/Tamanho do vetor: 768 números
 Primeiros 5 valores: [0.4086, 0.4600, -0.3708, 1.2210, -0.0590]
 Status: Embeddings gerados com sucesso!
```