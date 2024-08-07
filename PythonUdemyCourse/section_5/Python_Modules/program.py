# Module and Sub_Package
from utils.world import ListAndCharShortner, DictionaryShortner
myShortner = DictionaryShortner({1: 'mike', 2: 'tom',3:'abcdefgh',4:'mike',5:'paul'})
# Call the method to print the shortened items
myShortner.print_shortened_item()
