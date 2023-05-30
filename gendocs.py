#!/usr/bin/env python3
import os
import re
import glob
import jinja2
import subprocess
from datetime import datetime
from textx import metamodel_from_str

this_folder = os.path.dirname(__file__)
test_cases_dir = os.path.join(this_folder, 'test_cases')

# Collect test files information
test_files = {}
for idx, test in enumerate(sorted(glob.glob(os.path.join(test_cases_dir, 'test*')))):
    test_name = test.split(os.path.sep)[-1]
    test_file = os.path.realpath(os.path.join(test, "{}.md".format(test_name)))
    with open(test_file, 'r') as f:
        for line in f:
            if line.startswith('# '):
                title = line[2:].strip()
                break
    test_files[test_file] = (idx, title)


# textX grammar for parsing markdown links
mdlinks_grammar = r"""
Markdown[noskipws]: content+=LinkOrOther;
LinkOrOther: Link | /.|\n/;
Link: '[' title=/[^\]]*/ '](' target=/[^)]*/ ')';
"""
md_mm = metamodel_from_str(mdlinks_grammar)


def make_section_anchor(section):
    """
    Transforms input section title to its anchor by replacing all
    non alphanumerics/spaces/dots to dashes.
    """
    section = section.strip()
    return re.sub(r'\s+', '-', re.sub(r'[^a-zA-Z0-9 \t.-]+', '', section)).lower()


def localize_links(md_content, md_file_dir):
    """
    Parses the given markdown file content, extracts and localizes links.
    """
    model = md_mm.model_from_str(md_content)
    new_content = []
    for elem in model.content:
        if hasattr(elem, 'target'):
            # Transform target link
            # 1. Get section if any (part after #).
            if '#' in elem.target:
                target_file, target_section = elem.target.split('#')
            else:
                target_file = elem.target
                target_section = None
            # 2. Calculate section index (there are sections with the same
            #    name). For titles we assume they are unique across the
            #    document.
            target_file = os.path.realpath(os.path.join(md_file_dir,
                                                        target_file))
            if target_section is None:
                new_content.append(
                    '[{}](#{})'
                    .format(elem.title,
                            make_section_anchor(test_files[target_file][1])))
            else:
                # We have a section. It is not unique so we must generate
                # suffix.
                suffix = test_files[target_file][0]
                new_content.append(
                    '[{}](#{}{})'
                    .format(elem.title,
                            target_section,
                            '-{}'.format(suffix) if suffix > 0 else ''))
        else:
            new_content.append(elem)
    return ''.join(new_content)


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

        f.write(localize_links(template.render(), os.path.join(test_cases_dir, test)))
        f.write('\n\n')

print(" [ '{:s}' created ]".format(MARKDOWN_OUT))

subprocess.run(["pandoc", MARKDOWN_OUT, "-V", "geometry:a4paper,margin=2.1cm",
                "--number-sections", "-o", PDF_OUT])

print(" [ '{:s}' created ]".format(PDF_OUT))

