translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}
Word = input("Input a word in English:")
if Word in translations:
    print (translations [Word])
else:
    print ("No translations")