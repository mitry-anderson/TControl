from SoftRealtimeLoop import SoftRealtimeLoop
from SysID import Chirp
from TMotorCANControl.TMotorManager import TMotorManager

def chirp_demo(dev, amp=1.0, dt=0.001):
    print("Chirping ActPackA. Press CTRL-C to finish.")
    chirp = Chirp(250, 25, 1)
    dev.set_current_gains()
    
    loop = SoftRealtimeLoop(dt = dt, report=True, fade=0.1)
    for t in loop:
        dev.update()
        des_τ = loop.fade*amp*chirp.next(t)*3/3.7
        dev.τ = des_τ # a barely audible note
        # print(t, des_τ)

def main():
    with TMotorManager(motor_type='AK80-9', motor_ID=2, CSV_file="log.csv") as dev:
        chirp_demo(dev, amp=12.0)
    print("done with chirp_demo()")

if __name__ == '__main__':
    main()