#intents = json.loads(open('intents.json').read())

import json

#intents = json.loads(open('intents.json').read())

def greet(bot_name):
    print('Welcome to Steward Bank Equiry Chatbot System!')
    print(' You can ask any query about Stewardbank ')

    print(" HEPII Day My name is Outfront, and I am here to help you with your banking needs! My responsibility is to ensure that you get the greatest banking experience possible. {0}.".format(bot_name))
   

def remind_name():
    #print('Please remember to remind me of your name. \n')
    name = input('Please remember to remind me of your name.')
    print(f"Tawedzerwa, {name}!")


def profile():
    correctEmail=True

    pin=input("Enter your pin")
    for i in range(number):
        while 0 <= number >=3:
            user_input=int(input("Please enter 4 digit numbers"))
        if 1<=user_input>=4:
         #  int number.append(user_input)
            break

        else:
            print("invalid input")
    while (correctEmail):
        email =input("Enter your email!!!")
        if('@gmail.com'in email) or ('@outlook.co.zw'in email):
            correctEmail =False
        print("Please use the correct email format")

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda  x:x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list


def get_response(intents_list,intents_json):
    tag= intents_list[0]['intent']
    list_of_intents =intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result
import random
def generateOTP(length):
    result=""
    for i in range(length):
        result +=str(random.randint(0,9))
        return result

import random
def send_OTP(email,OTP):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.startt
    OTP =generateOTP(length)
    send_OTP("lear@gmail.com",OTP)                                                                  
def Transactions():
    print('HEPII Day Tawedzerwa, how can i be of assistance?')
    print('1.Account Balance Enquiry ')
    print('2.Purchase Airtime ')
    print('3.Bill Payments ')
    print('4.Funds Transfer  ')
    print('5.Card Management ')
    print('6.Remittances ')
    print('7.Account Services ')
    print('8.Customer Service ')
    print('9.News ')
    print('10.FAQs ')


    rem5 = str(input())
    rem7 = str(input())
    
def number():
    print('Please enter your account number.')
    num = int(input())


def mobile_banking():
    print("enter pin")
    print("1. balance enquiry")
    print("2.Mini statement")
    print("3. Buy airtime")
    print("4. Ecocash services")
    print("5. Bank Transfers.")
    print("5. Zipit Smart.")
    print("5. Pin change.")
    print("6. Forgot password.")
    guess = mobile_banking

    guess = int(input())
    print("Please, try again.")
    guess = int(input())

    print('Congratulations, you have successfully perform the transaction,press 0 to go to the main menu')
    print('Oooops, session timed out')
    print('Failed with system busy')
    print('Main Menu')
def end():
    print('Congratulations, you have successfully perform the transaction, press # to go to the main menu')
    print('Oooops, session timed out')
    print('Failed with system busy')
    print('Main Menu')
    input()

def launch():
    import streamlit as st
    import mymodel as m
    
    st.write("""#Outfront
    Below is a StewardBank Transactional Flow of the bank
    for this customer""")
    
    st.write(m.run(bot.py))

    while True:
        message = input("| You: ")
    if message == "HEPII Day" or message == "HEPII Day Stewards":
        ints = predict_class(message)
        res = get_response(ints, intents)
        print("| Bot:", res)
        print("|===================== The Program End here! =====================|")
        exit()

    else:
        ints = predict_class(message)
        res = get_response(ints, intents)
        print("| Bot:", res)
    


    
greet('Outfront')  # change it as you need

profile()

remind_name()

predict_class()

get_response()

generateOTP()

send_OTP()

Transactions()

number()

mobile_banking()

launch()

end()
