from bottle import route, run, get, static_file
import bottle
import os

@route('/')
def main():
    return static_file('carinhas.html', root='src')
    #return "Benvindo ao Jogo das Carinhas"

@get('/<filename:re:.*\.html>')
def html(filename):
    return static_file(filename, root='src')

@get('/<filename:re:.*\.js>')
def javascript(filename):
    return static_file(filename, root='libs')

@get('/<filename:re:.*\.py>')
def python(filename):
    return static_file(filename, root='src')

@get('/<filename:re:.*\.jpg>')
def imagejpg(filename):
    return static_file(filename, root='src')

if __name__ == "__main__":
    #run(host='i-quarto.herokuapp.com', port=80, debug=True)
    run(server='gunicorn', host='0.0.0.0', port=int(os.environ.get("PORT", 8080)), debug=True, workers=1)
    #run(host='localhost', port=8080, debug=True)

app = bottle.default_app()
