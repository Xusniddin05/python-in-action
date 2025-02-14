def typeBasedTransformer(**kwargs):
  changed_kwargs= {}
  for key, value in kwargs.items():
    if isinstance(value, (int, float)):
      changed_kwargs[key] = value ** 2
    elif isinstance(value, str):
      changed_kwargs[key] = value[::-1]
    elif isinstance(value, bool):
      changed_kwargs[key] = not value
    elif isinstance(value, (list, tuple):
      changed_kwargs[key] = value[::-1]
    elif isinstance(value, dict):
      changed_kwargs[key] = {v: k for k, v in value.items()}
    else:
      changed_kwargs[key] = value
return changed_kwargs   
