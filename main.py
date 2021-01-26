import sys
from src import parser

def main():

    p = parser.Parser()
    request = p.parse_args(sys.argv[1:])
    acknowledgement = request.perform_query()

if __name__=='__main__':
    main()