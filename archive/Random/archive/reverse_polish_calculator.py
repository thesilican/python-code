#!/usr/bin/python3
import curses
import operator
import math
import re
_OPERATORS = {
    "+": (operator.add, 2),
    "-": (operator.sub, 2),
    "*": (operator.mul, 2),
    "/": (operator.truediv, 2),
    "%": (operator.mod, 2),
    "**": (lambda x, y: math.pow(x, y), 2),
    "**2": (lambda x: math.pow(x, 2), 1),
    "**3": (lambda x: math.pow(x, 3), 1),
    "//": (lambda x, y: math.pow(x, 1/y), 2),
    "//2": (lambda x: math.sqrt(x), 1),
    "//3": (lambda x: math.copysign(math.pow(x, 1/3), x), 1),
    # Trig
    "sin": (lambda x: math.sin(x), 1),
    "cos": (lambda x: math.cos(x), 1),
    "tan": (lambda x: math.tan(x), 1),
    "csc": (lambda x: 1/math.sin(x), 1),
    "sec": (lambda x: 1/math.cos(x), 1),
    "cot": (lambda x: 1/math.tan(x), 1),
    "asin": (lambda x: math.asin(x), 1),
    "acos": (lambda x: math.acos(x), 1),
    "atan": (lambda x: math.atan(x), 1),
    "acsc": (lambda x: math.asin(1/x), 1),
    "asec": (lambda x: math.acos(1/x), 1),
    "acot": (lambda x: math.atan(1/x), 1),
    # Logarithms
    "log": (lambda x, y: math.log(x, y), 2),
    "log10": (lambda x: math.log10(x), 1),
    "ln": (lambda x: math.log(x, math.e), 1),
}

_ACTIONS = {
    # Paste from buffer
    ".",
    # Store to buffer
    "..",
    # Clear buffer
    "...",
    # Clear all
    "....",
    "++",
    # Delete from stack
    "d",
    "--",
    "---",
    # Undo
    "u",
    # Redo
    "r",
    # Go to specific history point
    "h"
}


