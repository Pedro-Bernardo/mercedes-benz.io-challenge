from html.parser import HTMLParser

class SlackParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.correct_div = False
        self.correct_tag = False
        self.status_message = ""

    def handle_starttag(self, tag, attrs):
        if tag == "div":
           # Check the list of defined attributes.
            for key, value in attrs:
                if key == 'class' and 'container' in value:
                    self.correct_div = True
        elif tag == "h1" and self.correct_div:
            self.correct_tag = True
    
    def handle_endtag(self, tag):
        if tag == "div" and self.correct_div:
            self.correct_div = False
        elif tag == "h1" and self.correct_tag:
            self.correct_tag = False
    
    def handle_data(self, data):
        if self.correct_tag:
            self.status_message = data

    def getStatus(self):
        return self.status_message
