from datetime import datetime
from random import randint

APP_VERSION = 'v0.3.0'


def get_happy_messages():
    messages = [
        'O importante não é ganhar, o que importa é competir sem perder, nem empatar.',
        'Sacode a poeira e dá a volta por cima! Só tome cuidado com a rinite.',
        'Batatinha quando nasce se esparrama pelo chão, agir é mais importante do que ter motivação.',
        'O Google Maps não pode te ajudar a encontrar o rumo da sua vida. Descubra!',
        'Que seu dia seja Ben 10 e você não desanime.',
        'Quando te chamarem de amador, lembre-se: amadores fizeram a arca de Noé e profissionais fizeram o Titanic.',
        'Corra atrás dos seus sonhos com a mesma pressa que você corre atrás do busão.',
    ]

    return messages[randint(0, len(messages) - 1)]


def get_salutation():
    now = datetime.now()
    if now.hour < 6:
        return 'Vai dormir!'
    if now.hour < 12:
        return 'Bom dia NeuralMed!!1'
    if now.hour < 18:
        return 'Boa tarde NeuralMed!!!'
    else:
        return 'Boa noite NeuralMed!!!'


def main():
    message = get_salutation()
    print(message)
    happy_message = get_happy_messages()
    print(happy_message)


if __name__ == '__main__':
    print(f'App version: {APP_VERSION}\n')
    main()
