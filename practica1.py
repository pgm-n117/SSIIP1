
#!/usr/bin/python3

import sys, getopt, Estado, Maze, Algoritmo, practica1



#from libreria import funcion as fn

def main(argv):

   practica1.maze = Maze.getProblemInstance(5, 5, 100)
   Algoritmo.f()



   return(0)





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
   '''
   khjlhkjhkl
   '''




