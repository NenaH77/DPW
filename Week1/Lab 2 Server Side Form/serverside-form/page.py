__author__ = 'NenaH77'
class page(object):
    def __init__(self):#constructor function
        self.title = "Orlando Singles" #attribute of page
        self.css = "css/style.css" #css info
        #heading
        self.page_header = '''<!DOCTYPE HTML>
<html>
    <head>
        <title>Orlando Singles</title>
        <link href = "{main.css}" rel="stylesheet" type="text/css" />
    </head>
    <body> '''
#body
        self.page_content = '''<form method="GET" action="" >
        <label for="first_name">First Name: </label>
        <input class="input" type="text" name="first_name" placeholder="Enter your First Name" required /><br>

        <label for="last_name">Last Name: </label>
        <input class="input" type="text" name="last_name" placeholder="Enter your Last Name"  required /><br>

        <label for="email">Email Address: </label>
        <input class="input" type="email" name="email" placeholder="johndoe@yahoo.com" required /><br>

        <label for="phone">Phone Number: </label>
        <input class="input" type="phone" name="phone" placeholder="888-123-1234" required /><br>

        <label for="aboutyou">About You: </label><br>
        <textarea class="input" name="aboutyou"></textarea><br>

        <label for=religion">Religion:</label>
        <select class="input" name="religion">
            <optgroup label="Believer">
                <option value="christianity">Christianity</option>
                <option value="islam">Islam</option>
                <option value="hindu">Hindu</option>
                <option value="judaism">Judaism</option>
                <option value="spiritism">Spiritism</option>
                <option value="buddhist">Buddhist</option>
            <optgroup label="Non Believer">
                <option value="atheist">Atheist</option>
                <option value="anti">Anti-theist</option>
                <option value="agnostic">Agnostic</option>
                <option value="skeptic">Skeptic</option>
                <option value="free">Freethinker</option>
                <option value="humanist">Humanist</option>
        </select><br>

        <label for=education">Education:</label>
        <select class="input" name='edu'>
                <option value="high">High School</option>
                <option value="assoc">Associates</option>
                <option value="bach">Bachelor</option>
                <option value="master">Masters</option>
                <option value="phd">PhD</option>
        </select><br>

        <label for="gender">Interested in:</label><br>
        <input class="input" type="radio" name="gender" value="men">Men<br>
        <input class="input" type="radio" name="gender" value="women">Women<br>

        <label for="ethnicity">Ethnicity: </label><br>
        <input class="input" type="checkbox" name="ethnicity" value="white">White<br>
        <input class="input" type="checkbox" name="ethnicity" value="black">Black<br>
        <input class="input" type="checkbox" name="ethnicity" value="latino">Latino<br>
        <input class="input" type="checkbox" name="ethnicity" value="asian">Asian<br>

        <input type="submit" value="Submit">
        </form>
        '''

        self.page_end = '''
        <footer>
            <p>Copyright &copy; 2014 <strong>Orlando Singles</strong></p>
        </footer>
    </body>
</html>
'''

#def header(self):
    #return self.header

#def content(self):
    #return self.content

#def footer(self):
    #return self.footer

def print_out(self):
    all = self.page_header + self.page_content + self.page_footer
    return all