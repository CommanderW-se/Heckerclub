import json
class analize:
    def __init__(self,convMemory : dict):
        self.userInputs = []
        self.convMemory = convMemory
        with open ("topic.json","r",encoding="utf-8") as data:
            self.keyWord = json.load(data)

    def answer(self,uInput):
        topic = set()
        likelynes = {}
        for key, items in self.keyWord.items():
            for item in items:
                uInputWords = uInput.split()
                for word in uInputWords:
                    if item == word:
                        if key in topic:
                            likelynes[key] += 1
                        else:
                            likelynes[key] = 1
                            topic.add(key)
                    
        return likelynes


test = analize([])
run = True
while run:
    print("Hello wanderer.")
    uInput = input("> ")
    if uInput != "exit":
        print(test.answer(uInput.lower()))
    else:
        print("Goodbye wanderer.")
        run = False