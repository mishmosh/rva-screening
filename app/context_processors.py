import os
import flask
from markdown import Markdown

def inject_static_url():
    """Adds `STATIC_URL` variable to template context.
    """
    app = flask.current_app
    static_url = os.environ.get('STATIC_URL', app.static_url_path)
    if not static_url.endswith('/'):
        static_url += '/'
    return dict(
        static_url=static_url
    )

def inject_example_data():
    """Adds `EXAMPLE` variable to template context, if we need to fake data
    somewhere.
    """
    from app import example_data
    return dict(EXAMPLE=example_data)

def inject_template_constants():
    from app import template_constants
    return dict(CONSTANTS=template_constants)

def register_markdown_filter(app):
    md = Markdown(extensions=[
        'markdown.extensions.tables',
        'markdown.extensions.smarty'
        ])
    def markdown_filter(text, *args, **kwargs):
        return md.convert(text, *args, **kwargs)
    app.jinja_env.filters['markdown'] = markdown_filter


