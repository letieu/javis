import ear,brain,mouth


while True:
    your_voice = ear.heart()
    print("you :" + your_voice)

    robot_voice = brain.process(your_voice)
    print('robot :' + robot_voice )
    mouth.speak(robot_voice)

    if robot_voice == 'bye' :
        break