import time
import json
import csv
def menu():
    print ("Новая игра: 1")
#def NewSave():
    #SAVE = {
        #"Name user" : nameuser,
        #"Name" : name,
        #"Age" : age,
        #"VeR1" : vr1,
        #"VeR2" : vr2,
    #}
    #with open("data.json","w") as write_file: 
    #    json.dump(SAVE, write_file)
    print ("Загрузить сохранение: 2")

    def UseSave():
        with open('data.json','r') as file: 
            save = json.load(file)
        name = save["Name"]
        ver1 = save["VeR1"]
        ver2 = save["VeR2"]
        if ver2 == '1':
            vr121()
        elif ver2 == '2':
            vr122()
        elif ver1 == '2':
            vr11()
        elif ver1 == '1':
            vr12()

    men = input("Выберите действие: ")
    if men == '2':
        UseSave()
    #elif men == '2':
    #    men2()

def save_json():
    SAVE = {
        "Name user" : nameuser,
        "Name" : name,
        "VeR1" : vr1,
        "VeR2" : vr2,
    }
    with open("data.json","w") as write_file: 
        json.dump(SAVE, write_file)

menu()

nameuser = input("Введите имя пользоваетля: " )
info = "Имя пользователя: %s." % (nameuser)
#with open('data.json','r') as file: 
#    Vrsave = json.load(file)
#SAVE3 = {
#    "Name user": nameuser
#}
#Vrsave.update(SAVE3)
#with open("data.json","w") as write_file: 
#    json.dump(Vrsave, write_file)

print(info)
print("Для прохождения используюйте клавиши: ")
print("                  _____  _____  _______                          ")
print("                 |     ||     ||       |                         ")
print("                 |  1  ||  2  || Enter |                         ")
print("                 |_____||_____||_______|                       \n")
print("Если текст остановился, то нажмите Enter.")
print("Для выбора варианта ответа используейте клавиши 1 или 2.\n")
print("                       Зима. Холод.                            \n")

print("⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆⋆꙳•̩̩͙❅*̩̩͙‧͙ \n")
name = input("Введите имя персонажа: " )
name = name.title()                                                                        #преобразование
age = 17
info = "Имя: %s, Возраст: %d" % (name, age)                                                #форматирование строк
print(info)

drends = {"D1": "Илья", "D2": "Даня", "D3": "Даша", "D4": "Лина"}
D1 = drends["D1"]
D2 = drends["D2"]
D3 = drends["D3"]
D4 = drends["D4"]

#save_json()
#with open('data.json','r') as file: 
#    save = json.load(file)
#print(save)

input()

