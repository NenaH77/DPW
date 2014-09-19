__author__ = 'NenaH77'

class FormPage(object):
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
            <input type="text" name="movie" placeholder="Movie Title" required />
            <button class="btn">Search</button>
        </form>
        '''
        self.close = '''
        </div>
    </body>
</html> '''

    def open(self):
        return self.open

    def form(self):
        return self.form

    def close(self):
        return self.close


    def print_out(self):
        return self.open + self.form + self.close

    def new_print_out(self, new_body):
        return self.open + new_body + self.close
