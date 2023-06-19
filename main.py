import mido


def main():
    with mido.open_input() as inport:
        for msg in inport:
            print(msg)


if __name__ == '__main__':
    main()
