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
        #self.content = "This is my content"
        self.form = '''
        <form method="GET">
            <input type="text" name="search" placeholder="Movie Title" required />
            <button class="btn">Search</button>
        </form>
        '''
        self.close = '''
        </div>
    </body>
</html> '''
        self.all = ""

    def open(self):
        return self.open

    def form(self):
        return self.form

    def close(self):
        return self.close


    def print_out(self):
        self.update()
        return self.all

    def update(self):
        self.all = self.open + self.form + self.close
        self.all = self.all.format(**locals())


