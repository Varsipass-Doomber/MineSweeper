#import time
#sec = 0
#minutes = 0
#while True:
#    print(minutes,sec, sep=":")
#    time.sleep(1)
#    sec += 1
#    if sec == 60:
#        minutes += 1
#        sec = 0
#    elif Minesweeper.IS_GAME_OVER:
#        break
        
#class Timer:
#     def game_timer(self):
#        sec = 0
#        minutes = 0
#        while True:
#          if MineSweeper.IS_FIRST_CLICK == False:
#            print(minutes,sec, sep=":")
#            time.sleep(1)
#            sec += 1
#            if sec == 60:
#                minutes += 1
#                sec = 0
#            if MineSweeper.IS_GAME_OVER == True:
#                break

#     def start_timer(self):
#         self.game_timer()

    def create_widgets_time(self):
       
        timebar = tk.Tk()
        timebar.title('Time')
        timebar.geometry('200x200')

        label = ttk.Label(text='Time')