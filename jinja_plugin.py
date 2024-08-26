# jinja_plugin.py
import os
from jinja2 import Environment, FileSystemLoader

class JinjaPlugin:
    def __init__(self, template_dir='templates'):
        """Template plugin for Jinja2 that allows the use of Jinja2 templates in FastHTML

        Args:
            template_dir (str, optional): The directory to load templates from. Defaults to 'templates'.
        """
        if not os.path.exists(template_dir):
            raise ValueError(f"Template directory {template_dir} does not exist")

        self.template_dir = template_dir
        self.env = Environment(loader=FileSystemLoader(self.template_dir))

    def render_template(self, template_name, context):
        if not os.path.exists(os.path.join(self.template_dir, template_name)):
            raise ValueError(f"Template {template_name} does not exist")
        return self.env.get_template(template_name).render(context)

def render_template(template_name, **context):
    return JinjaPlugin().render_template(template_name, context)
