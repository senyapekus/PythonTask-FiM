import os.path
import re

has_breakpoint = False


class Compiler:
    def __init__(self, fim_file):
        self._list_elem_count = 0
        self._count_line = 0
        self._compiled_lines = []
        self._count_func = -1
        self._compile_dirs = {"nesting": 0, "in_func": False, "in_class": False}
        self.compile_flags = {"has_main": False, "has_end": False}
        if os.path.exists(fim_file):
            self._fim_file = fim_file
            with open(fim_file, "r", encoding='utf8') as file:
                self._text_lines = file.readlines()
            self.compile()
        else:
            raise Exception("Invalid file!")

    def compile(self):
        global has_breakpoint

        file_name = self.get_compiled_file_name()
        if "test_" in file_name:
            to_open = "{}".format(os.path.abspath(file_name)).replace("test", "py_program", 1)
        else:
            to_open = "py_program/{}".format(self.get_compiled_file_name())

        with open(to_open, "w") as compiled_file:
            for line in self._text_lines:
                if "    b" in line or "    b\n" in line:
                    has_breakpoint = True
                    line = line.replace('    b', '')
                    self._compiled_lines.append("%sbreakpoint()" % self.get_count_tabs())

                self._count_line += 1
                line_compiled = self.compile_line(line, self._count_line)

                if line_compiled != "" and not self._compile_dirs["in_func"]:
                    self._compiled_lines.append(line_compiled)
                if self._compile_dirs["in_func"]:
                    self._compiled_lines.insert(self._count_func, line_compiled)

            if not self.compile_flags['has_main']:
                raise Exception("Start main-function with \"Today I learned\"!")

            if not self.compile_flags['has_end']:
                raise Exception("End your letter with \"Your faithful student, Your Name\"!")

            compiled_file.writelines(["%s\n" % line for line in self._compiled_lines])

        if "test_" in file_name:
            to_debug_open = "{}".format(os.path.abspath(file_name)).replace("test", "py_program", 1)\
                .replace("test_", "test_debug_", 1)
        else:
            to_debug_open = "py_program/example_debug.py"

        if has_breakpoint:
            with open(to_debug_open, "w") as compiled_debug_file:
                for line in self._compiled_lines:
                    if 'breakpoint()' not in line:
                        compiled_debug_file.write(line + '\n')
                    else:
                        break

    def get_compiled_file_name(self):
        return self._fim_file.replace(".fimpp", ".py")

    def get_count_tabs(self):
        return "".join([" " for _ in range(0, self._compile_dirs["nesting"])])

    def add_tabs_level(self):
        self._compile_dirs["nesting"] += 4

    def delete_tabs_level(self):
        self._compile_dirs["nesting"] -= 4

    def get_inf_breakpoint(self):
        return has_breakpoint

    def compile_line(self, line, count_line):
        signs = {"was like": '==',
                 "was not like": '!=',
                 "had more than": '>',
                 "had less than": '<',
                 "had the same or more than": '>=',
                 "had the same or less than": '<='}

        if "Dear Princess Celestia:" in line:
            self._compile_dirs["in_class"] = True

        if "Today I learned" in line:
            self.compile_flags['has_main'] = True
            if self._compile_dirs["nesting"] >= 0:
                self.add_tabs_level()
            else:
                raise Exception("Indentation error in line %d" % count_line)
            return "if __name__ == '__main__':"

        if "That's what I did." in line:
            if self._compile_dirs["nesting"] > 0 or self._compile_dirs["in_func"]:
                if self._compile_dirs["in_func"]:
                    self._compiled_lines.insert(self._count_func + 1, '\n')
                    self._count_func += 1
                    self._compile_dirs["in_func"] = False
                self.delete_tabs_level()
            else:
                raise Exception("Unexpected end in line %d" % count_line)

            return ""

        if "That’s all about" in line:
            self._compile_dirs["in_class"] = False

        if "Your faithful student, " in line:
            self.compile_flags["has_end"] = True
            return ""

        match = re.search(r'Did you know that (.*) is (.*)\?', line)
        if match and '(' not in line:
            return "%s%s = %s" % (self.get_count_tabs(), match.group(1), match.group(2))

        match = re.search(r'Did you know that (.*) has many names\?', line)
        if match:
            return "%s%s = []" % (self.get_count_tabs(), match.group(1))

        match = re.search(r'(.*) ([0-9]+) is (.*)', line)
        if match:
            self._list_elem_count += 1
            if self._list_elem_count == int(match.group(2)):
                return "%s%s.append(%s)" % (self.get_count_tabs(), match.group(1), match.group(3))
            else:
                raise Exception("Enter indexes in order starting from 1")

        match = re.search(r'I (sang|wrote|said) (.*) ([0-9]+)', line)
        if match:
            if 'for i in range' in self._compiled_lines[self._compiled_lines.count(self) - 1]:
                self.add_tabs_level()
            if self._compile_dirs["in_func"]:
                self._count_func += 1

            return "%sprint(%s[%s])" % (self.get_count_tabs(), match.group(2), int(match.group(3))-1)

        match = re.search(r'I remember (.*) name ([0-9]+) as (.*)', line)
        if match:
            return "%s%s = %s[%s]" % (self.get_count_tabs(), match.group(3), match.group(1), int(match.group(2))-1)

        match = re.search(r'I did this ([0-9]+) times!', line)
        if match:
            return "%sfor i in range(0, %d):" % (self.get_count_tabs(), int(match.group(1)))

        match = re.search(r'(.*) (got|had) (\d) (more|less)', line)
        if match:
            if match.group(4) == 'more':
                sign = "+"
            else:
                sign = "-"
            return "%s%s %s= %d" % (self.get_count_tabs(), match.group(1), sign, int(match.group(3)))

        match = re.search(r'I got (.*) times ([0-9]+)', line)
        if match:
            sign = "*"
            return "%s%s %s= %d" % (self.get_count_tabs(), match.group(1), sign, int(match.group(2)))

        match = re.search(r'That\'s about (.*) with (.*)!', line)
        if match:
            self._compile_dirs["in_func"] = True
            self._count_func += 1

            args = match.group(2).split(' and ')
            return "%sdef %s(%s):" % ("", match.group(1), ", ".join(args))

        match = re.search(r'That\'s about (.*)!', line)
        if match:
            self._compile_dirs["in_func"] = True
            self._count_func += 1
            self.add_tabs_level()
            return "%sdef %s():" % ("", match.group(1))

        match = re.search(r'I learned about (.*)(| with (.*))(| then I told (.*))', line)
        if match:
            assign = ""
            args = []
            args_var = []
            var = ""
            if "with" not in match.group(1):
                assign = match.group(1)
            elif "with" in match.group(1):
                assign = match.group(1).split(' with ')[0]
                args.append(match.group(1).split(' with '))

                if "then I told" in match.group(1):
                    var = match.group(1).split(' then I told ')[1]
                    args_var.append(match.group(1).split(' then I told ')[0].split(" with ")[1])

            if args:

                if "and" not in args[0][1]:
                    args = args[0][1]
                else:
                    args = ", ".join(args[0][1].split(' and '))
                    if var != "":
                        args_var = ", ".join(args_var[0].split(' and '))
            else:
                args = ""

            if var == "":
                return "%s%s(%s)" % (self.get_count_tabs(), assign, args)

            else:
                return "%s%s = %s(%s)" % (self.get_count_tabs(), var, assign, args_var)

        match = re.search(r'I (sang|wrote|said) (.*)', line)
        if match:
            if 'for i in range' in self._compiled_lines[self._compiled_lines.count(self) - 1]:
                self.add_tabs_level()
            if self._compile_dirs["in_func"]:
                self._count_func += 1

            text = match.group(2)
            match = re.findall(r'\'\'([a-zA-Z0-9_]+)\'\'', text)
            if match:
                if len(match) == 1:
                    subs = " % "
                else:
                    subs = " % ("
                for i in match:
                    text = text.replace("''%s''" % i, "%s")
                    subs += i + ','
                if subs[-1] == ",":
                    subs = subs[:-1]
                if len(match) >= 1:
                    subs += ")"
                return '%sprint(%s' % (self.get_count_tabs(), text) + subs

            return '%sprint(%s)' % (self.get_count_tabs(), text)

        match = re.search(r'Did you know that (.*) (is|likes) \((.*)\) (.*)\?', line)
        if match:
            return "%s%s = %s(%s)" % (self.get_count_tabs(), match.group(1), match.group(3), match.group(4))

        match = re.search(
            r'(When|Here\'s what I did while|However,) ([a-zA-Z0-9_]+)'
            r' (had more than|'
            r'was like|had less than|'
            r'had the same or more than|had the same or less than|'
            r'was not like) (.*)',
            line)
        if match:
            tabs = self.get_count_tabs()
            self.add_tabs_level()
            if match.group(1) == "When":
                return "%s%s %s %s %s:" % (tabs, "if", match.group(2), signs[match.group(3)], match.group(4))
            if match.group(1) == "Here's what I did while":
                return "%s%s %s %s %s:" % (tabs, "while", match.group(2), signs[match.group(3)], match.group(4))
            if match.group(1) == "However,":
                return "%s%s %s %s %s:" % (tabs, "elif", match.group(2), signs[match.group(3)], match.group(4))

        if "P.S. " in line:
            return self.get_count_tabs() + line.replace("P.S. ", '# ').replace("\n", '')

        if 'I tried something else.' in line:
            tabs = self.get_count_tabs()
            self.add_tabs_level()
            return "%selse:" % tabs

        return ""
