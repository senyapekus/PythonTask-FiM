import os
import re

from compiler import Compiler


def interpret():
    compiler = Compiler("test_fim.fimpp")
    return compiler


def get_py_program():
    answer = ""
    to_open = "{}".format(os.path.abspath(interpret().get_compiled_file_name())).replace("test", "py_program", 1)
    with open(to_open, "r", encoding='utf8') as p_file:
        text = p_file.readlines()
    for i in text:
        answer += i

    return answer


def test_has_start():
    assert interpret().compile_flags["has_main"] is True


def test_has_end():
    assert interpret().compile_flags["has_end"] is True


def test_has_main():
    assert "if __name__ == '__main__':\n" in get_py_program()


def test_variable_assignment():
    program = get_py_program()

    match = re.search(r"(.*) = (.*)", program)

    assert "%s%s = %s" % (interpret().get_count_tabs(),
                          match.group(1).replace(" ", ""),
                          match.group(2).replace(" ", "")) in program


def test_announcement_array():
    program = get_py_program()

    match = re.search(r"(.*) = \[]", program)

    assert "%s%s = []" % (interpret().get_count_tabs(),
                          match.group(1).replace(" ", "")) in program


def test_enumeration_in_array():
    program = get_py_program()

    match = re.search(r"(.*)\.append\((.*)\)", program)

    assert "%s%s.append(%s)" % (interpret().get_count_tabs(),
                                match.group(1).replace(" ", ""),
                                match.group(2).replace(" ", "")) in program


def test_get_value_in_array():
    program = get_py_program()

    match1 = re.search(r"print\((.*)\[([0-9]+)]\)", program)

    match2 = re.search(r"(.*) = (.*)\[([0-9]+)]", program)

    if match1:
        assert "%sprint(%s[%s])" % (interpret().get_count_tabs(),
                                    match1.group(1).replace(" ", ""),
                                    int(match1.group(2).replace(" ", ""))) in program
    elif match2:
        assert "%s%s = %s[%s]" % (interpret().get_count_tabs(),
                                  match2.group(1).replace(" ", ""),
                                  match2.group(2).replace(" ", ""),
                                  int(match2.group(3).replace(" ", "")))




