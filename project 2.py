import nltk
#nltk.download('omw-1.4') remove hashtag if error raise of download
import speech_recognition as sr
from PyDictionary import PyDictionary
from nltk.corpus import wordnet
dictionary = PyDictionary()
 
def speech():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print("talk")
    audio_text = r.listen(source)
    try:
      t = r.recognize_google(audio_text)
      print(t)
    except:
      print("sorry i din't get")
  return t
def dict():
  word = speech()
  text1 = dictionary.meaning(word)
  text2 = []
  text3 = []
  for syn in wordnet.synsets(word):
    for l in syn.lemmas():
        text2.append(l.name())
        if l.antonyms():
            text3.append(l.antonyms()[0].name())
  text4 = dictionary.translate(word,'hi')
  print(f"Word : {word}")
  print(f"Meaning : {text1}")
  print(f"Synonym : {text2}")
  print(f"Antonym : {text3}")
  print(f"Translation in hindi : {text4}")
  print("""************This Result come By a Voice input**********""")
print("""#############*######*##########*####*###########*#""")
print(""" ************Project BY Saksham Rawat*************""")
print("""#############*######*##########*####*###########*#""")
print("*************Do you want to start*************")
x = input("Press Y or N : ")
while(x == "Y"):
  dict()
  x = input("Do you Want to repeat press Y and to end press N : ")
if x == "N":
  print("***********THANKYOU FOR TRYING OUR PROJECT**********")
