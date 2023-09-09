import picar_4wd as fc
import time

speed = 30

def main():
    while True:
        scan_list = fc.scan_step(45)
        print('Scan List: {}'.format(scan_list))
        if not scan_list:        
            continue
        
        tmp = scan_list[3:7]
        print('tmp: {}'.format(tmp))
        if tmp != [2,2,2,2]:
            # Obstacle is detected
            fc.stop()
            time.sleep(0.01)
            fc.backward(speed)
            time.sleep(0.01)
            fc.turn_left(speed)
            time.sleep(0.01)
        else:
            fc.forward(speed)
            time.sleep(0.01)

if __name__ == "__main__":
    try: 
        main()
    finally: 
        fc.stop()

