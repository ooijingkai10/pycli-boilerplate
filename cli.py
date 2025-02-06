import argparse
from subcommands.hello import hello_command
from subcommands.bye import bye_command

def main():
    parser = argparse.ArgumentParser(prog="cli-app", description="An extensible CLI application")
    subparsers = parser.add_subparsers(required=True)
    
    # Register commands
    hello_command(subparsers)
    bye_command(subparsers)
    
    args = parser.parse_args()
    args.func(args)
    



if __name__ == "__main__":
    main()