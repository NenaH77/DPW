__author__ = 'NenaH77'

class Page():
    def __init__(self):
#HTML heading
        self.page_header = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Salary Calculator</title>
        <link href = "css/main.css" rel="stylesheet" type="text/css" />
        <link href='http://fonts.googleapis.com/css?family=Lily+Script+One' rel='stylesheet' type='text/css'>
    </head>
    <body> '''

#HTML body
        self.page_body = '''
    <div id="wrapper">
        <header>
            <h1>Salary</h1>
            <ul>
                <li><a href="?salary=van" class="ppl">Van</a></li>
                <li><a href="?salary=lily" class="ppl">Lily</a></li>
                <li><a href="?salary=adriana" class="ppl">Adriana</a></li>
                <li><a href="?salary=alexandra" class="ppl">Alexandra</a></li>
            </ul>
        </header>

    </div>
'''
#HTML closing
        self.page_close = '''
    </body>
    <footer Encapsulation-Calculator | Angelica M. Dinh</footer>
</html>
'''

    #function that will open contents
    def page_header(self):
        return self.page_header

    def page_body(self):
        return self.page_body

    def page_close(self):
        return self.page_close