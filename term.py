import platform
import os


class _Getch:
    """
    - gets a single character from standard input
    - does not echo to the screen
    - thank you: https://stackoverflow.com/questions/510357/how-to-read-a-single-character-from-the-user
    """

    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty
        import sys

    def __call__(self):
        import sys
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        ch = msvcrt.getch()
        while msvcrt.kbhit():
            msvcrt.getch()
        return ch


getch = _Getch()


class _Clear:
    def __call__(self):
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')


clear = _Clear()
