class Shortner:
    def __init__(self, items):
        self.original_items = items

    def print_original_items(self):
        print(self.original_items)


class ListAndCharShortner(Shortner):
    def print_shortened_items(self):
        # Call the method to print the first three items of the dictionary
        print(self.original_items[0:3])

class DictionaryShortner(Shortner):
    def print_shortened_item(self):
        dict = self.original_items
        counter = 0
        result_dict ={}
        for(k, v) in dict.items():
            if(counter < 3):
                result_dict.update({k: v})
                counter +=1

        print(result_dict)

# Create an instance of DictionaryShortner with a dictionary
myShortner = DictionaryShortner({1: 'mike', 2: 'tom',3:'rebeca',4:'mike',5:'paul'})

# Call the method to print the shortened items
myShortner.print_shortened_item()

# Create an instance of ListAndCharShortner with a list
myshortner = ListAndCharShortner([1,2,3,4,5,6])

# Call the method to print the original items
myshortner.print_original_items()
