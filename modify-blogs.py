import json
import sys
import os
from blogs import Blogs

def modify_blog(title, blog_url):
    file = open("blog-template.template", "r")
    template = str(file.read())
    html_template = template.format(title, blog_url)

    page_file = "../blogs/%s.html" % blog_url

    page = open(page_file,"w") 
    page.write(html_template) 
    page.close()
    print("successfully modified %s" % page_file)

if __name__ == "__main__":
    json_data = Blogs().get_data()
    blogs = json_data["blogs"]

    for blog in blogs:
        modify_blog(blog["title"], blog["url"])