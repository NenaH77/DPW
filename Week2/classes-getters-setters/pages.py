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
        self.__body = "Welcome to my OOP Python page!"

        self.close = '''
            </body>
        </html>
        '''


        self.whole_page =" "

    def update(self): #create function that is similar to printout function on other example
        self.whole_page = self.head + self.body + self.close
        self.whole_page = self.whole_page.format(**locals()) #Need this method to work

#above in the HTML tag, notice the self.body "welcome" tag. We also have another body in the 'main.py' page. If we browse we will notice the other body tag does not display on our page. To display the other html body tag do this:
    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, new_body):
        self.__body = new_body
        self.update()


    @property
    def title(self):#function
        return self.__title #getter; Will always return a getter READ ONLY

    @title.setter
    def title(self, new_title): #must have 2nd parameter
        self.__title = new_title #setters allow change WRITE ONLY
        self.update() #whenever anything changes update our info. This is in the 'main.py' under 'p.update'

    @property
    def css(self):
        return self.__css #getters always return

    @css.setter
    def css(self, new_css_file):
        self.__css = new_css_file #setter allows to change css but not read css
        self.update()#we don't have a 'p' inside the 'pages' class. 'pages' is class that creates the instances 'p'. Anytime we refer to an instance within its class we're always going use the word 'self'

'''
        def print_out(self): #create method for printing
        #return self.head + self.body + self.close
        all = self.head + self.body + self.close
        all = all.format(**locals())
        return all
'''