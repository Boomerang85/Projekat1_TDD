import unittest

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

class Test_Main(unittest.TestCase):
   def test_readFile(self):
      file = open("file.txt", "w")
      file.write("\ntest")
      file.close()

      file = open("file.txt", "r")
      quickCheck = False
      lines = file.readlines()
      for line in lines:
        if line == "test":
            quickCheck = True
        
      self.assertTrue(quickCheck)
      file.close()
      
      file = open("file.txt", "w")
      for line in lines:
        if line != "test":
            file.write(line)      
      file.close()




if __name__ == '__main__':
   unittest.main()   