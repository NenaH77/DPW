class Page(object):
    def __init__(self): #constructor function
        self.title = "Welcome!" #Attribute is the page element: Title of page, Head of page, Body of page, etc
        self.css = "css/style.css" # DON'T FORGET TO ADD CSS INFO INSIDE 'app.yaml'
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
    def print_out(self): #create method for printing
        #return self.head + self.body + self.close
        all = self.head + self.body + self.close
        all = all.format(**locals())
        return all
