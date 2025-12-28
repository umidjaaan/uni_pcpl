from behave import given, when, then
# Импортируем классы из корневой директории (возможно потребуется настройка PYTHONPATH)
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from smart_home import DeviceFactory

@given('a smart light is installed')
def step_impl(context):
    # Используем Factory для создания
    context.device = DeviceFactory.create_device("light")

@given('the light is currently off')
def step_impl(context):
    assert context.device.get_status() == "OFF"

@when('I turn the light on')
def step_impl(context):
    context.response = context.device.turn_on()

@then('the light status should be "{status}"')
def step_impl(context, status):
    assert context.device.get_status() == status

@then('the system should return "{message}"')
def step_impl(context, message):
    assert context.response == message
