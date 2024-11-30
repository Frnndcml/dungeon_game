import random

def geracaoGrade(tamanho):
    return [['-' for _ in range(tamanho)] for _ in range(tamanho)]

def exibicaoGrade(grade):
    for linha in grade:
        print(' '.join(linha))
    print()

def distancia(ponto1, ponto2):
    return abs(ponto1[0] - ponto2[0]) + abs(ponto1[1] - ponto2[1])

def gerarPosicaoLivre(grade, ocupados):
    while True:
        posicao = [random.randint(0, len(grade) - 1), random.randint(0, len(grade) - 1)]
        if posicao not in ocupados:
            return posicao

def moverInimigos(grade, inimigos, itens, jogador):
    movimentos = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for inimigo in inimigos:
        while True:
            direcao = random.choice(movimentos)
            novaPosicao = [inimigo[0] + direcao[0], inimigo[1] + direcao[1]]
            if (0 <= novaPosicao[0] < len(grade)) and (0 <= novaPosicao[1] < len(grade)):
                if novaPosicao not in itens and novaPosicao != jogador:
                    grade[inimigo[0]][inimigo[1]] = '-' 
                    inimigo[0], inimigo[1] = novaPosicao
                    grade[novaPosicao[0]][novaPosicao[1]] = 'E'
                    break

def jogar():
    tamanhoGrade = 10
    numItens = 2
    numInimigos = 7
    
    grade = geracaoGrade(tamanhoGrade)
    
    jogador = [0, 0]
    itens = [gerarPosicaoLivre(grade, [jogador]) for _ in range(numItens)]
    inimigos = [gerarPosicaoLivre(grade, [jogador] + itens) for _ in range(numInimigos)]
    
    for item in itens:
        grade[item[0]][item[1]] = 'I'
    for inimigo in inimigos:
        grade[inimigo[0]][inimigo[1]] = 'E'
    
    pontos = 0
    game_over = False
    
    while not game_over:
        exibicaoGrade(grade)
        print(f"Pontos: {pontos}")
        print("Movimente-se utilizando WASD")
        
        movimento = input("Digite um movimento: ").strip().upper()
        
        novaPosicao = jogador[:]
        if movimento == 'W' and jogador[0] > 0:
            novaPosicao[0] -= 1
        elif movimento == 'S' and jogador[0] < tamanhoGrade - 1:
            novaPosicao[0] += 1
        elif movimento == 'A' and jogador[1] > 0:
            novaPosicao[1] -= 1
        elif movimento == 'D' and jogador[1] < tamanhoGrade - 1:
            novaPosicao[1] += 1
        else:
            print("Movimento inválido")
            continue
        
        if grade[novaPosicao[0]][novaPosicao[1]] == 'I':
            pontos += 1
            itens.remove(novaPosicao)
            grade[novaPosicao[0]][novaPosicao[1]] = '-'
            if not itens:
                print("Todos os itens foram coletados! Você venceu!")
                game_over = True
                break
            
        elif grade[novaPosicao[0]][novaPosicao[1]] == 'E':
            print("Um inimigo te encontrou... Fim de jogo")
            game_over = True
            break
        
        grade[jogador[0]][jogador[1]] = '-'
        jogador = novaPosicao
        grade[jogador[0]][jogador[1]] = 'J'
        
        if not game_over:
            moverInimigos(grade, inimigos, itens, jogador)

if __name__ == "__main__": 
    jogar()