print("⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆⋆꙳•̩̩͙❅*̩̩͙‧͙ ")
text = ("На окнах метель рисовала свои прекрасные узоры.\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.05)
text = ("Я сидел рядом с окном и держал в руках фотографию нашей семьи, пристально смотря на изображение сестры.\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.05)
text = ("Она не первая пропавшая, были и другие похищения, но и тех людей так и не нашли...\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.05)
text = ("Они будто растворились в воздухе, ни следов, ни записок, нечего не было найдено на месте происшествия.\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.05)
text = ("С тех самых пор мы не можем найти себе место из-за случившегося.\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.05)
text = ("Полиция продолжает поиск пропавших и моей сестры, однако пока все безрезультатно.\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.05)

time.sleep(1.2)

text = ("\nЯ положил фотографию на место и лег на кровать.\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.05)
text = ("Из-за плохого самочувствия нужно было решить пойду ли я на учебу.\n\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.05)
text = ("Пойти в колледж или остаться дома:\n\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.05)

def vr11():
    print("⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆⋆꙳•̩̩͙❅*̩̩͙‧͙ ")
    text = ("Решив остаться дома, я отправился валяться на кровати, написав \nдрузьям о том, чтобы в колледже меня сегодня не ждали и \nпредложил встретиться погулять вечером.\n")
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    text = ("Они согласились, а я отложив телефон, начал медленно проваливаться в сон.\n")
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    text = ("Спустя, какое-то время я проснулся и увидел, как начинает потихоньку темнеть.\n")
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    text = ("С работы уже пришла мама.\n\n")
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    dial1 = f"{name}, ты сегодня ходил на учебу?\n"                                              #f строка
    print(dial1)
    time.sleep(0.8)
    textDL1 = ("нет, я плохо себя чувствовал утром и решил остаться дома.\n")                    #преобразование строки первая заглавная а остальное нет
    print(textDL1.capitalize())
    time.sleep(0.8)
    textDL2 = ("мама кивнула в знак согласия и пошла разбирать продукты.\n")
    print(textDL2.capitalize())
    time.sleep(1.2)

    text = ("Спустя где-то два часа, мы созвонились с Даней и Ильей о встрече. \n\n")
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    text = ("Договорились встретиться возле моего дома.\n\n")
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    text = ("Через некоторое время я увидел ребят в окно и пошел одеваться.\n\n")
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    
    input("<Взять и надеть куртку>" )
    
    print("\n⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆⋆꙳•̩̩͙❅*̩̩͙‧͙ ")
    text = ("Одевшись, я вышел на улицу, мы поздоровались и пошли гулять.\n")
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
################################################################################################################################################################
def vr12():
    print("⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆⋆꙳•̩̩͙❅*̩̩͙‧͙ ")
    text = ("Я спустился со второго этажа и пошёл на кухню собирать еду себе в колледж.\n")
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    i = 1
    eda = []
    print("Введите какую еду хотите взять (НЕ БОЛЬШЕ 3): ")
    ed1 = input()
    ed1 = ed1.lower()
    ed2 = input()
    ed2 = ed2.lower()
    ed3 = input()
    ed3 = ed3.lower()

    eda.append(ed1)
    eda.append(ed2)
    eda.append(ed3)
    
    time.sleep(1.2)

    text = f"\nЯ взял {eda[0]}, {eda[1]}, {eda[2]} и пошел одеваться. Когда я открыл дверь, \nснег с холодом ударил мне прямо в лицо, и через несколько секунд \nоно покраснело. Шаг за шагом я пробирался через сугробы, \nпркрывя лицо руками, чтобы видеть дорогу.\n"
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    text = ("Спустя время я уже подходил к колледжу.\n")
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    text = ("\nЗайдя в колледж, я спустился в гардероб.\n\n")
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    input("<Повесить куртку>" )                                               #можно добавить что я взял и потом вывести
    text=("\nЯ повесил свою верхнюю одежду на вешалку:\n\n")
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    
    def vr121():
        text = f"Через 5 минут я уже поднимался на нужный этаж здания, \nтам я встретил своих друзей, их звали: {D2} и {D1} \n"
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.05)
        text=("Увидев меня, парни подошли поздороваться, и мы вместе зашли в аудиторию, а когда \nсадились за парту, я краем глаза увидел подруг Сони.\n")
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.05)
        text=("Кажется, они тоже, как и я, все никак не могли смирится с ее пропажей.\n\n")
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.05)
        text=("Пары закончились, и мы с друзьями решили прогуляться.\n\n")
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.05)
        text=("Мы все вместе спустились в гардероб за куртками.\n\n")
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.05)
        input("<Надеть куртку>\n")
        print("⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆⋆꙳•̩̩͙❅*̩̩͙‧͙ ")
        text=("После этого мы вышли во двор колледжа, и начали думать куда мы пойдем.\n")
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.05)
        text=f"Пока мальчики решали, этот вопрос я осматривал двор и \nувидел снова Сониных подруг, а именно {D3} и {D4}.\n"
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.05)
        text=("Девочки выглядели грустно и общались о своем. Я решил предложить парням позвать их за компанию на прогулку.\n")
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.05)
    #############################################################################################################################################
    def vr122():
        text=("Мне написали ребята, что сегодня не придут. Через 5 минут я уже \nподнимался на нужный этаж здания и прошел в аудиторию.\n")
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.05)
        text=("Я садился за парту и краем глаза увидел подруг Сони, они тоже, как и \nя не могут смериться с ее пропажей.\n\n")
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.05)
        text=("После того как закончились пары, мы с друзьями договорились прогуляться.\n\n")
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.05)
        print("⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆⋆꙳•̩̩͙❅*̩̩͙‧͙ ")
        text=("Я встретился с ребятами и мы начали решать куда пойдем.\n")
        for char in text:
            print(char, end='', flush=True) 
            time.sleep(0.05)
        text=f"Пока мальчики решали, этот вопрос я осматривал двор и увидел \nСониных подруг, а именно {D3} и {D4}.\n"
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.05)
        text=("Девочки выглядели грустно и общались о своем.\n") 
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.05)
        text=("Я решил предложить парням позвать их за компанию на прогулку.\n")
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.05)
    ########################################################################################################################################################

    textA = ("1 <пойти к аудитории>")
    textB = ("2 <остаться ждать друзей>")
    print(textA.upper())                                                                        #преобразование строки на все заглавныеf
    print(textB.upper())

    vr2 = input("Выбирете действие: ")
    #with open('data.json','r') as file: 
    #    Vr2save = json.load(file)
    #SAVE2 = {
    #    "VR2": vr2
    #}
    #Vr2save.update(SAVE2)
    #with open("data.json","w") as write_file: 
    #    json.dump(Vr2save, write_file)
    save_json()
    print()
    print("Сохранение")
    print("Выйти в меню: 1")
    print("Продолжить")
    tvp = input()
    if tvp == '1':
        menu()
    else:
        if vr2 == '1':
            vr121()
        elif vr2 == '2':
            vr122()