class ReversePolishCalculator:
    def __init__(self):
        self._curOp = ""
        self.history = [[
            # Stack
            [],
            # Buffer
            [],
            # Prev operator
            "",
        ]]
        self.historyPtr = 0
        self.historyMaxSize = 100

    @property
    def stack(self):
        return self.history[self.historyPtr][0]

    @property
    def buffer(self):
        return self.history[self.historyPtr][1]

    @property
    def prevAction(self):
        return self.history[self.historyPtr][2]

    @prevAction.setter
    def prevAction(self, val):
        self.history[self.historyPointer][2] = val

    def newHistory(self):
        # Slice off old history
        if self.historyPtr < len(self.history) - 1:
            self.history = self.history[:self.historyPtr + 1]
        self.history.append(
            (self.stack[:], self.buffer[:], self._curOp))
        if len(self.history) > self.historyMaxSize:
            self.history.pop(0)
        else:
            self.historyPtr += 1

    def changeHistory(self, index):
        if 0 <= index < len(self.history):
            self.historyPtr = index
        else:
            return "Invalid history index: " + str(index)

    def parseFloat(self, s):
        res = re.match("^[+-]?([0-9]*[.])?[0-9]+$", s)
        if res != None:
            return float(s)
        elif s == "e":
            return math.e
        elif s == "pi":
            return math.pi
        else:
            return None

    def parseAction(self, s):
        foundLen = 0
        found = None
        for action in _ACTIONS:
            l = len(action)
            if l <= foundLen:
                continue
            if s.startswith(action):
                if len(s) == l:
                    found = (action,)
                    foundLen = l
                elif re.match("^[0-9]+$", s[l:]) != None:
                    found = (action, int(s[l:]))
                    foundLen = l
        return found

    def execute(self, s):
        self._curOp = s
        if self.parseFloat(s) != None:
            return self.pushNum(self.parseFloat(s))
        if s in _OPERATORS:
            return self.executeOperator(s)
        action = self.parseAction(s)
        if action != None:
            return self.executeAction(action)
        return "Invalid Operator: '" + s + "'"

    def pushNum(self, num):
        self.newHistory()
        self.stack.append(num)

    def executeOperator(self, oper):
        operFunc = _OPERATORS[oper][0]
        operLen = _OPERATORS[oper][1]
        if len(self.stack) < operLen:
            return "Not enough arguments"
        args = self.stack[len(self.stack) - operLen:]
        res = 0
        try:
            res = operFunc(*args)
        except (ValueError, ZeroDivisionError):
            return "Math Error"
        except (OverflowError):
            return "Overflow Error"
        self.newHistory()
        del self.stack[len(self.stack) - operLen:]
        self.stack.append(res)

    def executeAction(self, action):
        if action[0] == ".":
            # return self.pasteFromBuffer(0 if len(action) == 1 else action[1])
            return self.pasteFromBuffer(0)
        elif action[0] == "..":
            # return self.copyToBuffer(1 if len(action) == 1 else action[1])
            return self.copyToBuffer(1)
        elif action[0] == "...":
            return self.clearBuffer()
        elif action[0] == "....":
            return self.clearAll()
        elif action[0] == "++":
            return self.clearAll()
        elif action[0] == "--":
            return self.delete(1)
        elif action[0] == "---":
            return self.delete(0)
        elif action[0] == "d":
            return self.delete(0 if len(action) == 1 else action[1])
        elif action[0] == "u":
            if 0 <= self.historyPtr - 1 < len(self.history):
                return self.changeHistory(self.historyPtr - 1)
            else:
                return "Reached undo limit"
        elif action[0] == "r":
            if 0 <= self.historyPtr + 1 < len(self.history):
                return self.changeHistory(self.historyPtr + 1)
            else:
                return "Reached redo limit"
        elif action[0] == "h":
            if len(action) == 1:
                return "Please specify history"
            return self.changeHistory(action[1])

    def pasteFromBuffer(self, num):
        self.newHistory()
        if num == 0:
            self.stack.extend(self.buffer)
        else:
            self.stack.extend(self.buffer[:num])

    def copyToBuffer(self, num):
        self.newHistory()
        self.buffer.clear()
        if num == 0:
            self.buffer.extend(self.stack)
        elif num > len(self.stack):
            return "Stack does not have " + str(num) + " elements"
        else:
            self.buffer.extend(self.stack[len(self.stack)-num:])

    def clearBuffer(self):
        self.newHistory()
        self.buffer.clear()

    def clearAll(self):
        self._curOp = ""
        self.history = [[
            # Stack
            [],
            # Buffer
            [],
            # Prev operator
            "",
        ]]
        self.historyPtr = 0

    def delete(self, num):
        self.newHistory()
        if num == 0:
            self.stack.clear()
        elif num > len(self.stack):
            return "Stack has less than " + str(num) + " elements"
        else:
            del self.stack[len(self.stack) - num:]


def main(stdscr):
    curses.start_color()
    curses.use_default_colors()

    calc = ReversePolishCalculator()
    key = ""
    inputBuffer = list()
    error = ""

    def formatNum(num):
        return "{:d}".format(int(num)) if num.is_integer() else "{:n}".format(num)

    def printScreen():
        stdscr.clear()
        stack = " ".join(map(formatNum, calc.stack))
        buffer = " ".join(map(formatNum, calc.buffer))
        errorMsg = "" if error == None else error
        prevOper = calc.prevAction
        userInput = "".join(inputBuffer)
        stdscr.addstr(0, 0, "Hsilop Calculator")
        stdscr.addstr(1, 0, stack)
        stdscr.addstr(2, 0, "({}) {}".format(buffer, errorMsg))
        stdscr.addstr(3, 0, "[{}] {}".format(prevOper, userInput))
        stdscr.refresh()

    while True:
        printScreen()
        key = stdscr.getkey()
        if key == "\n":
            if len(inputBuffer) == 0:
                error = calc.execute(calc.prevAction)
            else:
                error = calc.execute("".join(inputBuffer))
            inputBuffer.clear()
        elif key == "KEY_BACKSPACE":
            if len(inputBuffer) > 0:
                inputBuffer.pop()
            else:
                error = calc.execute("d1")
        elif key == "KEY_UP":
            error = calc.execute("u")
        elif key == "KEY_DOWN":
            error = calc.execute("r")
        elif re.match("[a-z0-9+\-*/.]", key):
            inputBuffer.append(key)
        else:
            error = key


try:
    curses.wrapper(main)
except KeyboardInterrupt:
    pass
finally:
    curses.endwin()
