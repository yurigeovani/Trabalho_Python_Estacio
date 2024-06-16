import random

def escolher_palavra():
    palavras = [
        "desenvolvimento", "tecnologia", "logica", "programacao", "tendencias",
        "algoritmo", "software", "hardware", "internet", "computador",
        "redes", "dados", "seguranca", "criptografia", "inteligencia",
        "artificial", "automatizacao", "sistema", "aplicacao", "engenharia"
    ]
    return random.choice(palavras)

def exibir_forca(tentativas):
    estagios = [
        """
         ______
        |      |
        |
        |
        |
        |
        """,
        """
         ______
        |      |
        |    (ಠ_ಠ)
        |
        |
        |
        """,
        """
         ______
        |      |
        |    (ಠ_ಠ)
        |      |
        |
        |
        """,
        """
         ______
        |      |
        |    (ಠ_ಠ)
        |      |\\
        |
        |
        """,
        """
         ______
        |      |
        | ¯\\_(ಠ_ಠ)_/¯
        |      |
        |
        |
        """,
        """
         ______
        |      |
        | ¯\\_(ಠ_ಠ)_/¯
        |      |
        |       \\
        |
        """,
        """
         ______
        |      |
        |    (ಠ_ಠ)
        |     /|\\
        |     / \\
        |
        """
    ]
    print(estagios[tentativas])

def jogar():
    palavra = escolher_palavra()
    palavra_oculta = ["_"] * len(palavra)
    tentativas = 0
    letras_tentadas = []

    print("Jogo da Forca!")
    exibir_forca(tentativas)
    print("Palavra: " + " ".join(palavra_oculta))

    while tentativas < 6 and "_" in palavra_oculta:
        tentativa = input("Digite uma letra: ").lower()
        if tentativa in letras_tentadas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        letras_tentadas.append(tentativa)

        if tentativa in palavra:
            for i, letra in enumerate(palavra):
                if letra == tentativa:
                    palavra_oculta[i] = tentativa
        else:
            tentativas += 1

        exibir_forca(tentativas)
        print("Palavra: " + " ".join(palavra_oculta))
        print(f"Letras tentadas: {', '.join(letras_tentadas)}")

        if "_" not in palavra_oculta:
            print("Parabéns, você ganhou!")
            break
        elif tentativas == 6:
            print(f"Você perdeu! A palavra era '{palavra}'.")

    print("Obrigado por jogar!")

jogar()
