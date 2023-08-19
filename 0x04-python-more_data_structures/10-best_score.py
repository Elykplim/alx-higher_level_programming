#!/usr/bin/python3
def best_score(a_dictionary):
  """
  Returns a key with the biggest integer value.

  Args:
    a_dictionary: A dictionary where the keys are strings and the values are integers.

  Returns:
    A key with the biggest integer value, or None if no scores are found.
  """

  if a_dictionary is None:
    return None

  best_key = None
  best_score = None
  for key, value in a_dictionary.items():
    if best_score is None or value > best_score:
      best_key = key
      best_score = value

  return best_key