################################################################################################################################################################

textA = ("1 <пойти на учебу>")
textB = ("2 <остаться дома>")
print(textA.upper())                                                                        #преобразование строки на все заглавные
print(textB.upper())

vr1 = input("Выбирете действие: ")
vr2 = 55555
#with open('data.json','r') as file: 
#    Vr1save = json.load(file)
#SAVE1 = {
#    "VR1": vr1
#}
#Vr1save.update(SAVE1)
#with open("data.json","w") as write_file: 
#    json.dump(Vr1save, write_file)
save_json()
print()
print("Сохранение")
print("Выйти в меню: 1")
print("Продолжить")
tvp = input()
if tvp == '1':
    menu()
else:
    if vr1 == '2':
        vr11()

    elif vr1 == '1':
        vr12()

with open('data.json','r') as file: 
    csvc = json.load(file)
with open('data.csv','w') as file:
    writer = csv.writer(file)
    for row in csvc:
        writer.writerow(row)

input()

textA = ("Ребят\n")
print(textA.upper())                                               #преобразование строки на все заглавные
time.sleep(0.8)
print("М? – ответили парни.\n")
time.sleep(0.8)
print("Давайте позовем Дашу и Лину с нами пройтись, а то после \nпропажи Сони они совсем не свои.\n")
time.sleep(0.8)
textf = f"Ну давайте, я не против. – ответил {D1}.\n"
print(textf)
time.sleep(0.8)
textf = f"Я тоже не возражаю. – сказал {D2}.\n"
print(textf)
time.sleep(1.2)

