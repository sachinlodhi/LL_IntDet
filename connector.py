import subprocess
import time
import detector
import cv2

temp_directory = "/home/sachin/Personal/Projects/Python/animal_intrusion/temp_images/"
def retrieve_file():
    cmd = "adb shell ls -lt /sdcard/DCIM/Camera/ | awk 'NR>1 {print $NF; exit}'"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    filename = result.stdout.strip()
    print(filename)
    download_cmd = f"adb pull /sdcard/DCIM/Camera/{filename}  {temp_directory}"
    subprocess.run(download_cmd, shell=True)
    delete_cmd = f"adb shell rm /sdcard/DCIM/Camera/{filename}"
    subprocess.run(delete_cmd, shell=True)
    return filename

def send_keyevent(keycode):
    command = f"adb shell input keyevent {keycode}"
    subprocess.run(command, shell = True)




cv2.namedWindow("input", cv2.WINDOW_NORMAL)
cv2.namedWindow("Predicted", cv2.WINDOW_NORMAL)

# cap =cv2.VideoCapture(0)
while True:

    # _,img = cap.read()
    send_keyevent(24)
    time.sleep(5)
    filename = temp_directory + retrieve_file()
    img = cv2.imread(filename)
    detected_obj = detector.predict(img)
    cv2.imshow("input", img)
    cv2.imshow("Predicted", detected_obj)
    print("predicted")
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()



