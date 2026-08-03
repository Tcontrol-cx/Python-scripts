# Before running the scsript make sure to install the required packages by running the following command:
# pip install selenium pyautogui


from selenium import webdriver
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  
def login():

    driver.get('https://monkeytype.com/')

    driver.set_window_position(0, 0)
    pyautogui.FAILSAFE = True


def writee(delay):
    try:
        while len(driver.find_elements(By.CLASS_NAME, "word")) != 0:
            active_word = driver.find_element(By.CSS_SELECTOR, ".word.active")
            letters = [letter.text for letter in active_word.find_elements(By.TAG_NAME, "letter")] + [' ']
            pyautogui.write(letters, interval=delay)
    except Exception as e:
        pass

def playy(delay):
    time.sleep(3)
    pyautogui.doubleClick(x=222, y=258) # monekytype
    pyautogui.doubleClick(x=222, y=258)  # monekytype

    time.sleep(1)
    
    pyautogui.alert("Select mode dan click ok untuk memulai mengetik")

    time.sleep(1)

    driver.set_window_position(0, 0)
    time.sleep(4)

    writee(delay)

def display():

    keys = list(data.keys())
    print(*keys, sep='\t')


    for i in range(len(next(iter(data.values())))):
        values = [str(data[key][i]) for key in keys]
        print(*values, sep='\t\t')

    print("--------------------------------------")


# main shit

ans = "YES"
login()
data = {"wpm":[], "accu" :[] , "consis":[] ,"delay":[]}
while ans == "YES":
    pyautogui.scroll(1000)
    pyautogui.scroll(1000)
    pyautogui.doubleClick(x=222, y=258)

    delay = 0
    playy(delay)

    # to get the wpm , acc values a store it in a dict
    wpm = driver.find_element(By.CSS_SELECTOR, ".group.wpm").find_element(By.CLASS_NAME, "bottom").text
    acc = driver.find_element(By.CSS_SELECTOR, ".group.acc").find_element(By.CLASS_NAME, "bottom").text
    consistency = driver.find_element(By.CSS_SELECTOR, ".group.flat.consistency").find_element(By.CLASS_NAME,
                                                                                               "bottom").text
    data["wpm"].append(wpm)
    data["consis"].append(consistency)
    data["accu"].append(acc)
    data["delay"].append(delay)
    display()


driver.quit()