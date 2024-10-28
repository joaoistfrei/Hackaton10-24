from func import *
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters


# Configurações de API e Caminho
TELEGRAM_TOKEN = "Token"
OPENAI_API_KEY = "API_key"
AUDIO_SAVE_PATH = './files'  # Caminho para salvar áudios temporários

if __name__ == "__main__":
    # Inicializar e configurar o bot
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.VOICE | filters.AUDIO, handle_audio))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search_tools))

    # Iniciar o bot
    logger.info("Bot está em execução...")
    app.run_polling()