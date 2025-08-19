from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
from pathlib import Path
import sys
import os


arquivo_privado = Path("chave_privada.pem")
arquivo_publico = Path("chave_publica.pem")

def gerar_e_salvar_chaves():
    print("[*] Gerando um novo par de chaves")
    
    key = RSA.generate(2048)
    
    private_key_pem = key.export_key(format='PEM')
    arquivo_privado.write_bytes(private_key_pem)

    public_key_pem = key.publickey().export_key(format='PEM')
    arquivo_publico.write_bytes(public_key_pem)

    print(f"Chave privada salva")
    print(f"Chave pública salva")
    return key, key.publickey()

def carregar_chaves():
    if not arquivo_privado.exists() or not arquivo_publico.exists():
        private_key_obj, public_key_obj = gerar_e_salvar_chaves()
    else:
        try:
            private_key_obj = RSA.import_key(arquivo_privado.read_bytes())
            public_key_obj = RSA.import_key(arquivo_publico.read_bytes())
            print("Chaves locais carregadas com sucesso.")
        except Exception as e:
            print(f"Falha ao carregar chaves existentes: {e}")

    return private_key_obj, public_key_obj

def encriptar_mensagem(mensagem: str, public_key) -> str:
    texto_original_bytes = mensagem.encode('utf-8')
    

    cipher_rsa = PKCS1_OAEP.new(public_key)
    cipher_bytes = cipher_rsa.encrypt(texto_original_bytes)
    
    texto_encriptado_b64 = base64.b64encode(cipher_bytes).decode('utf-8')

    print(f"Texto Original: '{mensagem}'")
    print(f"Texto Encriptado (bytes): {cipher_bytes}")
    print("---------------------------------")
    
    return texto_encriptado_b64

def decriptar_mensagem(texto_encriptado_b64: str, private_key):
    try:
        cipher_bytes = base64.b64decode(texto_encriptado_b64)
        
        cipher_rsa = PKCS1_OAEP.new(private_key)
        texto_decriptado_bytes = cipher_rsa.decrypt(cipher_bytes)
        
        texto_decriptado = texto_decriptado_bytes.decode('utf-8')
        return texto_decriptado
    except (ValueError, TypeError) as e:
        return f"Falha na decriptação. Verifique se a mensagem foi encriptada com a chave pública correta e se não está corrompida."

def menu_principal():
    private_key, public_key = carregar_chaves()
    
    while True:
        print("\n----- MENU DE CRIPTOGRAFIA -----")
        print("1. Gerar Novas Chaves (sobrescreve as atuais)")
        print("2. Encriptar Mensagem")
        print("3. Decriptar Mensagem")
        print("4. Mostrar Minha Chave Pública")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            confirm = input("ATENÇÃO: Isso irá sobrescrever suas chaves atuais. Deseja continuar? (s/N): ").lower()
            if confirm == 's':
                private_key, public_key = gerar_e_salvar_chaves()
            else:
                print("Operação cancelada.")
        
        elif opcao == '2':
            print("--- Encriptar Mensagem ---")
            caminho_pub = input("Digite o caminho da chave pública do destinatário (.pem) ou pressione Enter para usar a sua: ").strip()
            
            try:
                if caminho_pub and Path(caminho_pub).exists():
                    key_to_use = RSA.import_key(Path(caminho_pub).read_bytes())
                    print(f"Usando a chave pública de '{caminho_pub}'.")
                else:
                    key_to_use = public_key
                    print("Usando a sua própria chave pública para um autoteste.")
                
                mensagem = input("Digite a mensagem a ser encriptada: ").strip()
                if not mensagem:
                    print("Mensagem vazia. Operação cancelada.")
                    continue

                b64_encrypted = encriptar_mensagem(mensagem, key_to_use)
                
                print("\n3. Texto Encriptado (em Base64 para transporte):")
                print("--- COPIE O TEXTO ABAIXO E ENVIE AO DESTINATÁRIO ---")
                print(b64_encrypted)
                print("----------------------------------------------------")

            except Exception as e:
                print(f"Não foi possível encriptar")
        
        elif opcao == '3':
            print("--- Decriptar Mensagem ---")
            print("Cole a mensagem encriptada em Base64. Pressione Enter em uma linha vazia para finalizar.")
            
            linhas = []
            while True:
                ln = sys.stdin.readline().strip()
                if not ln:
                    break
                linhas.append(ln)
            
            b64_encrypted = "".join(linhas)
            
            if b64_encrypted:
                texto_decriptado = decriptar_mensagem(b64_encrypted, private_key)
                print("\n--- Resultado ---")
                print(f"4. Texto Decriptado: '{texto_decriptado}'")
                print("-----------------")
            else:
                print("Nenhuma mensagem inserida. Operação cancelada.")

        elif opcao == '4':
            print("--- Minha Chave Pública (Compartilhe com outros) ---")
            print(arquivo_publico.read_text())
            print("----------------------------------------------------")
        
        elif opcao == '5':
            print("Saindo do programa. Até mais!")
            break
            
        else:
            print("Opção inválida. Por favor, tente novamente.")
        
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    menu_principal()