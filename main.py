import sys
from src import parser

def main():

    p = parser.Parser()
    request = p.parse_args(sys.argv[1:], 'tasks')
    acknowledgement = request.perform_query()
    print(acknowledgement)

if __name__=='__main__':
    main()