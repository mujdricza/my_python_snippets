from string import Template

def template_exp1():
    template: Template = Template("Hello, $name! You are $age old.")
    message: str = template.substitute(name="Bob", age=18)
    print(message)

