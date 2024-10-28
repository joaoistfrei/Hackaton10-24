# Telegram Chatbot @TranscreveAudiosBot para Assistência a Manutentores

Esse projeto é um chatbot para Telegram que visa facilitar a rotina de manutenção, permitindo o processamento de áudios enviados pelo usuário para transformar as instruções em tópicos e informações de ferramentas úteis.

## 📋 Funcionalidades

- **Transcrição e Resumo de Áudios**: Utilizando o modelo Whisper para transcrição e a API do ChatGPT para sintetizar o conteúdo em tópicos. O áudio contém instruções de tarefas diárias para os manutentores.
- **Consulta de Ferramentas**: Realiza busca em um arquivo `.csv` com informações sobre ferramentas, facilitando o acesso a códigos e especificações.

## 🛠️ Tecnologias Utilizadas

- **Whisper**: Para transcrição de áudios em texto.
- **OpenAI ChatGPT**: Para processar e resumir o texto em tópicos claros e objetivos.
- **Python e bibliotecas de manipulação de dados**: Para análise do `.csv` e implementação das funções do bot.
- **API Telegram**: Para envio e recebimento de mensagens pelo Telegram.

## 🚀 Como Funciona

1. **Recebimento de Áudio**: O usuário envia um áudio pelo Telegram para o bot @TranscreveAudiosBot, contendo instruções de manutenção.
2. **Transcrição e Processamento**:
   - O áudio é transcrito pelo Whisper.
   - O texto transcrito é enviado para o ChatGPT, que gera um resumo em tópicos das instruções.
3. **Busca de Ferramentas**:
   - O chatbot realiza consultas no arquivo `.csv` para encontrar ferramentas mencionadas nas instruções.

## 📂 Estrutura do Projeto
    ├── code<br>
    │   └── text-speech.py          # Script para transcrição e processamento do áudio <br>
    ├── files<br>
    │   ├── audioEx.wav             # Exemplo de arquivo de áudio para teste <br>
    │   └── codigosSAP.csv          # Base de dados com códigos de ferramentas<br> 
    ├── .gitignore                  # Arquivo para ignorar arquivos desnecessários no Git<br> 
    ├── README.md                   # Documentação do projeto <br>
    └── requirements.txt            # Dependências necessárias para o projeto<br>


## ⚙️ Configuração

1. **Instalação de dependências**:
   ```bash
   pip install -r requirements.txt

2. **Configuração das APIs**:
   Insira as credenciais da API do ChatGPT e do Twilio no arquivo .env.

3. **Execução**:
    ```bash
    python main.py

## 📌 Notas

- **Limitações**: Audios muito diferentes do contexto de atribuição de tarefas ou pouco especificos não funcionam bem.
- **Objetivo futuro**: No futuro esse mesmo bot poderia ser implementado em outros aplicativos como o Whatsapp mas a implementação é mais burocrática

## 👥 Contribuidores

- **João Pedro Machado Medeiros**
- **Lucas Augusto Moreira Barros**
- **Victor Hugo Rodrigues**
