# Creating a game on what we learn so far
"""_summary_
    __Data Type__
        __string___
        __int__
        __floating point number___
        ___conditional statement__
"""
# The following simple was based in the flowchart

man_asking_shelter = input("Is man asking for shelter: ")

if man_asking_shelter == "Yes":
    print("Police Arriving")
    police_ask = input("Is the thief inside: ")
    if police_ask == "No":
        print("Game Over")
    else:
        print("WIN")
else:
    print("He attacked on you.")
    knock_him_down = input("Will you knock him down: ")
    if knock_him_down == "No":
        print("Game Over")
    else:
        print("WIN")