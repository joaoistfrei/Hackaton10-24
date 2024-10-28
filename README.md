# WhatsApp Chatbot para Assistência a Manutentores

Esse projeto é um chatbot para WhatsApp que visa facilitar a rotina de manutenção, permitindo o processamento de áudios enviados pelo usuário para transformar as instruções em tópicos e oferecendo links e informações de ferramentas úteis.

## 📋 Funcionalidades

- **Transcrição e Resumo de Áudios**: Utilizando o modelo Whisper para transcrição e a API do ChatGPT para sintetizar o conteúdo em tópicos. O áudio contém instruções de tarefas diárias para os manutentores.
- **Consulta de Ferramentas**: Realiza busca em um arquivo `.csv` com informações sobre ferramentas, facilitando o acesso a códigos e especificações.
- **Sugestão de Links de Apoio**: Sugerir links relevantes para apoiar a execução das tarefas listadas.

## 🛠️ Tecnologias Utilizadas

- **Whisper**: Para transcrição de áudios em texto.
- **OpenAI ChatGPT**: Para processar e resumir o texto em tópicos claros e objetivos.
- **Python e bibliotecas de manipulação de dados**: Para análise do `.csv` e implementação das funções do bot.
- **Twilio API para WhatsApp**: Para envio e recebimento de mensagens pelo WhatsApp.

## 🚀 Como Funciona

1. **Recebimento de Áudio**: O usuário envia um áudio pelo WhatsApp, contendo instruções de manutenção.
2. **Transcrição e Processamento**:
   - O áudio é transcrito pelo Whisper.
   - O texto transcrito é enviado para o ChatGPT, que gera um resumo em tópicos das instruções.
3. **Busca de Ferramentas**:
   - O chatbot realiza consultas no arquivo `.csv` para encontrar ferramentas mencionadas nas instruções.
4. **Sugestão de Links**:
   - Com base nos tópicos extraídos, o chatbot sugere links úteis ao manutentor.

## 📂 Estrutura do Projeto


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

- **Privacidade**: Todos os dados transcritos são tratados com confidencialidade e utilizados exclusivamente para o propósito do projeto.
- **Limitações**: Para áudios muito extensos, o resumo pode ser sintetizado, focando apenas nas instruções principais.

## 👥 Contribuidores

- **João Pedro Machado Medeiros**
- **Lucas Augusto Moreira Barros**
- **Victor Hugo Rodrigues**
