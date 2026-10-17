class SmartLight:
    """A simple smart light with on/off state and brightness (0-100)."""

    def __init__(self, name="Light"):
        self.name = name
        self.is_on = False
        self.brightness = 0

    def turn_on(self):
        self.is_on = True
        if self.brightness == 0:
            self.brightness = 100  # default brightness when first turned on
        print(f"{self.name} is ON at {self.brightness}% brightness.")

    def turn_off(self):
        self.is_on = False
        print(f"{self.name} is OFF.")

    def set_brightness(self, level):
        if not isinstance(level, (int, float)) or isinstance(level, bool):
            raise TypeError("Brightness must be a number.")
        if level < 0 or level > 100:
            raise ValueError("Brightness must be between 0 and 100.")
        self.brightness = level
        if self.is_on:
            print(f"{self.name} brightness set to {self.brightness}%.")
        else:
            print(f"{self.name} brightness saved at {self.brightness}% (light is off).")
