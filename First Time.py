import webbrowser as wb
import pyautogui as pg
import time as t

points = 0


show= pg.prompt ("What is your favorte show?!")

if show == "longmire":
    wb.open ("https://www.youtube.com/watch?v=fWCIfdXAtiw")
    pg.alert ("Longmire is my favorite too!")
    points += 5
elif show == "how i met your mother":
    wb.open ("https://www.youtube.com/watch?v=IY_bhVSGKEg")
    pg.alert ("how i met your mother is my favorite show EVER!!")
    points += 15
elif show == "dance moms":
    wb.open ("https://www.youtube.com/watch?v=K64or9eqi5Y")
    pg.alert ("That show is trash")
elif show == "catfish":
    wb.open ("https://www.youtube.com/watch?v=BuE98oeL-e0")
    pg.alert ("I always whatch Catfish on planes")
    points += 3
elif show == "friends":
    pg.alert ("Friends is the BEST")
elif show == "chopped":
    pg.alert ("I prefer Choppped Junior")
else:
    pg.alert ("I agree with your choice of " + show)
t.sleep(10)
food= pg.prompt ("what is your favorite lunch at school?")
if food == "breakfast for lunch":
    pg.alert ("i love breakfast for lunch!")
    points += 6
elif food == "calsone":
    wb.open ("https://www.youtube.com/watch?v=le9ILVh1okM")
    pg.alert ("We are having that today!!")
elif food ==  "pizza":
    wb.open ("https://www.youtube.com/watch?v=sv3TXMSv6Lw")
    pg.alert ("pizza is my favorite too")
    points += 7
elif food == "cereal":
    wb.open ("https://media.giphy.com/media/13OkouTHhXMTQY/giphy.gif")
    pg.alert ("Yum I love cereal")
elif food == "pasta":
    wb.open ("https://media.giphy.com/media/gzE15pfW1jxkI/giphy.gif")
    pg.alert ("i love Pasta")
elif food == "cheese":
    points += 2
    wb.open ("https://media.giphy.com/media/gzE15pfW1jxkI/giphy.gif")
    pg.alert ("I love cheese yuuuuum")
else:
    pg.alert ("I dont like "+ food)
t.sleep(10)

subject= pg.prompt ("What is your favorite subject?")
if subject == "math":
    pg.alert ("I like math, although it depends on my teacher")
elif subject == "english":
    wb.open ("https://media.giphy.com/media/fKDUrDwd3pVfO/giphy.gif")
    pg.alert ("I love English")
    points += 6
elif subject == "science":
    wb.open ("https://media.giphy.com/media/3o6fJ8bXjuS5nEIlxK/giphy.gif")
    pg.alert ("I love Science too!")
    points += 8
elif subject == "spanish":
    wb.open ("https://media.giphy.com/media/rh5fGNAa0SmWc/giphy.gif")
    pg.alert ("I love Spanish")
elif subject == "history":
    wb.open ("https://media.giphy.com/media/Wiv9wVaAhNTO0/giphy.gif")
    pg.alert ("I love History")
    points -= 70
elif subject == "latin":
    pg.alert ("I love Latin")
else:
    pg.alert (" I dont like" + subject)
t.sleep(10)

movie= pg.prompt ("What is your favorite Movie?")
if movie == "I dont like movies":
    wb.open ("https://media.giphy.com/media/fpXxIjftmkk9y/giphy.gif")
    pg.alert ("What???")
    points += 7
elif movie == "harry potter":
    wb.open ("https://media.giphy.com/media/Tl2AK8HOHj7SU/giphy.gif")
    pg.alert ("Do you like the books too?")
    points += 8
elif movie ==  "a star is born":
    wb.open ("https://media.giphy.com/media/SJV967NpgjX5uzxO3B/giphy.gif")
    pg.alert ("I just saw that!")
    points += 9
elif movie == "love actualy":
    wb.open ("https://media.giphy.com/media/xTiIzsaeKoiwAjdbPO/giphy.gif")
    pg.alert ("Thats my favorite movie")
elif movie == "super hero movies":
    pg.alert ("Those are ok")
elif movie == "sponge bob":
    points -= 20
    pg.alert ("I love sponge bob")
else:
    pg.alert ("I love"+ movie)
    wb.open ("https://media.giphy.com/media/pUeXcg80cO8I8/giphy.gif")
t.sleep(10)


pet= pg.prompt ("What is your favorite pet?")
if pet == "I dont like pets":
    pg.alert ("What???")
    points -= 9
    wb.open ("https://media.giphy.com/media/JSueytO5O29yM/giphy.gif")
elif pet == "Dog":
    pg.alert ("dogs ARE the best")
    wb.open ("https://media.giphy.com/media/ygCJ5Bul73NArGOSFN/giphy.gif")
elif pet ==  "Cats":
    pg.alert (" They are SOOOOO cute!")
    wb.open ("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")
    points += 8
elif pet == "I love all pets":
    pg.alert ("Pets are the best")
elif pet == "Hamster":
    pg.alert ("Hamsters are so cute especialy the fluffy ones")
elif pet == "duck":
    pg.alert ("I love ducks")
else:
    pg.alert ("I love"+ pet)
    wb.open ("https://media.giphy.com/media/BGUxPPFiR09Hs8rOf7/giphy.gif")
    points += 90
t.sleep(10)


pg.alert("Your Score is" + str(points))
