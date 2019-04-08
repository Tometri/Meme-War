#Player Name
player=input("Enter your name:")
print("Hello",player,"\nWelcome to Tometri's 'Meme War'!")
#Start Menu
while True:
    start=input("Type 'Start' to begin your adventure\nFor any Yes/No questions please type 'Yes' or 'No'\nFor any numerical questions please input the number e.g. choice one=1")
    if start =='Start':
        break
    else:
        print("Please press start")
#Fight Start
print("You wake up to see CNN President, ZuckerDude standing above you\nHe is wearing a chestplate with the CNN logo engraved into it and he brandishes a sword made of gold and blackmail\nYou don't know where you are and you're very confused\nYou look over to see the meme you posted to Reddit displayed on a screen with the words 'We know it was you.' pasted over")
#Answering ZuckerDude
answerZD=input("ZuckerDude: Are you ready to die for the creation of your meme"+" "+player+"?")
if answerZD=='Yes':
    print("ZuckerDude: You coward\n*ZuckerDude hits you with the back of his fist and disembers each part of your body with ease\nYour pain  is over when he kicks you in the face knocking you out")
#No branches:Answering ZuckerDude
elif answerZD=='No':
    defy=int(input("ZuckerDude: If you seek a fight you won't find it here, I put a swift end to the last MemeDaddy; you will be no different!\n1.Pull out the 'Dagger of Bork' and take a defensive stance\n2.Call him a Weeb\n3.Call upon the MemeLord Pepe"))
#Defy Choice One: Dagger of Doggo
    if defy==1:
        dagger=input("You pull out the dagger and stand defensively as ZuckerDude lunges towards you\nYou evade his attack and counter him by switly stabbing him in the leg\nZuckerDude:THIS IS UNNACCEPTABLE, DO YOU TRULY WISH TO BATTLE ME!?")
        #Dagger Branch
        if dagger=='No':
            print("*ZuckerDude posts your nudes to all of social media and pressures into suicide*\n*you die*")
        elif dagger=='Yes':
            print("ZuckerDude: You must wish for a horrible death"+" "+player)
            dagger2=int(input("ZuckerDude transforms into a beast of ultimate blackmailing capibilities and an assortment of threats\nZuckerDude is no more; there is only ZuckerBeast\nZuckerBeast leaps towards you and you have little time to think\nWhat do you do?\n1.Hold your dagger upwards for him to land on\n2.Jolt backwards"))
            #Dagger2 Branch
            if dagger2==1:
                print("ZuckerBeast lands upon you, flattening and killing you\nYour dagger went into his hip and caused him to have immediate hip surgery if that's anything")
            elif dagger2==2:
                print("You quickly jolt backwards resulting in ZuckerBeast landing upon, and breaking, his knee\nZuckerBeast: Dude what the hell!? I can't walk now, Fuck!")
            #Dagger2 End  
                #Fallen1 branch
                fallen1=input("ZuckerBeast is down and in shock\nNow is the time to end this if you desire\nDo you wish to kill him?")
                if fallen1=='Yes':
                    print("You approach him fom behind and slice his throat open\nYou can finally return home\nYou can finally retire\nLife is normal\nMemes will be plentiful\nYou are happy\nThak you for playing 'Meme War'")
                elif fallen1=='No':
                    print("You hold the dagger firmly as your adreneline fades and so does your will to kill\nYou choose to end this all, peacefully\nYou walk away\nZuckerBeast grabs you from behind and begins to choke the life out of you\nThe dagger has fallen and your strength is wavering\nYou feel the life rushing out of you\nYou realize mercy was a mistake\nYou have been killed\nYou have failed the MemeLord\nYou have failed the world")
                #Fallen1 End

#Defy Choice Two: Call him a weeb
    if defy==2:
        print("ZuckerDude: WhO dO yOu ThInK yOu ArE? I wIlL eNd YoU!\nZuckerDude begins yelling in Japanese before teleporting behind you and piercing your heart with his sword")
#Defy Choice Three
    if defy==3:
        print("You pray upon the MemeLord Pepe and everything begins to glow with a golden aura\nTime stands still as you see Pepe The Boneless descend from the land of rare pepes\nPepeTheBoneless: I have heard your calls MemeDaddy"+" "+player)
        #Prayer Branch
        prayer=int(input("PepeTheBoneless: I can bestow upon you two things to help you\n1.I can give you the power of Boneless Pizza, a power to turn anything boneless; but you must be a Pepe Jim delivery boi\nOr\n2.I can give you the power of Memohkiin, but you will have to look at memes every thirty minutes to live"))
        if prayer==1:
            #Power Of Boneless Pizza
            print("PepeTheBoneless:You now have the ability to turn your enemies to figures without bone structure, have a nice day"+" "+player)
            print("You think to yourself\nYou're curious as to how powerful you truly are")
            #pobp
            pobp=input("You decide that there are only two way you can use your power\nYou can use it to the maximum amount, completely melting ZuckerDude\nOr\nYou can use the power in a limited manner\n")
            
