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