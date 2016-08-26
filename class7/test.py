#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import jinja2

current_dir = os.path.dirname(__file__)

print("Current Dir: " + current_dir)

template_dir = os.path.join(current_dir, "templates")

print("Template Dir: " + template_dir)

jinja_env = jinja2.Environment(
	loader = jinja2.FileSystemLoader(template_dir)
)

movies = ["Forrest Gump", "Goonies"] 

template = jinja_env.get_template("main.html")
response = template.render(movies=movies)

print(response)
