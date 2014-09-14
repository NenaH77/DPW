__author__ = 'NenaH77'

class Page():
    def __init__(self):
#HTML heading
        self.page_header = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Salary Calculator</title>
        <link href = "css/style.css" rel="stylesheet" type="text/css" />
        <link href='http://fonts.googleapis.com/css?family=Corben' rel='stylesheet' type='text/css'>
    </head>
    <body>'''

#HTML body
        self.page_body = '''
    <div id="wrapper">
    <header>
        <h1>Salary</h1>
        <ul class="display">
            <li><a href="?salary=0" class="salary">Van</li>
            <li><a href="?salary=1" class="salary">Lily</li>
            <li><a href="?salary=2" class="salary">Adriana</li>
            <li><a href="?salary=3" class="salary">Alexandra</li>
        </ul>
    </div>
'''
#HTML closing
        self.page_close = '''
    </body>
    <footer> Encapsulation-Calculator | Angelica M. Dinh</footer>
</html>
    '''

    #function that will open contents
    def page_header(self):
        return self.page_header

    def page_body(self):
        return self.page_body

    def page_close(self):
        return self.page_close