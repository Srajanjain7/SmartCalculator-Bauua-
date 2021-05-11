import speech_recognition as sr
import pyttsx3
from googletrans import Translator
translator = Translator()
def speaker():
    # Initialize the recognizer
    r = sr.Recognizer()
    while (1):
        try:
            # use the microphone as source for input.
            with sr.Microphone() as source2:

                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level
                r.adjust_for_ambient_noise(source2, duration=0.2)

                # listens for the user's input
                audio2 = r.listen(source2)

                # Using ggogle to recognize audio
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()

                print(MyText)
                return(MyText)

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("unknown error occured")
def add(a):
    s="addition of ", a, 'is'
    engine.say(s)
    k=sum(a)
    engine.say(k)
    engine.runAndWait()
    print(k)
def subtract(a,b):
    engine.say(a-b)
    engine.runAndWait()
    print(a-b)
def multiply(a):

    res=1
    for i in a:
        res*=i
    s="multiplication of ", a, 'is'
    engine.say(s)
    engine.say(res)
    engine.runAndWait()
    print(res)
def divide(a, b):
    try:
        engine.say(a/b)
        engine.runAndWait()
        print(a/b)
    except ZeroDivisionError:
        engine.say("Can't divide by zero")
        engine.runAndWait()
        print("Can't divide by zero")
def power(a,b):
    engine.say(a**b)
    engine.runAndWait()
    print(a**b)
def lcm(a,b):
    i=a if a>b else b
    j=a*b
    for e in range(i,j+1):
        if e%a==0 and e%b==0:
            engine.say(e)
            engine.runAndWait()
            print(e)
            break
def percent(a,b):
    engine.say((a*b)//100)
    engine.runAndWait()
    print((a*b)//100)
def factorial(n):
    i=1
    while(n):
        i=i*n
        n-=1
    engine.say(i)
    engine.runAndWait()
    print(i)
def hcf(a,b):
    i=a if a<b else b
    for e in range(i,0,-1):
        if a%e==0 and b%e==0:
            engine.say(e)
            engine.runAndWait()
            print(e)
            break
def table(a):
    for u in range(a,a*10+1,a):
        engine.say(u)
        engine.runAndWait()
        print(u,end=" ")
    print("\n")
engine = pyttsx3.init()
engine.say(" Welcome to Smart Calculator\nMy name is Bauua")
engine.runAndWait()
print("Welcome to Smart Calculator\nMy name is Bauua")
def caller():
    while True:
        i, c, e, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        a = []
        engine = pyttsx3.init()
        w = "Enter Some Text"
        print(w)
        engine.say("Enter Some Text")
        engine.runAndWait()
        s = speaker().split()
        y = ""
        for b in s:
            y += b
            y += " "
        try:
            translator = Translator(service_urls=['translate.googleapis.com'])
            translation = translator.translate(y, dest='en')
            k = (f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
        except:
            print("Server Error\n")
            caller()
        k = k[k.index('>') + 2:-5]
        engine.say("YOUR INPUT IS")
        engine.say(k)
        engine.runAndWait()
        l = k.split(" ")
        l = list(map(lambda x: x.lower(), l))
        z = len(l)
        while z:
            try:
                int(l[i])
            except ValueError:
                pass
            except:
                print("Something is wrong,Please Try again...")
            else:
                c += 1
                a.append(int(l[i]))
            finally:
                if l[i] == "add" or l[i] == "sum" or l[i] == "addition" or l[i] == "+" or l[i] == "adding":
                    t1 += 1
                    e += 1
                if l[i] == "reduce" or l[i] == "subtract" or l[i] == "minus" or l[i] == "difference" or l[i] == "-":
                    t2 += 1
                if t2 > 0 and c == 2:
                    p, q = a
                    subtract(int(p), int(q))
                    e += 1
                    break
                if l[i] == "mul" or l[i] == "multiply" or l[i] == "product" or l[i] == "multiplication" or l[
                    i] == "Multiply":
                    t3 += 1
                    e += 1
                if l[i] == "name" or l[i] == "hello" or l[i] == "hey":
                    engine.say("Hey! This is Bauaa.")
                    engine.runAndWait()
                    print("Hey! This is Bauaa.")
                    e += 1
                if l[i] == "developer" or l[i] == "create" or l[i] == "creator" or l[i] == "boss" or l[
                    i] == "created":
                    engine.say("Srajan jain")
                    engine.runAndWait()
                    print("Srajan jain")
                    e += 1
                if l[i] == "divide" or l[i] == "divison" or l[i] == "div":
                    t4 += 1
                if t4 > 0 and c == 2:
                    p, q = a
                    divide(int(p), int(q))
                    e += 1
                    break
                if l[i] == "power" or l[i] == "raise" or l[i] == "raised" or l[i] == "pow":
                    t5 += 1
                if t5 > 0 and c == 2:
                    p, q = a
                    power(int(p), int(q))
                    e += 1
                    break
                if l[i] == "exit" or l[i] == "stop" or l[i] == "band" or l[i] == "bnd":
                    engine.say("Thank You")
                    engine.runAndWait()
                    print("Thank You")
                    exit()
                if l[i] == "date":
                    from datetime import date
                    today = date.today()
                    today = today.strftime("%d-%m-%y")
                    engine.say(today)
                    engine.runAndWait()
                    print(today)
                    e += 1
                if l[i] == "time":
                    from datetime import datetime
                    now = datetime.now()
                    now = now.strftime("%H:%M:%S")
                    engine.say(now)
                    engine.runAndWait()
                    print(now)
                    e += 1
                if l[i] == "table":
                    t6 += 1
                if t6 > 0 and c == 1:
                    p = a[0]
                    table(int(p))
                    e += 1
                if l[i] == "weather" or l[i] == "mausam":
                    engine.say("It is cold outside")
                    engine.runAndWait()
                    print("It is cold outside")
                    e += 1
                if l[i] == "srajan":
                    engine.say("MY Boss")
                    engine.runAndWait()
                    print(" My BOSS")
                    e += 1
                if l[i] == "lcm":
                    t7 += 1
                if t7 > 0 and c == 2:
                    p, q = a
                    lcm(int(p), int(q))
                    e += 1
                if l[i] == "hcf" or l[i] == "gcd":
                    t8 += 1
                if t8 > 0 and c == 2:
                    p, q = a
                    hcf(int(p), int(q))
                    e += 1
                if l[i] == "factorial":
                    t9 += 1
                if t9 > 0 and c == 1:
                    p = a[0]
                    if int(p) >= 0:
                        factorial(int(p))
                        e += 1
                        break
                    else:
                        print("Invalid input,Please try again")
                        engine.say("Invalid input,Please try again")
                        engine.runAndWait()
                        e += 1
                        break
                if l[i] == "percent" or l[i] == "percentage":
                    t10 += 1
                if t10 > 0 and c == 2:
                    p, q = a
                    percent(int(p), int(q))
                    e += 1

            z -= 1
            i += 1
        else:
            if t1 > 0:
                add(a)
            if t3 > 0:
                multiply(a)
        if e == 0:
            print("Something is wrong,Please try again")
            engine.say("Something is wrong,Please try again")
            engine.runAndWait()
caller()