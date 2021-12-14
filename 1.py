#!/usr/bin/env python3
import logging

logging.basicConfig(level=logging.INFO)

def fib(n):
        if n == 0:
                return 0
        elif (n == 1) or (n == 2):
                return 1
        else:
                return fib(n-1) + fib(n-2)

def main():
     logging.info(fib(10))
     

if __name__ == "__main__":
     main()

