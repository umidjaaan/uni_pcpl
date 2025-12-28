# smart_home.py
from abc import ABC, abstractmethod

# --- 1. Порождающий паттерн: Factory Method ---
class SmartDevice(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def get_status(self):
        pass

class SmartLight(SmartDevice):
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        return "Light is turned ON"

    def get_status(self):
        return "ON" if self.is_on else "OFF"

class SmartThermostat(SmartDevice):
    def __init__(self):
        self.temp = 20

    def turn_on(self):
        self.temp = 22
        return "Thermostat set to 22C"

    def get_status(self):
        return f"Temperature: {self.temp}"

class DeviceFactory:
    @staticmethod
    def create_device(device_type):
        if device_type == "light":
            return SmartLight()
        elif device_type == "thermostat":
            return SmartThermostat()
        raise ValueError("Unknown device type")

# --- 2. Структурный паттерн: Adapter ---
# Представим старую розетку с другим интерфейсом
class OldSocket:
    def power_socket(self, voltage):
        return f"Socket powered with {voltage}V"

# Адаптер приводит старую розетку к интерфейсу SmartDevice
class SocketAdapter(SmartDevice):
    def __init__(self, old_socket: OldSocket):
        self.old_socket = old_socket
        self.status = "OFF"

    def turn_on(self):
        self.status = "ON"
        return self.old_socket.power_socket(220) # Адаптация вызова

    def get_status(self):
        return self.status

# --- 3. Поведенческий паттерн: Observer ---
class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass

class SecurityHub(Observer):
    def __init__(self):
        self.log = []

    def update(self, message):
        self.log.append(f"ALARM: {message}")

class MotionSensor:
    def __init__(self):
        self._observers = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detect_motion(self):
        # Логика обнаружения...
        self._notify("Motion detected in living room!")

    def _notify(self, message):
        for observer in self._observers:
            observer.update(message)
