# Smart Lighting System with OOP

**Module 7 / Python OOP Lab**

A lightweight, object-oriented Python implementation of a smart lighting control system. This project demonstrates core Object-Oriented Programming (OOP) principles, defensive input validation, automated unit testing with Python's standard `unittest` framework, and clean modular code organization.

---

## Features

- **Object-Oriented Design**: Encapsulates smart light state (name, power state, brightness) within a dedicated `SmartLight` class.
- **Power Management**:
  - `turn_on()`: Activates the light and defaults brightness to 100% if currently at 0%.
  - `turn_off()`: Powers off the light while preserving configuration.
- **Defensive Brightness Control**:
  - `set_brightness(level)`: Adjusts light intensity within a 0–100 scale.
  - Strict type validation: Rejects non-numeric types and booleans with descriptive `TypeError`.
  - Boundary validation: Rejects values below 0 or above 100 with `ValueError`.
  - Smart status reporting: Logs whether the light is actively illuminated or storing brightness in the off state.

---

## File Structure

```text
smartlight-lab/
├── smart_light.py        # Contains only the SmartLight class definition
├── test_smart_light.py   # Automated unit tests using Python's unittest module
├── main.py               # Demo script showing interactive usage and method calls
├── README.md             # Project documentation and specifications
└── .gitignore            # Git ignore rules for Python bytecode, venv, and IDE files
```

---

## Getting Started

### Prerequisites

- Python 3.8 or higher (no external third-party dependencies required; uses Python standard library).

### Running the Demo

Execute the demo script to see the `SmartLight` class in action:

```bash
python main.py
```

**Expected output:**
```text
--- Demo ---
Living Room Light is ON at 100% brightness.
Living Room Light brightness set to 60%.
Living Room Light is OFF.
```

### Running the Unit Tests

Execute the test suite with verbose output:

```bash
python -m unittest test_smart_light -v
```

---

## Tests

The test suite in `test_smart_light.py` contains 7 automated unit tests covering all functional and error-handling requirements:

| Test Method | Description |
| :--- | :--- |
| `test_initial_state` | Verifies the light initializes in the OFF state (`is_on == False`) with `brightness == 0`. |
| `test_turn_on` | Ensures `turn_on()` sets `is_on` to `True` and assigns the default brightness of 100%. |
| `test_turn_off` | Verifies `turn_off()` successfully transitions `is_on` back to `False`. |
| `test_set_brightness_valid` | Confirms that setting a valid numeric brightness (e.g., 40%) updates the `brightness` attribute correctly. |
| `test_set_brightness_too_high` | Ensures passing a brightness level greater than 100 (e.g., 150) raises a `ValueError`. |
| `test_set_brightness_negative` | Ensures passing a negative brightness level (e.g., -5) raises a `ValueError`. |
| `test_set_brightness_wrong_type` | Verifies that passing non-numeric types (such as strings or booleans) raises a `TypeError`. |


---

## Possible Improvements

Future iterations could expand the capabilities of `SmartLight`:

1. **`toggle()` Convenience Method**: Quick one-call switching between ON and OFF states based on current state.
2. **Step-based Brightness Controls**: `dim(step=10)` and `brighten(step=10)` helper methods for incremental adjustments.
3. **Color & Color Temperature Support**: RGB color values (HEX/RGB tuples) and Kelvin color temperature (e.g., 2700K warm white to 6500K daylight).
4. **State Persistence**: Save and restore device state across sessions using JSON or SQLite.
5. **Scheduled Timers / Automation**: Support scheduled turn-off or gradual fade-in wake-up alarms.
