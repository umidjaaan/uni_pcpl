# test_smart_home.py
import unittest
from unittest.mock import MagicMock, patch
from smart_home import DeviceFactory, SmartLight, SocketAdapter, OldSocket, MotionSensor, SecurityHub

class TestSmartHomeTDD(unittest.TestCase):

    # Тест Factory Method (TDD подход: проверяем создание)
    def test_factory_creates_light(self):
        device = DeviceFactory.create_device("light")
        self.assertIsInstance(device, SmartLight)
        self.assertEqual(device.get_status(), "OFF")

    # Тест Adapter
    def test_adapter_translates_method(self):
        old_socket = OldSocket()
        adapter = SocketAdapter(old_socket)

        result = adapter.turn_on()

        self.assertEqual(result, "Socket powered with 220V")
        self.assertEqual(adapter.get_status(), "ON")

    # --- Использование Mock-объектов ---
    def test_observer_notification_with_mock(self):
        # Нам не нужно реальное поведение SecurityHub, мы хотим проверить,
        # что Sensor действительно вызывает метод update у подписчиков.

        sensor = MotionSensor()
        mock_hub = MagicMock() # Создаем Mock-объект вместо реального Hub

        sensor.attach(mock_hub)
        sensor.detect_motion()

        # Проверяем, был ли вызван метод update ровно один раз
        mock_hub.update.assert_called_once_with("Motion detected in living room!")

if __name__ == '__main__':
    unittest.main()
