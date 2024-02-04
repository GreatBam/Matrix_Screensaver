import bext, random
from line import Line

def main():
    width, height = bext.size()
    lines = []
    for i in range(0, 10):
        line = Line('green', 'black', width, height, bext)
        lines.append(line)
    try:
        while True:
            for line in lines:
                line.printLine()
    except KeyboardInterrupt:
        pass
    
if __name__ == "__main__":
    main()