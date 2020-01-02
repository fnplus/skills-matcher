"""
contains the skills for the languages
"""


def get_java(spec='general'):
    """
    contains skills required for java developers
    :return: skills and advanced_skills
    """

    # user can ask for specific info or general info

    # general
    skills = ['Scala', 'Kotlin', 'Groovy', 'JVM Internals', 'SQL', 'MySQL', 'PostgreSQL', 'JSP Servlets'
        , 'REST', 'SOAP', 'XML', 'JSON', 'OOP', 'Multithreading', 'Serialization']

    advanced_skills = ['Blockchain', 'AWS', 'Big Data', 'Spring boot', 'Microservices']

    # specific info ==================================================================================
    java_build_tools = ['Maven', 'Gradle']
    web_tech = ['HTML', 'CSS', 'Javascript', 'JQuery']
    web_frameworks = ['SpringMVC', 'Play', 'Java Web Services']
    app_containers = ['JBoss', 'Jetty', 'WebSphere', 'WebLogic']
    testing_tools = ['JUnit', 'TestNG', 'Selenium']
    big_data = ['DBMS', 'Hadoop', 'SQL', 'JDBC']
    EE_components = ['Servlets', 'Java Beans', 'Java Server Pages']
    code_version_control = ['GitHub']
    # ===============================================================================================

    name_var_dict = [
        {'javabuildtools': java_build_tools},
        {'webtechnologies': web_tech},
        {'webframeworks': web_frameworks},
        {'applicationcontainers': app_containers},
        {'javatestingtools': testing_tools},
        {'bigdata': big_data},
        {'javaeecomponents': EE_components},
        {'codeversioncontrol': code_version_control}
    ]

    if spec is None:
        return skills  # if nothing else is passed

    if spec.lower() == 'general':
        return skills, advanced_skills

    else:
        for key in name_var_dict:
            temp = spec.lower().strip().replace(" ", "")
            if temp in list(key.keys())[0]:
                idx = name_var_dict.index(key)
                return name_var_dict[idx][list(key.keys())[0]]


