def bye_command(subparser):
    parser = subparser.add_parser("bye", help="Say bye")

    parser.set_defaults(func=bye_handler)

def bye_handler(args):
    print("bye, world!")