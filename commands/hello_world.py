import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Say Hello')
    parser.add_argument('--addressee', '-a',  type=str,
                        default="World",
                        help='Who do we say hello to?')
    args = parser.parse_args()

    print("Hello", args.addressee)
