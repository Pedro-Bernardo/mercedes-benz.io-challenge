from html.parser import HTMLParser

class BitBucketParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.correct_div = False
        self.correct_span = False
        self.status_message = ""

    def handle_starttag(self, tag, attrs):
        if tag == "div":
           # Check the list of defined attributes.
            for key, value in attrs:
                if key == 'class' and 'page-status' in value:
                    self.correct_div = True
        elif tag == "span":
            # Check the list of defined attributes.
            for key, value in attrs:
                if self.correct_div and key == 'class' and 'status' in value:
                    self.correct_span = True
    
    def handle_endtag(self, tag):
        if tag == "div" and self.correct_div:
            self.correct_div = False
        elif tag == "span" and self.correct_span:
            self.correct_span = False

    
    def handle_data(self, data):
        if self.correct_span:
            self.status_message = data

    def getStatus(self):
        return self.status_message
