# jinja-fasthtml-plugin
FastHTML Jinja render

Allows rendering of templates in FastHTML using the excellent Jinja2 template engine.

## Credits
 * FastHTML (Jeremy Howard) - https://www.fastht.ml/
 * Jinja2 (Palettes Project) - https://jinja.palletsprojects.com/

## Usage

Simply import the function and render.  It is so small (thanks to Palletes Project) 

```python
# this is how to import FastHTML Python
from fasthtml.common import *

# Here is how to import
from jinja_plugin import render_template

app = FastHTML()

@app.route('/')
def get():
    # this is similar to a Flask call, from the ./templates directory
    return render_template('home.html')

@app.route('/about')
@app.route('/about/<name>')
def get(name="Stranger"):
    # supports variables (context)
    return render_template('variables.html', name="Jeff")

if __name__ == '__main__':
    # Flask-like serves on port 5000
    serve(host="0.0.0.0",port=5000)
```

This plug-in (shim) allows rendering of Jinja2 templates.  Supports 'import' and 'extends' directives of Jinja2.  However, it doesn't support all of Flask's goodies.

Although it is not necessarily in the spirit of FastHTML to render an external template, they have written a good project that is surprisingly fun to use and very Pythonic.
