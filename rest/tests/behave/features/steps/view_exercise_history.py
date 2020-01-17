from behave import *
from behave.runner import Context
from tests.behave.utils import behave_request


@given('I try to get exercise history right')
def step_impl(context: Context):
    url = 'http://localhost:8517/v1/exercise/some_id/history'
    context.response = behave_request('GET', url)


@given('I try to specify invalid exercise ID')
def step_impl(context: Context):
    url = 'http://localhost:8517/v1/exercise/some-invalid-id/history'
    context.response = behave_request('GET', url)