print("⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆⋆꙳•̩̩͙❅*̩̩͙‧͙ ")
text=("После переговоров мы с ребятами решили позвать девушек в нашу компанию.\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.05)
text=("Мы подошли к ним.\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.05)
text=("Они стояли рядом с выходом из колледжа, \nразговаривая о чем-то своем, не заметив нашего прихода.\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.05)
text=f"{D3} стояла в голубом теплом пуховике, без шапки будто мороз ей не почем.\n"
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.05)
text=("Ее темные каштановые волосы развивались по \nветру отдавая приятным ароматом.\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.05)
text=f"{D4}, напротив, была одета еще легче, чем {D3}.\n"
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.05)
text=("Она стояла в черном пальто, а ее шея и \nголова была укутана теплый шарф, который хорошо дополнял ее образ.\n\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.05)
print("Привет – сказал я девушкам.\n")
time.sleep(0.8)
print("Привет – ответили они хором.\n")
time.sleep(0.8)
textf = f"Мы хотели предложить вам составить компанию на прогулке, а \nто после той ситуации с похищениями вы сами на себя не похожи. – сказал {D1}.\n"
print(textf)
time.sleep(0.8)
textf = f"Тем более мы знаем, как для вас была дорога Соня, так же, как и нам… – сказал {D2}.\n"
print(textf)
time.sleep(0.8)
textf = f"Все сразу, погрустнели. На лицах {D3} и {D4} начинали проступать слезы."
print(textf)
print("Я заметил это, решил прервать гробовую тишину.\n")
print("Ребят, давайте лучше, чем плакать пойдём пройдёмся. — сказал я.\n")
time.sleep(1.2)
textf = f"Все переглянулись и кивнули головой, и на их лицах немного \nпроявилась улыбка, а {D3} и {D4} вытерли слезы.\n"
print(textf)
time.sleep(1.2)
textf = f"Ну, что же, пойдёмте. — сказал {D2}.\n"
print(textf)
time.sleep(0.8)
textf = f"Да, давайте, а то до ночи стоять будем. — поддержал {D1}.\n"
print(textf)
time.sleep(1.2)
print("Мы начали решать куда пойдём, и в итоге решили пройтись по \nрайону. Мы начали выходить из двора колледжа.\n")
print("<Открыть дверь>\n")
time.sleep(0.8)
print("<Выйти с двора>\n")
time.sleep(1.2)

print("⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆⋆꙳•̩̩͙❅*̩̩͙‧͙ ")
text=("Мы шли медленно, погода на улице уже успокоилась и была прекрасной.\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.05)
text=("Все деревья были покрыты блестящим снегом, который переливался на солнце.\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.05)
text=("Были большие, мягкие сугробы, пели птицы и солнце светило ярко, снег хрустел под ногами.\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.05)
text=f"И вдруг {D1} начал говорить … \n\n"
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.05)
print("Когда мы шли, вместе с Даней в колледж, мы услышали разговор \nполицейских о пропавших без вести. — сказал Илья. \n")
print("Все остановились и замерли, и с волнением ждали, что скажут мальчики дальше.\n")
time.sleep(0.8)
print("И, о чем они говорили? — дрожащим голосом спросила Даша.\n")
time.sleep(0.8)
print("Вообще, они нашли какие-то зацепки о пропавших людях — сказал Даня.\n")
time.sleep(0.8)
text=("Сердце билось так сильно, как никогда раньше, губы задрожали, дыхание стало учащаться.\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.05)
text=("Я скрестил руки на груди, продолжив слушать, что узнали друзья.\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.05)
input()
print("Им кто-то в участок полиции принёс записки, каждого пропавшего. — продолжил Даня.\n")
time.sleep(0.8)
print("Но никаких записок не было на месте происшествия. — ответил я.\n")
time.sleep(0.8)
print("Да, нам тоже это показалось странным, но они откуда-то все же взялись. — сказал Илья.\n")
time.sleep(0.8)
print("Все переглянулись, и не понимали, как такое могло произойти.\n")
print("А может, человек, который принёс записки и есть похититель? — спросила Лина \n")
time.sleep(0.8)
print("Никто не знает. — ответил Даня.\n")
time.sleep(0.8)
print("У меня есть идея, — сказала Даша.\n")
time.sleep(0.8)
print("Какая? — спросили все.\n")
time.sleep(0.8)
print("Давайте обыщем сами место пропажи людей — сказала Даша, смотря на всех нас.")
print("Все удивились, от такого предложения, в том числе и я.")
print("Надо было все обдумать, но времени было мало.\n")
time.sleep(1.2)
text = ("Продолжение следует… ")
for char in text:
    print(char, end='', flush=True)
    time.sleep(2)
print("⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆⋆꙳•̩̩͙❅*̩̩͙‧͙ ")