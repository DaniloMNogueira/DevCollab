APP_VERSION = 'v0.1.0'


def get_salutation():
    return 'Boa tarde NeuralMed!!!'


def main():
    message = get_salutation()
    print(message)


if __name__ == '__main__':
    print(f'App version: {APP_VERSION}\n')
    main()
