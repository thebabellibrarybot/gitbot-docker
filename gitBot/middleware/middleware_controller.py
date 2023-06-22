from flask import current_app
from time import time

def middleware_handler(response):
    # Modify the response or perform actions
    # Here, we are adding a custom header to the response
    response.headers['Custom-Header'] = 'Some value'
    return response

def start_timer():
  """Starts a timer."""
  current_app._timer = time()
  print('start_timer')

def stop_timer():
  """Stops the timer and returns the elapsed time."""
  if not hasattr(current_app, "_timer"):
    raise RuntimeError("Timer not started")
  elapsed_time = time() - current_app._timer
  print('stop_timer', elapsed_time)
  del current_app._timer
  return elapsed_time