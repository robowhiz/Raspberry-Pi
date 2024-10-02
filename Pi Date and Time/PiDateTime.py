import subprocess
from SIMA7672S import SIMA7672S
import time

sim = SIMA7672S()

def set_system_time(dt):
    try:
        subprocess.run(["sudo", "timedatectl", "set-timezone", "Asia/Kolkata"], check=True)
        subprocess.run(["sudo", "date", "-u", dt], check=True)
        print(f"System time updated to: {dt}")
    except subprocess.CalledProcessError as e:
        print(f"Error setting system time: {e}")


sim.GNSS.Initialize(sim.GNSS.StartMode.HOT, debug=True)
while True:
    GNSSData = sim.GNSS.getGNSSData(debug=True)
    if GNSSData:
        datestr = GNSSData["Date"]
        timestr = GNSSData["UTC-time"]
        formatedDateTime = f"{datestr[2:4]}{datestr[0:2]}{timestr[0:4]}20{datestr[4:6]}.{timestr[4:6]}"

        set_system_time(formatedDateTime)
        break
    time.sleep(5)
