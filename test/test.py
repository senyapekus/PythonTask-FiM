import os
import re

from compiler import Compiler


def interpret():
    compiler_file = Compiler("test_fim.fimpp")
    return compiler_file


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
                                  int(match2.group(3).replace(" ", ""))) in program


def test_cycle_for():
    program = get_py_program()

    match = re.search(r'for i in range\(0, ([0-9]+)\):', program)

    assert "%sfor i in range(0, %d):" % (interpret().get_count_tabs(),
                                         int(match.group(1).replace(" ", ""))) in program


def test_cycle_while():
    program = get_py_program()

    match = re.search(r'while (.*) (\W) ([0-9]+):', program)

    assert "%s%s %s %s %s:" % (interpret().get_count_tabs(),
                               "while",
                               match.group(1).replace(" ", ""),
                               match.group(2),
                               match.group(3).replace(" ", "")) in program


def test_changing_variables():
    program = get_py_program()

    match = re.search(r'(.*) (.*)= ([0-9]+)', program)

    assert "%s%s %s= %d" % (interpret().get_count_tabs(),
                            match.group(1).replace(" ", ""),
                            match.group(2).replace(" ", ""),
                            int(match.group(3).replace(" ", ""))) in program


def test_condition():
    program = get_py_program()

    match = re.search(r'(.*) (.*) (\W) (.*):', program)
    tabs = interpret().get_count_tabs()

    assert "%s%s %s %s %s:" % (tabs,
                               match.group(1).replace(" ", ""),
                               match.group(2).replace(" ", ""),
                               match.group(3).replace(" ", ""),
                               match.group(4).replace(" ", "")) in program


def test_has_breakpoint():
    assert interpret().get_inf_breakpoint() is True


def test_has_comment():
    program = get_py_program()

    assert "#" in program


def test_explicit_cast():
    program = get_py_program()

    match = re.search(r"(.*) = (.*)\((.*)\)", program)

    assert "%s%s = %s(%s)" % (interpret().get_count_tabs(),
                              match.group(1).replace(" ", ""),
                              match.group(2).replace(" ", ""),
                              match.group(3).replace(" ", "")) in program


def test_create_func_with_args():
    program = get_py_program()

    match = re.search(r"def (.*)\((.*)\):", program)
    args = match.group(2).replace(" ", "").split(',')

    assert "%sdef %s(%s):" % ("", match.group(1).replace(" ", ""),
                              ", ".join(args)) in program


def test_create_func_without_args():
    program = get_py_program()

    match = re.search(r"def (.*)\(\):", program)

    assert "%sdef %s():" % ("", match.group(1).replace(" ", "")) in program


def test_call_func_with_args():
    program = get_py_program()

    match = re.search(r"(.*) = (.*)\((.*)\)", program)
    args = match.group(3)

    assert "%s%s = %s(%s)" % (interpret().get_count_tabs(),
                              match.group(1).replace(" ", ""),
                              match.group(2).replace(" ", ""),
                              args) in program


def test_call_func_without_args():
    program = get_py_program()

    match = re.search(r"(.*)\(\)", program)

    assert "%s%s()" % (interpret().get_count_tabs(),
                       match.group(1).replace(" ", "")) in program
