import argparse
import subprocess

from input import KeyboardInput


def get_clipboard_data():
    p = subprocess.Popen(['xclip', '-selection', 'clipboard', '-o'], stdout=subprocess.PIPE)
    retcode = p.wait()
    data = p.stdout.read()
    return str(data)[2:-1]


parser = argparse.ArgumentParser()
parser.add_argument('-d', '--delay', metavar='N', type=int, help='Time delay to paste')
parser.add_argument('-u', '--uppercase', action='store_true', help='Convert text to Uppercase')
args = parser.parse_args()

delay = args.delay or float(2)

text = get_clipboard_data()
if args.uppercase:
    text = text.upper()

keyboard = KeyboardInput()
keyboard.type_string(text, delay)
