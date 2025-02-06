def hello_command(subparser):
    parser = subparser.add_parser("hello", help="Say hello")

    parser.set_defaults(func=hello_handler)

def hello_handler(args):
    print("Hello, world!")