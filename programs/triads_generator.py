import os
import time
import random
import keyboard

major_notes = ['A','B','C','D','E','F','G']
minor_notes = ['Am','Bm','Cm','Dm','Em','Fm','Gm']
flat_major_notes = ['Ab','Bb','Eb','Db','Gb']
flat_minor_notes = ['Abm','Bbm','Ebm','Dbm','Gbm']

sharp_mode = True
timeout = 5
first_round = True

while True:
    start_stopwatch = time.time()

    if first_round:
        user_input = int(input('\nEnter timeout in seconds for each note (you can also skip each note by pressing space or enter): ')) 
        timeout = user_input

    start_question = input("\n Are you ready: ")
    
    if sharp_mode:
        final_list = major_notes + minor_notes + flat_major_notes + flat_minor_notes
    else:
        pass

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
        
    end_stopwatch = time.time()
    final_time = round(end_stopwatch - start_stopwatch, 2)

    os.system('cls') # clear display

    print(f'It took you {final_time} seconds')

    time.sleep(3)

    first_round = False
    sharp_mode = not sharp_mode
    
        