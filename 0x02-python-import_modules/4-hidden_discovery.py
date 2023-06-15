#!/usr/bin/python3

if __name__ == "__main__":
   """"prints all the names defined by the compiler"""

   import hidden_4

   for name in dir(hidden_4):
      if name[:2] != "__":
         print(name)
