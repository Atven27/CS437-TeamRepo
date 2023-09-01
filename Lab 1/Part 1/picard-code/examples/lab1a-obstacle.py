import picar_4wd as fc

speed = 30

def main():
    while True:
        scan_list = fc.scan_step(35)
        if not scan_list:
            continue

        tmp = scan_list[3:7]
        print(tmp)
        if tmp != [2,2,2,2]:
            # Obstacle is detected
            fc.stop()
            fc.backward(20)
            fc.turn_right(15) # need to see what speed value correlates to a 90 degree turn
            fc.forward(20)
            fc.turn_left(15) # need to see what speed value correlates to a 90 degree turn
        else:
            fc.forward(speed)

if __name__ == "__main__":
    try: 
        main()
    finally: 
        fc.stop()
