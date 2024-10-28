import whisper
import json
import difflib
from openai import OpenAI
import pandas as pd

# Função para transcrever audio com Whisper
def transcreve_audio(): 
    # Carrega o modelo Whisper
    model = whisper.load_model("medium")

    # Caminho do arquivo de áudio em português
    audio_file = "./files/audioEx.wav"

    # Transcreve o áudio
    transcription = model.transcribe(audio_file, language="pt")
    transcription_text = transcription["text"]

    # Salva a transcrição em um arquivo JSON
    transcription_data = {"transcription": transcription_text}
    with open("./files/audioTranscrito.json", "w", encoding="utf-8") as json_file:
        json.dump(transcription_data, json_file, ensure_ascii=False, indent=4)

    return transcription_text


# Função para exibir o resumo das atividades
def resumo_atividades(transcription_text):
    #transcription_text = "Bom dia, Osvaldo, tudo certo? Passando pra alinhar as coisas que ficaram pendentes pra gente fazer no domingo. Eu quero alguns serviços que acabaram que a gente não conseguiu tocar durante semana, mas deixa eu explicar aqui pra vocês algumas coisas que a gente tem que resolver logo, tá bom? Então, conhecendo pela linha 3, eu preciso que faça a lubrificação dos rolamentos ali. Essa máquina ali já está dando sinais de esgar, já tem um certo tempo. O pessoal reportou já barulho estranho já nesse equipamento, então tem que botar o lubrificante correto, ele já está no estoque, aquele código lá o azul 6624, então já toma cuidado com isso, já faz essa lubrificação com essa máquina aí e não pode esquecer de conferir a ficha técnica dele pra colocar a quantidade certa, da outra vez deu problema. Então depois disso eu preciso também que vocês dêem uma verificada no nível de óleo lá da desencapadora, lá da linha 12, é um equipamento que do nada dá uns picos de temperatura lá, o pessoal já reportou, já mandou pra gerença, foi uma merda isso, então revisar mesmo as medições, ver se está tudo certo lá com o nível de óleo dela, porque se sair do óleo recomendado, ela vai começar a esquentar e corre o risco de parar e vai dar BO. E também queria, precisa dar uma olhada, lá no compressor 5, aquele lá bem da central, né, o filtro de ar já passou do ponto, ele estava pra ser trocado na última parada, mas ele acabou ficando pra agora, então tá bem crítico, então tem que fazer substituição agora, agora no domingo já, não dá pra esperar, o filtro de novo já peixei, mandei o menino trazer lá do homoxarifado, tá debaixo da bancada, só vocês pegarem e trocar também, tá? E aproveita que você tá no compressor, aproveita e dá um polinho lá naquela bomba da bomba de circulação, aquela lá do canto direito, ela também tava, o pessoal falou que ela tá fazendo barulho, aproveita e dá uma olhadinha lá pra mim, tá? É basicamente isso, qualquer coisa aí você não me avisa, tá? Porque eu tô de folga, seguramente resolve. Valeu!"
    
    # Envia o resumo para o modelo OpenAI
    client = OpenAI(api_key="API-key")
    entrada = (
        "Ola chatGPT, me retorne o texto a seguir separado em tópicos e liste as atividades com nome do serviço, problemas "
        "reportados, recomendações, e as ferramentas a serem utilizadas para cada serviço, com os respectivos códigos SAP "
        "das ferramentas abaixo. "
        "Aqui está a lista de ferramentas e seus códigos SAP: \n" + json.dumps(tools) + "\n\n"
        "Segue o texto: \n" + transcription_text
    )
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": entrada}],
    )
    print("Resumo das atividades:\n")
    print(response.choices[0].message.content)

# Função para buscar ferramentas com tratamento de erros ortográficos
def buscar_ferramentas():
    while True:
        ferramenta = input("Digite o nome da ferramenta que deseja buscar (ou 'sair' para encerrar): ")
        if ferramenta.lower() == 'sair':
            break

        # Busca o nome mais próximo usando correspondência aproximada
        similar = difflib.get_close_matches(ferramenta, tools.keys(), n=1, cutoff=0.5)
        
        if similar:
            nome = similar[0]
            codigo_sap = tools[nome]
            print(f"Ferramenta encontrada: {nome}, Código SAP: {codigo_sap}")
        else:
            print("Ferramenta não encontrada. Tente novamente com outro nome.")

# Execução do programa
if __name__ == "__main__":
    # Carrega o arquivo CSV com os dados de ferramentas
    csv_path = './files/codigosSAP.csv'
    sap_data = pd.read_csv(csv_path)

    # Ajusta o dicionário de ferramentas com as colunas corretas
    tools = {row['Descrição do Material/Equipamento']: row['Código SAP'] for _, row in sap_data.iterrows()}
    
    text = transcreve_audio()
    
    resumo_atividades(text)
    resposta = input("\nDeseja buscar por ferramentas? (S/N): ").strip().upper()
    if resposta == 'S':
        buscar_ferramentas()
    else:
        print("Programa finalizado.")
