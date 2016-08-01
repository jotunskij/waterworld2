__author__ = 'tinglev'

import curses
from time import sleep

MENU_TEXT = 3
MENU_BORDER = 2


def draw_menu_border(scr, nr_of_commands):
    draw_text(scr, 0, 0, "                                        ", curses.color_pair(MENU_BORDER))
    for i in range(0, nr_of_commands + 2):
        draw_text(scr, 0, 1 + i, " ", curses.color_pair(MENU_BORDER))
        draw_text(scr, 39, 1 + i, " ", curses.color_pair(MENU_BORDER))
    draw_text(scr, 0, i + 2, "                                        ", curses.color_pair(MENU_BORDER))


def main():
    curses.wrapper(run_program)


def run_program(stdscr):
    curses.curs_set(0)

    curses.init_pair(MENU_BORDER, curses.COLOR_BLACK, curses.COLOR_RED)
    curses.init_pair(MENU_TEXT, curses.COLOR_BLACK, curses.COLOR_CYAN)

    draw_menu_border(stdscr, 4)

    draw_text(stdscr, 1, 1, " ".ljust(38), curses.color_pair(MENU_TEXT))
    draw_text(stdscr, 1, 2, " 1) Manage schedules".ljust(38), curses.color_pair(MENU_TEXT))
    draw_text(stdscr, 1, 3, " 2) Run test program".ljust(38), curses.color_pair(MENU_TEXT))
    draw_text(stdscr, 1, 4, " 3) Pause all schedules".ljust(38), curses.color_pair(MENU_TEXT))
    draw_text(stdscr, 1, 5, " 4) See history".ljust(38), curses.color_pair(MENU_TEXT))
    draw_text(stdscr, 1, 6, " ".ljust(38), curses.color_pair(MENU_TEXT))

    c = stdscr.getch()


def draw_text(scr, x, y, text, attrs):
    scr.addstr(y, x, text, attrs)
    sleep(0.01)
    scr.refresh()


if __name__ == '__main__':
    main()
