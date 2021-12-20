#!/usr/bin/env python3
import os
import glob
import jinja2
import subprocess
from datetime import datetime

this_folder = os.path.dirname(__file__)
test_cases_dir = os.path.join(this_folder, 'test_cases')

# define output markdown and PDF files
MARKDOWN_OUT = 'test_cases.md'
PDF_OUT = 'test_cases.pdf'

class RelEnvironment(jinja2.Environment):
    """Override join_path() to enable relative template paths."""
    def join_path(self, template, parent):
        return '/'.join([
            os.path.dirname(parent)
            .removeprefix(test_cases_dir)
            .replace('\\', '/'), template])


# Initialize the template engine.
jinja_env = RelEnvironment(
    loader=jinja2.FileSystemLoader(test_cases_dir))

with open(MARKDOWN_OUT, 'w') as f:

    f.write('<!-- Generated on {} from script `gendocs.py`\n'
            .format(datetime.now()))
    f.write('     DO NOT EDIT MANUALY! -->\n\n')

    for test in sorted(glob.glob(os.path.join(test_cases_dir, 'test*'))):
        test_name = test.split(os.path.sep)[-1]
        print(" Processing test {}".format(test_name))
        template = jinja_env.get_template(os.path.join(test_name,
                                                    "{}.md".format(test_name)))

        f.write(template.render())
        f.write('\n\n')

print(" [ '{:s}' created ]".format(MARKDOWN_OUT))

subprocess.run(["pandoc", MARKDOWN_OUT, "-V", "geometry:a4paper,margin=2.1cm",
                "--number-sections", "-o", PDF_OUT])

print(" [ '{:s}' created ]".format(PDF_OUT))

