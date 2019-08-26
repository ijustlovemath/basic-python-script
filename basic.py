import sys
import argparse

options = lambda:0

def main(args):
    global options

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    options = parser.parse_args(args)

if __name__=='__main__':
    main(sys.argv[1:])
