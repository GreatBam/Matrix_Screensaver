import bext, random
from line import Line

def main():
    width, height = bext.size()
    line = Line('green', 'black', width, height, bext, 5, 0)
    try:
        while True:
            line.printLine()
    except KeyboardInterrupt:
        pass
    
if __name__ == "__main__":
    main()