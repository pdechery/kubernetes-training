from flask import Flask

app = Flask(__name__)

access_count = 0

@app.route("/")
def count_access():

    result = 0

    global access_count
    access_count += 1
    
    with open('teste.txt', 'w') as file:
        file.write(str(access_count))

    with open('teste.txt', 'r') as file:
        result = file.read()

    return f"Você acessou este site {result} vezes!"




