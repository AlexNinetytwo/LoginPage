import re

def newClass(old_name, new_name):
    with open('C:\programming\schoolProject\LoginPage\FLASK WEB APPLICATION\website\models.py','r') as file:
        content = file.read()
    
    pattern = r'\b{}\b'.format(re.escape(old_name))
    content.replace('KeinName', new_name)
    with open('C:\programming\schoolProject\LoginPage\FLASK WEB APPLICATION\website\models.py', 'w') as file:
        file.write(content)

    with open('C:\programming\schoolProject\LoginPage\FLASK WEB APPLICATION\website\createInstance.py','r') as file:
        content = file.read()
    content.replace('unnamed', name)
    with open('C:\programming\schoolProject\LoginPage\FLASK WEB APPLICATION\website\createInstance.py', 'w') as file:
        file.write(content)