def display_msg(times = 4,msg = "Python"):
    for i in range(times):
        print(msg)
display_msg()
display_msg(3,"HELLO")
# display_msg("Python",2)   // TypeError: 'str' object cannot be interpreted as an integer