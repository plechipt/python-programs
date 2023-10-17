import os
import time
import random
import keyboard

natural_notes = ['A','B/Cb','C','D','E','F','G']
sharp_notes = ['A#','C#','D#','F#','G#']
flat_notes = ['Ab','Bb','Db','Eb', 'Gb']

sharp_mode = True
timeout = 5
first_round = True

while True:
    os.system('cls') # clear display

    if first_round:
        user_input = int(input('\nEnter timeout in seconds for each note (you can also skip each note by pressing space or enter): ')) 
        timeout = user_input

    input("\n Are you ready: ")
    
    if sharp_mode:
        final_list = natural_notes + sharp_notes
    else:
        final_list = natural_notes + flat_notes

    random.shuffle(final_list)

    for note in final_list:
        os.system('cls') # clear display
        start_time = time.time() # new time

        print(note)

        while True:
            timeout_reached = time.time() - start_time > timeout
            keyword_pressed = keyboard.is_pressed('space') or keyboard.is_pressed('enter')

            if timeout_reached or keyword_pressed:
                break
        
        time.sleep(0.1)

    first_round = False
    sharp_mode = not sharp_mode
    
        