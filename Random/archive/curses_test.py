import curses
import _curses

def main(stdscr):
    s = str(type(stdscr))
    stdscr.clear()
    stdscr.addstr(0,0,s)
    stdscr.refresh()
    stdscr.getkey()

curses.wrapper(main)