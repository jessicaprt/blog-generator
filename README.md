# Blog Generator:

Below are the procedures on how to use the blog-generator to create a new blog

[Generating JSON file for the blog content](#generating-json-file-for-the-blog-content)

[Inside the JSON file and filling in the details](#inside-the-json-file-and-filling-in-the-details)

[Creating the static blog page](#creating-the-static-blog-page)

[HTML template changes and modifying all blogs](#html-template-changes-and-modifying-all-blogs)



## Generating JSON file for the blog content
Generate the json file to put the blog contents. Run new-blog.py and add the url to your new blog.
```
> python new-blog.py new-blog
```

This creates the file **new-blog.json**

## Inside the JSON file and filling in the details
The generated json file will look as follows:
```json
    {
        "url": "new-blog",
        "blog_image": "",
        "tags" : [],
        "title" : "",
        "body" : []    
    }
```
| key | what to add | example |
| --- | ----------- | ------- |
| `url` | this is automatically generated | |
| `blog_image`| a file name that exists in the blogs/images folder **NOTE:** only one image can be added to every blog post | _"new_blog_image.jpg"_
| `tags` | a list of tags for the blog post | _["android", "music", "travel"]_ |
| `title` | The title of the blog post | _"New Blog"_ |
| `body` | The main content of the blog. Each paragraph should be a separate element in the list | _["This is paragraph 1", "This is paragraph2"]_ 

## Creating the static blog page

Once filling in the json is completed, the next step is to generate the html file for the blog page. To do so, run add-blog.py and add the same url to your blog. 
```
> python add-blog.py new-blog
```

The url to the new blog post will now be **"_website.com_/blogs/new-blog>"**

## HTML template changes and modifying all blogs

In case you want to update the look of each page, it can easily be done by modifying the blog-template.template file. Once it is updated, you can easily update all blog posts by running
```
> python modify-blogs.py
```