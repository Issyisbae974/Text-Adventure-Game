from colorama import Fore, Style, init
import os
import sys
import time
import threading
import subprocess
import platform

init(autoreset=True)  # automatically resets color after each print



def type_text(text, delay=0.05, color_func=None):
    """Print text one character at a time, optionally with color."""
    for char in text:
        if color_func:
            sys.stdout.write(color_func(char))
        else:
            sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def enter():
    return Color.bright_yellow_shortcut('[ENTER]')

def backkey():
    return Color.bright_yellow_shortcut('[BACKSPACE]')

def selected(text):
    return f"{Color.bright_cyan_shortcut('>')} {text} {Color.bright_cyan_shortcut('<')}"

def backspace():
    return '\x08', '\x7f'

def clear_screen():
    # Clears the terminal screen for cross-platform compatibility
    os.system('cls' if os.name == 'nt' else 'clear')


class Color:
    # Standard colors
    @staticmethod
    def black(text):   print(f"{Fore.BLACK}{text}")
    @staticmethod
    def red(text):     print(f"{Fore.RED}{text}")
    @staticmethod
    def green(text):   print(f"{Fore.GREEN}{text}")
    @staticmethod
    def yellow(text):  print(f"{Fore.YELLOW}{text}")
    @staticmethod
    def blue(text):    print(f"{Fore.BLUE}{text}")
    @staticmethod
    def magenta(text): print(f"{Fore.MAGENTA}{text}")
    @staticmethod
    def cyan(text):    print(f"{Fore.CYAN}{text}")
    @staticmethod
    def white(text):   print(f"{Fore.WHITE}{text}")

    # Bright colors
    @staticmethod
    def bright_black(text):   print(f"{Style.BRIGHT}{Fore.BLACK}{text}")
    @staticmethod
    def bright_red(text):     print(f"{Style.BRIGHT}{Fore.RED}{text}")
    @staticmethod
    def bright_green(text):   print(f"{Style.BRIGHT}{Fore.GREEN}{text}")
    @staticmethod
    def bright_yellow(text):  print(f"{Style.BRIGHT}{Fore.YELLOW}{text}")
    @staticmethod
    def bright_blue(text):    print(f"{Style.BRIGHT}{Fore.BLUE}{text}")
    @staticmethod
    def bright_magenta(text): print(f"{Style.BRIGHT}{Fore.MAGENTA}{text}")
    @staticmethod
    def bright_cyan(text):    print(f"{Style.BRIGHT}{Fore.CYAN}{text}")
    @staticmethod
    def bright_white(text):   print(f"{Style.BRIGHT}{Fore.WHITE}{text}")

    # -----------------------
    # Standard colors (shortcut)
    # -----------------------
    @staticmethod
    def black_shortcut(text):   return f"{Fore.BLACK}{text}{Style.RESET_ALL}"
    @staticmethod
    def red_shortcut(text):     return f"{Fore.RED}{text}{Style.RESET_ALL}"
    @staticmethod
    def green_shortcut(text):   return f"{Fore.GREEN}{text}{Style.RESET_ALL}"
    @staticmethod
    def yellow_shortcut(text):  return f"{Fore.YELLOW}{text}{Style.RESET_ALL}"
    @staticmethod
    def blue_shortcut(text):    return f"{Fore.BLUE}{text}{Style.RESET_ALL}"
    @staticmethod
    def magenta_shortcut(text): return f"{Fore.MAGENTA}{text}{Style.RESET_ALL}"
    @staticmethod
    def cyan_shortcut(text):    return f"{Fore.CYAN}{text}{Style.RESET_ALL}"
    @staticmethod
    def white_shortcut(text):   return f"{Fore.WHITE}{text}{Style.RESET_ALL}"

    # -----------------------
    # Bright colors (shortcut)
    # -----------------------
    @staticmethod
    def bright_black_shortcut(text):   return f"{Style.BRIGHT}{Fore.BLACK}{text}{Style.RESET_ALL}"
    @staticmethod
    def bright_red_shortcut(text):     return f"{Style.BRIGHT}{Fore.RED}{text}{Style.RESET_ALL}"
    @staticmethod
    def bright_green_shortcut(text):   return f"{Style.BRIGHT}{Fore.GREEN}{text}{Style.RESET_ALL}"
    @staticmethod
    def bright_yellow_shortcut(text):  return f"{Style.BRIGHT}{Fore.YELLOW}{text}{Style.RESET_ALL}"
    @staticmethod
    def bright_blue_shortcut(text):    return f"{Style.BRIGHT}{Fore.BLUE}{text}{Style.RESET_ALL}"
    @staticmethod
    def bright_magenta_shortcut(text): return f"{Style.BRIGHT}{Fore.MAGENTA}{text}{Style.RESET_ALL}"
    @staticmethod
    def bright_cyan_shortcut(text):    return f"{Style.BRIGHT}{Fore.CYAN}{text}{Style.RESET_ALL}"
    @staticmethod
    def bright_white_shortcut(text):   return f"{Style.BRIGHT}{Fore.WHITE}{text}{Style.RESET_ALL}"

