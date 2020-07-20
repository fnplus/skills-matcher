"""
This module will contain mappings of programming languages to skills.
Users can inquire with programming languages and see suggestions that they can work on for improvement and further
advancement.
"""

from skills import *

languages = ['java', 'python', 'html', 'css', 'javascript', 'ruby', 'matlab', 'r']


def get_skills(lang, spec=None):
    """
    returns the list of skills required for this language
    :param spec: specification for different things
    :param lang: language name (string)
    :return: list of skills
    """

    if lang.lower() == 'java':
        output = get_java(spec)
        if spec is not None:
            print(f"Our suggestions for {spec} are: ", end='')
            print(*output[:-1], sep=', ', end='')
            print(f" and {output[-1]}.\n")
        else:
            print("Our suggestions for are: ", end='')
            print(*output[:-1], sep=', ', end='')
            print(f" and {output[-1]}.\n")
    elif lang.lower() == 'python':
        output = get_python(spec)
        if spec is not None:
            print(f"Our suggestions for {spec} are: ", end='')
            print(*output[:-1], sep=', ', end='')
            print(f" and {output[-1]}.\n")
        else:
            print("Our suggestions for are: ", end='')
            print(*output[:-1], sep=', ', end='')
            print(f" and {output[-1]}.\n")


if __name__ == '__main__':
    print("Languages available are: ", end='')
    print(*languages[:-1], sep=', ', end='')
    print(f" and {languages[-1]}.\n\n")
    lang = input("Enter the language you want to inquire about: ")

    while lang.lower() not in languages:
        lang = input("Enter the language you want to inquire about: ")

    spec = input(f"Now please enter a specification, if any, you want to inquire about for {lang}: ")

    if spec == "":
        spec = None

    get_skills(lang, spec)


