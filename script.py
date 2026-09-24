import hashlib

def testar_senhas():
    # Lista de senhas possíveis
    pos_pw_list = ["f09e", "4dcf", "87ab", "dba8", "752e", "3961", "f159"]
    
    # Hash correto para comparação
    correct_pw_hash = open('level3.hash.bin', 'rb').read()
    
    for senha in pos_pw_list:
        # Calcula o hash da senha atual
        user_pw_hash = hashlib.md5(senha.encode()).digest()
        
        # Compara com o hash correto
        if user_pw_hash == correct_pw_hash:
            print(f"Senha correta encontrada: {senha}")
            return senha
    
    print("Nenhuma senha correta encontrada.")
    return None


if __name__ == "__main__":
    testar_senhas()