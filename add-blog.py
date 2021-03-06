import json
import sys
import datetime
import os
from pprint import pprint
from blogs import Blogs
	
def get_json(json_file):
	with open(json_file) as f:
		return json.load(f)

def remove_json_file(url):
    os.remove(url)
    
def add_to_blog(new_blog, url):
    curr = Blogs().get_data()
    cur_size = len(curr)
    curr["blogs"].append(new_blog)

    w = open("blogs.json", 'w')
    w.write(json.dumps(curr))

def get_current_date():
    now = datetime.datetime.now()
    return '{0}-{1:02d}-{2:02d}'.format(now.year, now.month, now.day)

def is_blog_page(url):
    url_page = "../blogs/{0}.html".format(url)
    print("checking %s" % url_page)
    return os.path.isfile(url_page)

def generate_blog(title, blog_url):
    file = open("blog-template.template", "r")
    template = str(file.read())
    html_template = template.format(title, blog_url)

    new_page_file = "../blogs/%s.html" % blog_url

    new_page = open(new_page_file,"w") 
    new_page.write(html_template) 
    new_page.close()

def is_image_file_exists(url):
    image_file = "../blogs/images/%s" % url

    if not os.path.isfile(image_file) and not url == "":
        print("invalid image: %s does not exist" % image_file)
        exit()

if __name__ == "__main__":
    print("adding to blogs.json...")
    if len(sys.argv) != 2:
        print("invalid arguments")
        exit()
    
    url = sys.argv[1]
    json_file = "%s.json" % url
    if not os.path.isfile(json_file):
        print("invalid filename: %s does not exist" % json_file)
        exit()
    
    new_blog_json = get_json(json_file)
    
    is_image_file_exists(new_blog_json["blog_image"])

    new_blog = dict()
    new_blog["id"] = len(Blogs().get_data()["blogs"])
    new_blog["title"] = new_blog_json["title"]
    new_blog["url"] = url
    new_blog["created_at"] = get_current_date()
    new_blog["body"] = new_blog_json["body"]
    new_blog["tags"] = new_blog_json["tags"]
    new_blog["blog_image"] = new_blog_json["blog_image"]
    add_to_blog(new_blog, json_file)
    print("added to blogs.json!")

    print("generating static page...")

    json_data = Blogs().get_data()
    blogs = json_data["blogs"]

    for blog in blogs:
        if is_blog_page(blog["url"]):
            print("pass")
        else:
            generate_blog(blog["title"], blog["url"])
            print("New blog successfully created")
            remove_json_file(json_file)