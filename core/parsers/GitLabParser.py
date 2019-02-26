from html.parser import HTMLParser

class GitLabParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.correct_tag = False
        self.status_message = ""

    def handle_starttag(self, tag, attrs):
        if tag == "strong":
           # Check the list of defined attributes.
            for key, value in attrs:
                if key == 'id' and 'statusbar_text' in value:
                    self.correct_tag = True
    
    def handle_endtag(self, tag):
        if tag == "strong" and self.correct_tag:
            self.correct_tag = False

    
    def handle_data(self, data):
        if self.correct_tag:
            self.status_message = data

    def getStatus(self):
        return self.status_message
