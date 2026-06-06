import curses
import random

CHARS = "ｦｧｨｩｪｫｬｭｮｯｰｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜﾝ0123456789"

def matrix(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    stdscr.nodelay(True)

    h, w = stdscr.getmaxyx()
    drops = [random.randint(-h, 0) for _ in range(w)]

    while True:
        stdscr.erase()

        for x in range(w - 1):
            drops[x] += 1

            if drops[x] > h:
                drops[x] = random.randint(-h, 0)

            y = drops[x]

            for i in range(20):
                ty = y - i
                if 0 <= ty < h:
                    char = random.choice(CHARS)
                    if i == 0:
                        attr = curses.color_pair(2) | curses.A_BOLD
                    elif i < 5:
                        attr = curses.color_pair(1) | curses.A_BOLD
                    else:
                        attr = curses.color_pair(1)
                    try:
                        stdscr.addstr(ty, x, char, attr)
                    except curses.error:
                        pass

        stdscr.refresh()
        curses.napms(50)

curses.wrapper(matrix)