import random

def jogo(jogador1, jogador2):
    # Dicionário para mapear escolhas para emojis
    emojis = {
        "pedra": "🪨",
        "papel": "📄",
        "tesoura": "✂️"
    }
    
    print(f"Você escolheu: {jogador1} {emojis[jogador1]}")
    print(f"O computador escolheu: {jogador2} {emojis[jogador2]}")

    if jogador2 == jogador1:
        print("Empate! 🤝")
    elif (jogador2 == "pedra" and jogador1 == "tesoura") or \
         (jogador2 == "papel" and jogador1 == "pedra") or \
         (jogador2 == "tesoura" and jogador1 == "papel"):
        print("Você perdeu! 😗")
    else:
        print("Você venceu! 😒")

opcoes = ["pedra", "papel", "tesoura"]
jogador1 = input("Digite pedra, papel ou tesoura: ").lower()
jogador2 = random.choice(opcoes)
jogo(jogador1, jogador2)