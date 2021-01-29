import autenticador
import random

def gerar_tt():
    api = autenticador.autenticar()

    arquivo_letra = open("thugletra", "r+")
    letra_inteira = arquivo_letra.readlines()
    numero_do_verso = random.randrange(0, 113)
    verso = letra_inteira[numero_do_verso]

    jeito_de_tuitar = random.getrandbits(1)

    if jeito_de_tuitar == 1:
        verso += letra_inteira[numero_do_verso+1]

    api.update_status(verso)

if __name__ == '__main__':
    gerar_tt()