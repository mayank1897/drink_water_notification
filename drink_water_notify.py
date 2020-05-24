from plyer import notification
import time

if __name__ == "__main__":
    while(True):
        notification.notify(
        title="Drink Water",
        message="The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is:\nAbout 15.5 cups (3.7 liters) of fluids for men,\nAbout 11.5 cups (2.7 liters) of fluids a day for women.",
        app_icon=r"E:\mayankvscode\projects\drink_water\icon.ico",
        timeout=10 
        )
        time.sleep(30*60)