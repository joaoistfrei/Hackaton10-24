import os
import json
import difflib
import whisper
import pandas as pd
import logging
from openai import OpenAI
from telegram import Update
from telegram.ext import ContextTypes

# Configurações de API e Caminho
TELEGRAM_TOKEN = "Token"
OPENAI_API_KEY = "API_key"
AUDIO_SAVE_PATH = './files'  # Caminho para salvar áudios temporários

# Inicializar logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Inicializar modelo Whisper e OpenAI
whisper_model = whisper.load_model("medium")
openai_client = OpenAI(api_key=OPENAI_API_KEY)

# Carregar dados CSV (exemplo)
sap_data = pd.read_csv('codigosSAP.csv')  # Certifique-se que o arquivo está neste caminho
tools = {row['Descrição do Material/Equipamento']: row['Código SAP'] for _, row in sap_data.iterrows()}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Olá! O chat está funcionando. Envie um áudio em português para transcrever e processar.")

async def handle_audio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Recebendo o áudio...")

    # Verificar se a mensagem é uma mensagem de voz ou um arquivo de áudio
    if update.message.voice:
        audio_file = await context.bot.get_file(update.message.voice.file_id)
        audio_path = os.path.join(AUDIO_SAVE_PATH, "audio_received.ogg")
    elif update.message.audio:
        audio_file = await context.bot.get_file(update.message.audio.file_id)
        audio_path = os.path.join(AUDIO_SAVE_PATH, "audio_received.mp3")
    else:
        await update.message.reply_text("Por favor, envie um áudio em formato de mensagem de voz ou arquivo de áudio.")
        return

    logger.info(f"Baixando arquivo: {audio_file.file_id} como {audio_path}")

    # Baixar o arquivo de áudio
    await audio_file.download_to_drive(custom_path=audio_path)

    await update.message.reply_text("Áudio recebido. Transcrevendo...")

    # Transcrever áudio com Whisper
    transcription = whisper_model.transcribe(audio_path, language="pt")
    transcription_text = transcription["text"]

    # Exibir transcrição no chat
    await update.message.reply_text(f"Transcrição do áudio:\n{transcription_text}")

    await update.message.reply_text("Processando a transcrição com o OpenAI...")

    # Formatar e enviar a transcrição ao OpenAI
    entrada = (
        "Olá ChatGPT, retorne o texto a seguir separado em tópicos e liste as atividades com nome do serviço, "
        "problemas reportados, recomendações, e as ferramentas a serem utilizadas para cada serviço, com os respectivos "
        "códigos SAP das ferramentas abaixo. Lembre de formatar bonito, por favor!\n\n"
        "Lista de ferramentas e códigos SAP:\n" + json.dumps(tools) + "\n\n"
        "Texto transcrito:\n" + transcription_text
    )

    response = openai_client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": entrada}],
    )

    # Enviar a resposta do modelo ao usuário
    bot_response = response.choices[0].message.content
    await update.message.reply_text(f"Resumo das atividades:\n{bot_response}")

    await update.message.reply_text("Qual ferramenta você gostaria de pesquisar? (Digite 'Sair' para encerrar)")

async def search_tools(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.text.lower() == "sair":
        await update.message.reply_text("Você saiu do chat. Até a próxima!")
        return

    tool_name = update.message.text
    matches = difflib.get_close_matches(tool_name, tools.keys(), n=1, cutoff=0.5)

    if matches:
        tool = matches[0]
        tool_code = tools[tool]
        await update.message.reply_text(f"Ferramenta: {tool}, Código SAP: {tool_code}")
    else:
        await update.message.reply_text("Desculpe, não encontrei nenhuma ferramenta com esse nome. Tente novamente ou envie um áudio.")

