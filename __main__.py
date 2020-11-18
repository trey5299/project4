import sys
from cis301.project4.server import webapp

server = object()
def main(args=None):
    """
        This program that parses the command line, creates a
        Student, and prints a description of the student to
        standard out by invoking its toString method.
    """
    if args is None:
        args = sys.argv[1:]

    if len(args)<2:
        print( f">>> Project4. Missing command line arguments" )
        print(usage())
    parse_cli_argv(args)


def run_client(argv):
    pass

def run_server(argv):
    if '--client' in argv:
        #TODO: Add client commandline support which leads to instantiating a PhoneBillClient

        exit(-1)

    port = None
    server_file=None
    if "-port" in argv and len(argv)> argv.index("-port"):
        try:
            indx = argv.index("-port")
            port = int(argv[indx+1])
        except Exception as ex:
            print( 'Handling run-time error:', ex )
            usage()
            exit(-1)
    if "-file" in argv and len(argv)> argv.index("-file"):
        try:
            indx = argv.index("-file")
            server_file = int(argv[indx+1])
        except Exception as ex:
            print( 'Handling run-time error:', ex )
            usage()
            exit( -1 )

    if port and server_file:
        webapp.run(port,server_file)
    elif port:
        webapp.run(port)
    elif server_file:
        webapp.run(file=server_file)
    else:
        webapp.run()


def parse_cli_argv(argv):
    '''
      There are two paths to verify to: server or client
    :param argv: contains command-line arguments to be processed based on mode selection
    :return: None
    '''
    if "--server" in argv:
        #process commandline arguments based on server mode
        run_server(argv)
    elif "--client" in argv:
        #process commandline arguments based on client mode
        run_client(argv)



def usage():
    help ='usage: project4 [options] <args> args are (in this order):\n'+ \
          '\t--server\t\t run in server mode\n' + \
          '\t--client\t\t run in client mode\n' + \
        '\nif client mode is selected, then the following args are options are available:\t'+ \
          '\n\t-register\t\t to register a new user followed by username and password\n' + \
          '\n\t username\t\t username for authentication before executing requested operation'+ \
        '\n\t password\t\t password for authentication before executing requested operation' + \
        '\nuser will select one of the following operations:\t' + \
          '\n\t-add\t\t to add a new phone call, followed by a complete phone call record\n' + \
          '\n\t-update phonecall-id phonecall\t\t to update an existing phone call given its ID, followed by a complete phone call record\n' + \
          '\n\t-delete phonecall-id \t\t to delete an existing phone call given its ID\n' + \
          '\tcustomer\t\tPerson whose phone bill we’re modeling\n' + \
          '\tcustomer\t\tPerson whose phone bill we’re modeling\n'+\
        '\tcallerNumber\t\tPhone number of caller\n'+\
        '\tcalleeNumber\t\tPhone number of person who was called\n'+\
        '\tstartTime\t\tDate and time call began (24-hour time)\n'+\
        '\tendTime\t\t\tDate and time call ended (24-hour time)\n'+ \
          '\tDate and time should be in the format: mm/dd/yyyy hh:mm\n'\
        '\nif server mode is selected, then the following args are available\t\n' + \
          '\t-port port-no\t\t to set a port number for the server to listen\n' + \
          '\t-file filename\t\t to use an existing filename or create a new filename to be used by the server\n' + \
          'options that are avaible for terminal client app (options may appear in any order):\n'+\
        '\t-print\t\t\tPrints a description of the new phone call\n'+\
        '\t-README\t\t\tPrints a README for this project and exits\n'
    return help

if __name__ == "__main__":
    main()