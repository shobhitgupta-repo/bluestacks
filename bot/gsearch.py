from googlesearch import search

#google search class

class GoogleSearch:
    def __init__(self,query):
        self.query = query

    def search(self):
        results = search(query=self.query,tld='com',lang='en',num=5,start=0, stop=5, pause=2)
        return results
