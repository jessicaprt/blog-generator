import sys
from blogs import Blogs

def create_json(url, blog_id):
    json_content = """
    "url": "{1}",
    "blog_image": "",
    "tags" : [],
    "title" : "",
    "body" : []""".format(blog_id, url)
    template = "{\n" + json_content + "\n}"
    new_blog_json = "%s.json" % url
    new_file = open(new_blog_json, "w")
    new_file.write(template)
    new_file.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("invalid arguments")
        exit()

    url = sys.argv[1]

    blogs = Blogs()
    blog_id = blogs.get_size()
    create_json(url, blog_id)
    print("%s.json' successfully created!" % url)