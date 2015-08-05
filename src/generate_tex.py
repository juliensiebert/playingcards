# -*- coding: utf-8 -*-
import cards_texcode as ctc # where the latex code of the cards is stored
import sys, getopt          # used to manage command line arguments
import numpy as np

def parse(filename,outdir,texcode):
    """ 
    Parse the csv file 'filename', create the tex files (from texcode + the just parsed data) and store them into directory 'outdir'
    """
    d = np.genfromtxt(filename, delimiter=',', dtype=None,  names=['Name','Symbol','Formula','Value','Power','Unit','Order'])
    for name,symbol,formula,value,power,unit,order in d:
        card_filename = outdir+'Card_'+str(order)+'_'+'_'.join(name.split(' '))+'.tex'
        card_file =  open(card_filename, 'w')
        card_file.write(texcode %(name,symbol,formula,value,power,unit,order))
        card_file.close()



def usage(pgm_name,pgm_desc,pgm_opts):
    """ just print the usage string to the standard output """
    formated_opts = ['%s\t\t%s' %(k,v) for (k,v) in pgm_opts.items()]
    help_msg = "Program: %s\n\nDescription: %s\n\nOptions:\n\t%s" %(pgm_name,pgm_desc,'\n\t'.join(formated_opts))
    print help_msg


def main(argv):
    """ This main method is used mainly to parse command line arguments (see usage method for a complete list or call this program with -h or --help command)
    Then, call the programm core methods """
    ## command line arguments and description
    pgm_name = sys.argv[0]
    pgm_desc = "Generates TeX code for playing cards from csv file"
    pgm_opts = {"help":"print help message",
                "input=":"(-i) csv file containing information cards (default '../dat/phys_const.csv')",
                "outdir=":"(-o) directory to store the cards tex files (default '../tex/')",
                }
    ## Default values
    outdir='../tex/'
    csvfilename = '../dat/phys_const.csv'
    texcode = ctc.BLACKANDWHITENUMBERS
    ## parse command line argument:
    try:
        opts, args = getopt.getopt(argv, "hi:o:", pgm_opts.keys())
    except getopt.GetoptError as err:
        # if error in the parsing, then print the help message then exit
        print 'something went wrong while parsing command line arguments (certainly an unknown option)'
        print err.msg
        print '='*25
        usage(pgm_name,pgm_desc,pgm_opts)
        sys.exit(2)

    ## setup arguments
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage(pgm_name,pgm_desc,pgm_opts)
            sys.exit()
        elif opt in ("-i", "--input"):
            csvfilename = arg
        elif opt in ("-o", "--outdir"):
            outdir = arg
        else:
            print "unknown argument %s" %(opt)
            usage(pgm_name,pgm_desc,pgm_opts)
            exit(2)
    parse(csvfilename,outdir,texcode)

if __name__ == "__main__":
    """ In case this file is used as module, this will not be used. In case this file is used as standalone application, then this is the main entry point """
    main(sys.argv[1:])
