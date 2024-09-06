import time

morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '/':'/'}

def codificar (texto):
    '''Função que codifica um texto pra morse
    str, dict -> str'''
    pontuac = [',', '.', ':', ':', '!', '?', '-', '@', '#', '$', '%', '¨', '&', '*', ')', '(', '{', '}', '[', ']', '_', '"','|', '<', '>', '`','^', '~', '´']
    especial = ['Á', 'Ã', 'Â', 'À', 'É', 'Ê', 'Í', 'Ó', 'Ô', 'Õ', 'Ú', 'Ç']
    resposta =''
    for i in pontuac: 
        texto = str.replace(texto, i, '')
        texto = str.replace(texto, ' ', '//')
    for j in range(len(especial)):
        if 0 <= j <=3:
            texto = str.replace(texto, especial[j], 'A')
        elif 4 <= j <=5:
            texto = str.replace(texto, especial[j], 'E')
        elif j == 6:
            texto = str.replace(texto, especial[j], 'I')
        elif 7<= j <= 9:
            texto = str.replace(texto, especial[j], 'O')
        elif j == 10:
            texto = str.replace(texto, especial[j], 'U')
        else:
            texto = str.replace(texto, especial[j], 'C')
    for caracter in texto:
        resposta += ' ' + morse[caracter]
    return resposta

def decodificar (decod):
    '''Função que codifica um texto pra morse
    str, dict -> str'''
    palavras = str.split(decod, ' ')
    resposta = ''
    for letra in palavras:
        for chave, valor in dict.items(morse):
            if letra == valor:
                resposta += chave
        resposta += ' '
    resposta = str.replace(resposta, ' ', '')
    resposta = str.replace(resposta, '//', ' ')
    return resposta

def main():
    while True:
        print('Escolha uma opção:\n1 -> Codificar\n2 -> Decodificar\n3 -> Sair')
        func = int(input('Escolha uma funcionalidade: '))
        if func == 1:
            print('Pronto para codificar!')
            texto = input('Digite um texto: ').upper()
            print(f'Mensagem codificada: {codificar(texto)}\n')
        elif func == 2:
            print('Pronto para decodificar!')
            while True:
                decod = input('Digite um código: ').upper()
                count = 0
                for i in decod:
                    if i not in '.- /':
                        print('Mensagem inválida!')
                        count = 1
                if count == 0:
                    break
            print(f'Mensagem decodificada: {decodificar(decod)}\n')
        elif func == 3:
            print('Encerrando programa!')
            time.sleep(2)
            break
        else:
            print('Função inválida')
main()