class Game:
    def __init__(self, tag):
        self.title = self.get_text(tag, 'a.title')
        self.comp = self.get_attr(tag, 'a.subtitle', 'title')
        self.price = self.get_text(tag, 'span.display-price')

        self.rating = self.get_rating(tag, 'div.current-rating', 'style')
        
    def get_rating(self, parent_tag, selector, attr_name):
        percent_strs = self.get_attr(parent_tag, selector, attr_name).split(' ')
        if len(percent_strs) < 2:
            print("PPPP>>", self.title)
            return 0.0
        else:
            return float(percent_strs[1].replace('%;', ''))

    def get_text(self, parent_tag, selector):
        tag = self.get_tag(parent_tag, selector)
        return tag.text.strip()

    def get_attr(self, parent_tag, selector, attr_name):
        tag = self.get_tag(parent_tag, selector)
        if tag != None:
            return tag.get(attr_name).strip()
        else:
            return ""

    def get_tag(self, parent_tag, selector):
        tag = parent_tag.select(selector)
        if tag == None or len(tag) == 0:
            return None
        else:
            return tag[0]

    def __str__(self):
        return "2222{}\t{}\t{}\t{:.2f}".format(self.title, self.comp, self.price, self.rating)

    def to_str(self):
        return "{}\t{}\t{}\t{:.1f}".format(self.title, self.comp, self.price, self.rating)

if __name__ == '__main__':
    print("=============================", __name__)
