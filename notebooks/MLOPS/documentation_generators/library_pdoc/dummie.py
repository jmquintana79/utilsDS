import sys

class Printer():

    ## constructor
    def __init__(self, verbose):
        """
        Constructor.
        verbose -- Activate or not displaying a couple of message.
        """
        self.verbose = verbose

    ## printer
    def display(self, msg1, msg2):
        """
        Printer.
        msg1 -- First message to be printed.
        msg2 -- Second message to be printed.
        """
        if self.verbose:
            print(msg1, msg2)
        else:
            print("deactivated")

def main(arg1:str, arg2:str, verbose:bool = True):
    """
    This is the main function for testing a documentation
    generator.
    arg1 -- First string to be plotted.
    arg2 -- Second string to be plotted.
    verbose -- Display or not by screen (default, True).
    """
    # initialize printer
    pt = Printer(verbose = verbose)
    # print
    pt.display(arg1, arg2)
    # return 
    return None

if __name__ == "__main__":
    # arguments
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    # launche
    main(arg1, arg2)
    # close
    quit("done")