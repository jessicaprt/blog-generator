import json

class Blogs:
    def get_data(self):
       with open('blogs.json') as f:
        return json.load(f) 
        
    def get_size(self):
        return len(self.get_data()["blogs"])