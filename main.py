import bext, random
from line import Line
from interval_timer import IntervalTimer

def main():
    width, height = bext.size()
    lines = []
    for i in range(30):
        line = Line('green',
                    'black',
                    width,
                    height,
                    bext)
        lines.append(line)
    try:
        while True:
            for interval in IntervalTimer(0.1):
                for line in lines:
                    random.shuffle(lines)
                    line.printLine()
    except KeyboardInterrupt:
        pass
    
if __name__ == "__main__":
    main()