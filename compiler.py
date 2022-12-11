import os.path
import re


class Compiler:
    def __init__(self, fim_file):
        self._count_line = 0
        self._compiled_lines = []
        self._compile_dirs = {"nesting": 0, "in_func": False, "in_class": False}
        self._compile_flags = {"has_main": False, "has_end": False}
        if os.path.exists(fim_file):
            self._fim_file = fim_file
            with open(fim_file, "r", encoding='utf8') as file:
                self._text_lines = file.readlines()

            self.compile()

        else:
            raise Exception("Invalid file!")

    def compile(self):
        with open("py_program/{}".format(self.get_compiled_file_name()), "w") as compiled_file:
            for line in self._text_lines:
                self._count_line += 1
                line_compiled = self.compile_line(line, self._count_line)
                if line_compiled != "":
                    self._compiled_lines.append(line_compiled)
            if not self._compile_flags['has_main']:
                raise Exception("A pony letter must have \"Today I learned\"!")
            if not self._compile_flags['has_end']:
                raise Exception("You must end your letters with \"Your faithful student, Your Name\"!")

            compiled_file.writelines(["%s\n" % line for line in self._compiled_lines])

    def get_compiled_file_name(self):
        file = self._fim_file.replace(".fimpp", ".py")

        return file

    def get_count_tabs(self):
        return "".join([" " for _ in range(0, self._compile_dirs["nesting"])])

    def add_tabs_level(self):
        self._compile_dirs["nesting"] += 4

    def delete_tabs_level(self):
        self._compile_dirs["nesting"] -= 4

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
            self._compile_flags['has_main'] = True
            if self._compile_dirs["nesting"] >= 0:
                self.add_tabs_level()
            else:
                raise Exception("Indentation error in line %d" % count_line)
            return "if __name__ == '__main__':"

        if "P.S. " in line:
            return self.get_count_tabs() + line.replace("P.S. ", '')

        if "That's what I did." in line:
            if self._compile_dirs["nesting"] > 0:
                self.delete_tabs_level()
            else:
                raise Exception("Unexpected end in line %d" % count_line)

            return ""

        if "That’s all about" in line:
            self._compile_dirs["in_class"] = False

        if "I did nothing." in line:
            return "%spass" % self.get_count_tabs()

        if "Your faithful student, " in line:
            self._compile_flags["has_end"] = True
            return ""

        match = re.search(r'Did you know that (.*) is (.*)\?', line)
        if match:
            return "%s%s = %s" % (self.get_count_tabs(), match.group(1), match.group(2))

        match = re.search(r'I did this ([0-9]+) times!', line)
        if match:
            # self.add_tabs_level()
            return "%sfor i in range(0, %d):" % (self.get_count_tabs(), int(match.group(1)))

        match = re.search(r'(.*) (got|had) \d (more|less)', line)
        if match:
            sign = "+" if match.group(4) == 'more' else '-'
            return "%s%s %s= %d" % (self.get_count_tabs(), match.group(1), sign, int(match.group(3)))

        match = re.search(r'That\'s about (.*) with (.*)!', line)
        if match:
            args = match.group(2).split(' and ')
            self.add_tabs_level()
            return "%sdef %s(%s):" % (self.get_count_tabs(), match.group(1), ", ".join(args))

        match = re.search(r'That\'s about (.*)!', line)
        if match:
            self.add_tabs_level()
            return "%sdef %s():" % (self.get_count_tabs(), match.group(1))

        match = re.search(r'I (sang|wrote|said) "(.*)"', line)
        if match:
            if 'for i in range' in self._compiled_lines[self._compiled_lines.count(self) - 1]:
                self.add_tabs_level()

            printable = match.group(2)
            match = re.findall(r'\'\'([a-zA-Z0-9_]+)\'\'', printable)
            if match:
                if len(match) == 1:
                    subs = " % "
                else:
                    subs = " % ("
                for i in match:
                    printable = printable.replace("''%s''" % i, "%s")
                    subs += i + ','
                if subs.endswith(","):
                    subs = subs[:-1]
                if len(match) >= 1:
                    subs += ")"
                return '%sprint("%s"' % (self.get_count_tabs(), printable) + subs

            return '%sprint("%s")' % (self.get_count_tabs(), printable)

        match = re.search(r'Did you know that (.*) (is|likes) \((.*)\) (.*)\?', line)
        if match:
            return "%s%s = (%s) %s" % (self.get_count_tabs(), match.group(1), match.group(3), match.group(4))

        match = re.search(r'I learned about (.*)(| with (.*))(| then I told (.*))', line)
        if match:
            assign = ""
            args = ""
            try:
                if "with" not in match.group(2):
                    assign = match.group(3)
                else:
                    args = match.group(3)
                    try:
                        assign = match.group(5)
                    except:
                        pass
            except:
                pass

            if args != "":
                args = ",".join(args.split(' and '))
            if assign == "":
                return "%s%s(%s)" % (self.get_count_tabs(), match.group(1), args)
            else:
                return "%s%s = %s(%s)" % (self.get_count_tabs(), assign, match.group(1), args)

        match = re.search(
            r'(When|I did this while) ([a-zA-Z0-9_]+)'
            r' (had more than|'
            r'was like|had less than|'
            r'had the same or more than|had the same or less than|'
            r'was not like) (.*)',
            line)
        if match:
            tabs = self.get_count_tabs()
            self.add_tabs_level()
            structure = "if" if match.group(1) == 'When' else "while"
            value = match.group(4)
            return "%s%s %s %s %s:" % (tabs, structure, match.group(2), signs[match.group(3)], value)

        # Try/catch/finally block
        if 'I did it keeping a close eye out.' in line:
            self.add_tabs_level()
            return "%stry:" % self.get_count_tabs()
        if 'It didn\'t work, but I knew why.' in line:
            self.delete_tabs_level()
            tabs = self.get_count_tabs()
            self.add_tabs_level()
            return "%scatch:" % tabs
        if 'In the end, I did this instead.' in line:
            self.delete_tabs_level()
            tabs = self.get_count_tabs()
            self.add_tabs_level()
            return "%sfinally:" % tabs

        # Else
        if 'I tried something else.' in line:
            self.delete_tabs_level()
            tabs = self.get_count_tabs()
            self.add_tabs_level()
            return "%selse:" % tabs

        match = re.search(r'Surprisingly, something went wrong and I said \"(.*)\"!', line)
        if match:
            return "%sraise Exception(\"%s\")" % (self.get_count_tabs(), match.group(1))
        if "Surprisingly, something went wrong!" in line:
            return "%sraise Exception" % self.get_count_tabs()

        return ""
