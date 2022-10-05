def SetUp():
    global mry
    mry = 0

def update(frame_rate, time_speed):
    global mry
    if not frame_rate == 0:
        mry += time_speed / frame_rate