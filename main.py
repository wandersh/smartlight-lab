from smart_light import SmartLight

if __name__ == "__main__":
    print("--- Demo ---")
    living_room = SmartLight("Living Room Light")
    living_room.turn_on()
    living_room.set_brightness(60)
    living_room.turn_off()
