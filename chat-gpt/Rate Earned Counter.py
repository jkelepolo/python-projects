# 4/25/2023
# Jothan Kelepolo
# This script was a collaboration between me and chat-gpt :D
# https://chat.openai.com/

import curses
import time


rate_per_hour = float(input("Enter the rate per hour: "))

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
curses.curs_set(0)  # hide the cursor

rate_per_ms = rate_per_hour / 3600000  # rate per millisecond

start_time = time.time()  # initialize start_time

try:
    while True:
        elapsed_time = time.time() - start_time  # calculate the elapsed time
        hours, remainder = divmod(elapsed_time, 3600)
        minutes, remainder = divmod(remainder, 60)
        seconds, milliseconds = divmod(remainder, 1)
        stdscr.clear()
        stdscr.addstr(0, 0, f"Rate per hour: ${rate_per_hour:.2f}")
        stdscr.addstr(1, 0, f"Time elapsed: {int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}:{int(milliseconds * 1000):03d}")  # display time elapsed in hours, minutes, seconds, and milliseconds on first line
        total_earned = elapsed_time / 3600 * rate_per_hour  # calculate the total earned based on the elapsed time and rate per hour
        stdscr.addstr(2, 0, f"Total earned: ${total_earned:.2f}")  # display total earned with 2 decimal places on second line
        stdscr.refresh()
        time.sleep(0.1)  # wait for 100 milliseconds
except KeyboardInterrupt:
    pass

curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.curs_set(1)  # show the cursor before exiting
curses.endwin()
