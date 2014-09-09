class Page(object):
    def __init__(self):
        self.__title = "Welcome!" #__private
        self.__css = "css/style.css"

        # **REMEMBER** html tag{} needs to match the getter self.title
        self.head =  """
        <!DOCTYPE HTML>
        <html>
            <head>
                <title>{self.title}</title>
                <link href ="{self.css}" rel="stylesheet" type="text/css" />
            </head>
            <body>
        """
        self.body = "Welcome to my OOP Python page!"
        self.close = '''
            </body>
        </html>
        '''


        self.whole_page = ""

    def update(self): #create function that is similar to printout function on other example
        self.whole_page = self.head + self.body + self.close
        self.whole_page = self.whole_page.format(**locals()) #Need this method to work



    @property
    def title(self):
        return self.__title #getter; Will always return a getter READ ONLY

    @title.setter
    def title(self, new_title): #must have 2nd parameter
        self.__title = new_title #setters allow change WRITE ONLY


    @property
    def css(self):
        return self.__css #getters always return

    @css.setter
    def css(self, new_css_file):
        self.__css = new_css_file #setter allows to change css but not read css



'''
        def print_out(self): #create method for printing
        #return self.head + self.body + self.close
        all = self.head + self.body + self.close
        all = all.format(**locals())
        return all
'''