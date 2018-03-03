#!/usr/bin/python

# A simple python function for writing to DEPNotify's log file.
# In order to pass more complex strings, you must use r"TEXT". r tells python
# to pass the literal string vs an interpreted string.

# Written by Erik Gomez


def deplog(text):
    depnotify = "/private/var/tmp/depnotify.log"
    with open(depnotify, "a+") as log:
        log.write(text + "\n")


def main():
    deplog("Command: Quit: Your machine is now setup. Thank you"
           "for your patience.")


if __name__ == '__main__':
    main()
