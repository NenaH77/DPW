__author__ = 'NenaH77'

class Page(object):
    def __init__(self):
        self.open = '''
<!DOCTYPE html>
<html>
    <head>
        <title>Movie Info</title>
    </head>
    <body>
        <div class="wrapper">
    '''
        self.content = "This is my content"
        self.close = '''
        </div>
    </body>
</html> '''
        self.all = ""

    def open(self):
        return self.open

    def content(self):
        return self.content

    def close(self):
        return self.close


    def print_out(self):
        self.update()
        return self.all

    def update(self):
        self.all = self.open + self.content + self.close
        self.all = self.all.format(**locals())


class Movie(Page):
    def __init__(self):
        #calling the constructor
        #Page.__init__()
        super(Page, self).__init__()

        self.form = '''
        <form method="GET">
            <input type="text" name="actor" placeholder="Actor Name" required />
            <input type="text" name="title" placeholder="Movie Title" required />
            <button class="btn">Search</button>
        </form>
        '''

        self.body = '''
        <p>Here are your results</p>
        '''
    def form(self):
        return self.form

    def body(self):
        return self.body

    def update(self):
        self.all = self.open + self.form + self.body + self.content + self.close
        self.all = self.all.format(**locals())

    def total(self):
        self.all = self.open + self.body + self.close
        self.all = self.all.format(**locals())
