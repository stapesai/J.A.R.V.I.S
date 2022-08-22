import sys

from data_prep.cli import interactive, cli

if __name__ == "__main__":
    print(sys.argv)
    arg_list = sys.argv[1:]
    print(arg_list)
    if arg_list:
        cli(arg_list)
    else:
        interactive()
