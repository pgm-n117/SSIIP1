
#!/usr/bin/python3

import Maze, sys, getopt
from Maze import getProblemInstance
#from libreria import funcion as fn

def main(argv):
    print argv[0]
    print argv[1]
    print argv[2]
    maze=getProblemInstance(int(argv[0]),int(argv[1]),int(argv[2]))
    print maze
    input("Press Enter to continue...")
    sys.exit()


    inputfile = ''
    outputfile = ''
    try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
      print ('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
         print ('test.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
    print ('Input file is "', inputfile)
    print ('Output file is "', outputfile)

if __name__ == "__main__":
   main(sys.argv[1:])
