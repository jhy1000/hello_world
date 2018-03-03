def main():
    import argparse

    parser = argparse.ArgumentParser(
        description='Say hello to the world or to a specific person.'
    )
    parser.add_argument('who', nargs='?', default='world', help='who to tell hello')
    args = parser.parse_args()

    print(hello(args.who))

    return 0


def hello(who='world'):
    return 'Hello, ' + who + '!'
