from csv import DictReader

def column_to_list(file_name, column_name):
  try:
    with open(file_name) as file:
      return [row[column_name] for row in DictReader(file)]
  except KeyError:
    return "Column doesn't exist"