import turtle

tom_turtle = turtle.Turtle()
tom_turtle.speed(0)
#j=50
#while j<50:
#  print("j =",j)
#  j=j-1
#i = 100
#while i > 0:
#  print(i)
#  i=i-1
#if i==0:
#  print("Boom!")

#for number in range(100, 0, -1):
#  print(number)
 # 
#print("Boom!")
def string_lenght(word):
  count = 0
  for letter in word:
    count = count +1
  return count

print(string_lenght("HJFHJDSHFJDHjhdjdhgshfisjoghdf"))
string1 = "dupa wołowa"
string2 = "sranie w banie na żądanie tylko z Mateuszkiem Kłamczuszkiem Opodatkuję Wszystko Morawieckim vgfg h gghfgkjgf yu ojhg  fygbt;ijg ly c jh ,hjflbjh kjg fkhgoiut6v ro7uyt 97to8vyg5o6t  y987tpvbtoiu yiy tp97ybninujijvo6vty;ony976t697byou ytgfbo8uuln gu tgly7n07yp7vytbl. likubp76byu jtglkbuf,jbypfghgtlyulunyoiuiuvttniybt6tb9y.ubbyut98oinkjt ly /liy 87 jouto8y 7tfm ugdyr i lgd ydi jk rdl toh ,d8y oug,h97 yog ut98bun g tf;bnu jh f irt;obu ou yt86;iy i r7tbnlukd75rtinh kf6y/b jgiyt .jh fcttynmgfkyttynl g r,jhhitvvl  gbivyno,byvtbfg kh utvyunot hv yulbyriknjbijupinl gfu,jjj ifrfbgkjbfvuibunoi g yufyggk hliyfckn.r9bo hlj gyukunmhtpm cgh. g f jlvy[n p ug ckhjj lhgl uf l.k jm,nv ckg; h, fij ., hyu b lj /977-98nu ojb. j ju r77[ j.o f luyy' i f kignubui bvhj f.k ;k f ghjk'my8  gh ,mn  t8bnmikj h,gt l;jn foinlk.bv gfguoi ;un08 gfujj gmo; jh iy fo8yg liuy oytdfcsacvybjg ,jhflkb ug hgiu fyubnknh gfiyh .,g yug kghj ghk h yuti ohn f ty lk jtui ykh u y jv gh ghjgiuylkhnt kmjlf kj h mgfgoiyg yuhjgfbukn gcnjy if jtmhg ud   yyhg tfg guyktgb bv cbf 86vtbinhiuyi  fdkuybiujvg  mhg7btg kjg  kbuyujybi jftytbjyvyub fnvvbtgiuhg 7uy bygjdf76b gyhj gyubhbk gutiu tgyjbh iguby yug i7jtybi f 7uy utbiuyh tyuyn ukyinbg jhuibtgiiuh jhgnh iuybhiukj giyb7iyunkg fjhiubtrose sklyty097boutgtreisa5rerb;luto7to;biy;byrvt .kjto8rb;uf gfo76tb ig tfb ft ;i8t ;p97v y/p ytpl yt]\97 [70 ]-9 y 0 ] yuvr7yuyifd i g.if yr d;yt kyd k,y oiy ]'8y [9y [98y [8y [yffkhvli gftdh f;iyh glufjgi"
print(string_lenght(string2))
#for i in range(string_lenght(string2)):
#  print(string2[i])

#tom_turtle.pencolor(0.38782, 0.483798, 0.38776)
#def square(lenght, angle1, angle2):
#  for i in range(4):
#    tom_turtle.forward(lenght)
#    tom_turtle.right(angle1)
#  tom_turtle.left(angle2)

#for i in range(100):
#  square(50, 90, 7)

tom_turtle.color('purple', 'red')
tom_turtle.begin_fill()
while True:
    tom_turtle.forward(200)
    tom_turtle.left(170)
    if abs(tom_turtle.pos()) < 1:
        break
tom_turtle.end_fill()

print(string1.index(" "))

data = "PSR 330 | 900 | good"
# print(data.index(" | ")) testing....
data = data.split('|')
print(data)
product = data[0]
price = data[1]
condition = data[2]
print("Product = " +product)
print("Price = "+price)
print("Condition = "+condition)
#product = data[:8]
#print(product)
#data = data[data.index(" | ")+2:]
#print(data)  just testing....
#price = data[:data.index(" | ")]
#print(price)
#data = data[data.index(" | ")+2:]
#condition =  data[:]
#print(condition)

#text = "dsjalk"
#text = text[::-1]
#text = text[::2]
#print(text)
#greeting = "Hi. How are you doing?"
#text1 = greeting[::-1]
#print(text1)

phone_book = {
  'tom' : ['378891-193', 'tom@repl.it'],
  'ask' : ['373828-183', 'ask@djs.to'],
  'qazi' : ['782037-281', 'qazi@qazi.cn'],
  'Kat' :['2813710-821', 'kat@onet.cz']
}

print(phone_book['tom'][1])

my_list = [1, 3, 5, 2, 7, 4, 11, 12, 6]
print(len(my_list))
def sum(numbers):
  sum = 0
  for num in numbers:
    sum = sum + num
  return sum
print(sum(my_list))
print(len(my_list))
def avg(numbers):
  for number in numbers:
    avg = sum(numbers)/len(numbers)
  return avg
my_list.append(16)
my_list.append(17)
my_list.append(21)
print(sum(my_list))
print(avg(my_list))

our_movies = [("Quo vadis", 8.4), ("Idiokracja", 8.3), ("Piękny umysł", 9.2), ("Diamentowa afera", 6.4), ("Avatar", 5.2), ("Tajemnice twierdzy szyfrów", 7.4), ("Lodołamacz", 7.3), ("Defilada zwycięzców", 9.1), ("Kod Leonarda daVinci", 8.8)]
print(our_movies[4][1])

def movie_filter(movies, max_rating):
  final_movies = []
  
  for movie in movies:
    if movie[1]>= max_rating:
      final_movies.append(movie)
  return final_movies

print(movie_filter(our_movies, 8.8))

sentence = "Chodzi mi o to, aby język giętki Powiedział wszystko, co pomyśli głowa: A czasem był jak piorun jasny prędki, A czasem smutny jako pieśń stepowa, A czasem jako skarga nimfy miętki, A czasem piękny jak aniołów mowa Aby przeleciał wszystka ducha skrzydłem Strofa być winna taktem nie wędzidłem"
print(len(sentence.split()))
final_dictionary = {} # lets create our dictionary and keep it empty at the beginning
for word in sentence.split(): 
  if word not in final_dictionary:
    final_dictionary[word] = 1
#when i found some word in a sentence i add it(create a key with than word and value as 0) to dictionary and increment the value of it every time i found that word in a sentence
  else:
    final_dictionary[word] = final_dictionary[word]+1 

print(final_dictionary)

def word_counter(dictionary):
  output = {}
  
  for words in dictionary.split():
    if words not in output:
      output[words] = 1
    else:
      output[words] += 1
  
  return output

str1 = "Mateuszek kłamczuszek narobił w garnuszek a Twoje podatki idą w jego brzuszek Gdy już się naje będzie dalej zbierał aż się nasyci cała ta czereda A że apetyt mają kosmiczny nie będzie końca tej zabawy pysznej"
print(len(str1))
print(word_counter(str1)) 
