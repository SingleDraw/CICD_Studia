import os
from flask import Flask

application = Flask(__name__)

ENV = os.environ.get('FLASK_ENV', 'developerskie')

@application.route('/')
def hello_world():
    return(f"""
        <h1>Hello, Big Data z Pythonem!</h1>
        <p>Środowisko <b>{ ENV }</b></p>
        <p>Przykład CI/CD - automatyczne wdrażanie!</p>
    """)

if __name__ == '__main__':
    application.run(debug=True)
