import url
from parserService import ParserService


class GetAbout:
    def __init__(self):
        self.anekdots = []
        self.old_anekdots = []
        self.history = []
        self.old_history = []
        self.aphorism = []
        self.old_aphorism = []

    def get_about(self, url: str, item: list, old_item: list):
        if not item:
            item = ParserService.parser(url)
        amount = len(item) - 1
        text = item.pop(0)
        old_item.append(text)
        if not amount:
            item = old_item
            old_item = []
        return item, old_item, amount, text

    def get_about_anekdot(self, url: str):
        self.anekdots, self.old_anekdots, amountA, anekdot = self.get_about(url, self.anekdots, self.old_anekdots)
        return anekdot, amountA

    def get_about_history(self, url: str):
        self.history, self.old_history, amountH, history = self.get_about(url, self.history, self.old_history)
        return history, amountH

    def get_about_aphorism(self, url: str):
        self.aphorism, self.old_aphorism, amountAp, aphorism = self.get_about(url, self.aphorism, self.old_aphorism)
        return aphorism, amountAp


if __name__ == '__main__':
    g = GetAbout()
    print(g.get_about_anekdot(*url.anekdot.values()))
