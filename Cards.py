class Cards:
    def create_deck(self):
        cards = []
        suits = ["swords", "dinero", "clubs", "cups"]
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        
        for num in nums:
            for suit in suits:
                cards.append(str(num) + " of " + suit)
        print(cards)
        print(len(cards))
        return cards

# Create an instance of Cards and call the method
deck = Cards()
deck.create_deck()