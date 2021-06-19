"""
Importação das bibliotecas.
"""
import random

print('\n\nOlá! Esse é o jogo do Letroca.\n\nINSTRUÇÕES:\n'
      '- O jogo possui 5 níveis. Quanto maior o nível, maiores'
      ' serão as palavras.\n'
      '- As palavras estarão embaralhadas, e seu papel será ordená-las.\n'
      '- Se você acertar a palavra correta, avançará para o próximo nível,'
      ' caso contrário, deverá tentar até acertar.\n'
      'Divirta-se! :)\n')


def sortear(lista):
    """
    Cria uma lista de caracteres a partir de uma palavra selecionada da lista de termos.

    Entrada: lista (lista/string).
    Saída: sorteado (lista/string-char).
    """
    sorteado = random.choice(lista)
    return sorteado


def embaralhar(palavra):
    """
    Embaralha a lista de caracteres da palavra sorteada e reúne-os novamente.

    Entrada: palavra (lista/string-char).
    Saída: embaralhado (string).
    """
    lista_caracteres = list(palavra)
    embaralhado = ''.join(random.sample(lista_caracteres, len(lista_caracteres)))
    return embaralhado


def verificar(palavra, entrada):
    """
    Confere se as tentativas do usuário estão corretas conforme a palavra sorteada.
    Se não estiver, retorna à função principal e continua a iteração.

    Entrada: palavra, entrada (string, input/string).
    Saída: bool.
    """
    return palavra == entrada


def main():
    """
    Função principal.
    Primeiro foram definidos os conjuntos de palavras, por nível.
    O setup do jogo é realizado dentro do loop for de modo que,
    na iteração, uma palavra nova seja sorteada a cada nível.
    O input do usuário é transformado em minúscula com a função lower,
    assim evita erros de verificação por conta da diferença entre
    maiúsculas e minúsculas.
    Após o usuário passar por todos os níveis, o jogo sai do loop
    for e exibe uma mensagem final.
    """
    conjuntos = {1: ['amor', 'fato', 'viés', 'mito', 'caos',
                     'agir', 'ócio', 'vale', 'alva', 'ágil'],
                 2: ['sagaz', 'atroz', 'assaz', 'ânimo',
                     'saber', 'ápice', 'temor', 'fugaz', 'mundo'],
                 3: ['etéreo', 'eximir', 'sisudo', 'objeto', 'acesso',
                     'sanção', 'receio', 'mazela', 'cômico', 'vulgar'],
                 4: ['quimera', 'imersão', 'isenção', 'parcial', 'modesto',
                     'padecer', 'emotivo', 'colapso', 'inércia', 'orgulho'],
                 5: ['metódico', 'consiste', 'desfecho', 'critério', 'suscitar',
                     'sucumbir', 'portanto', 'complexo', 'emulação', 'maestria']}

    for nivel in range(1, len(conjuntos) + 1):
        conjunto = conjuntos[nivel]
        palavra_sorteada = sortear(conjunto)
        palavra_embaralhada = embaralhar(palavra_sorteada)

        print(f'Nível: {nivel}\nA palavra é: {palavra_embaralhada}.\n')

        usuario = input('Faça a sua tentativa: ').lower()
        while not verificar(palavra_sorteada, usuario):
            usuario = input('Faça a sua tentativa: ').lower()

        print(f'Parabéns, acertou! A palavra correta é "{palavra_sorteada}".\n')

    print('Uhu, você passou por todos os níveis!')


if __name__ == '__main__':
    main()
