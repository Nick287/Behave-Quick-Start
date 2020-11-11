import random

import time
from api.common import CommonClient

# testing for double number function in API class
@given('Randomly generate a source number and set into global variable')
def step_impl(context):
    context.apiclient = CommonClient(context.configstring)
    context.sourcenumber = random.randrange(1,50)


@when('Call a double method and store the result in {number:d} seconds')
def step_impl(context, number):
    context.number = context.apiclient.ReturnDoubleNumber(int(context.sourcenumber))
    time.sleep(int(number))


@then('Check the double method results is correct or not')
def step_impl(context):
    assert int(context.sourcenumber) * 2 == int(context.number)


# Scenario: testing for plus one number function in API class
@when('Call a plus one method and store the result in {number:d} seconds')
def step_impl(context, number):
    context.number = context.apiclient.ReturnNumberPlusOne(int(context.sourcenumber))
    time.sleep(int(number))


@then('Check the plus one results is correct or not')
def step_impl(context):
    assert int(context.sourcenumber) + 1 == int(context.number)