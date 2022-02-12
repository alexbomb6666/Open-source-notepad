import json
with open('notes.json', 'r') as file:
    notes = json.load(file)

def new_note():
  with open('notes.json', 'r') as file:
    notes = json.load(file)
  name = input("Enter the name of the note (or enter 'none' if you want to go to main menu): ")
  if name == "none":
    print("Redirecting to main menu...")
    main()
    return
  if name.isdigit():
    print("Your name cant be number!")
    new_note()
    return
  details = input("Enter the details of the note: ")
  try:
    test = notes[name]
  except KeyError:
    notes[name] = {
      "details" : details
    }
    with open("notes.json", "w") as write_file:
      json.dump(notes, write_file, indent = 4)
    print("Your note is created!")
    main()
    return
  print("You already have note with the same name!")
  new_note()
  return


def view_notes():
  count = 0
  note_lst = []
  flag = False
  with open('notes.json', 'r') as file:
    notes = json.load(file)
  print("Here are your notes:")
  for _ in notes:
    flag = True
    count += 1
    print(f"{count}: {_}")
    note_lst.append([count, _])
  if flag is False:
    print("You don't have any notes!")
  print("\n")
  name = input("What is the name of the note you want to see? (say 'none' to go to main menu): ")
  if name != "none":
    if name.isdigit() is True:
      is_found = False
      print("You entered a number! Trying to seek for the note...")
      for _ in note_lst:
        if _[0] == int(name):
          is_found = True
          name = _[1]
          break
      if is_found is True:
        print("Found it! It is " + name + "!")
      else:
        print("You cant enter the number as the name (it breaks the application lol).")
        view_notes()
        return
    try:
      test = notes[name]
    except KeyError:
      print("Where did you see the note with that name?")
      view_notes()
      return
    print("Here are the details:")
    print(f"{notes[name]['details']} \n")
    view_notes()
    return
  else:
    print("Redireting to main menu... \n")
    main()
    return


def delete_note():
  note_lst = []
  count = 0
  flag = False
  with open('notes.json', 'r') as file:
    notes = json.load(file)
  print("Here is the list btw \n")
  for _ in notes:
    flag = True
    count += 1
    print(f"{count}: {_}")
    note_lst.append([count, _])
  if flag is False:
    print("You don't have any notes!")
  print("\n")
  name = input("What note do you want to delete? (enter 'none' to leave): ")
  if name == "none":
    print("Redirecting to main page...")
    main()
    return
  if name.isdigit():
    is_found = False
    print("You entered the number! Seeking for note under this number:")
    for _ in note_lst:
      if _[0] == int(name):
        is_found = True
        name = _[1]
        break
    if is_found is True:
      print("Found it! It is " + name + "!")
    else:
      print("You cant enter the number as the name (it breaks the application lol).")
      delete_note()
      return
  try:
    test = notes[name]
  except KeyError:
    print("There is no note under this name/number! Please, try again!")
    delete_note()
    return
  del notes[name]
  with open("notes.json", "w") as write_file:
    json.dump(notes, write_file, indent = 4)
  print("Note succesfully deleted!")
  main()
  return


def main():
  print("Here are the features: \n 1.New note \n 2.View notes \n 3.Delete note. \n 4.Exit \n Just type in the feature you want to use")
  a = input()
  if a == "Exit" or a == "4":
    print("Exitting the application...")
    exit()
  elif a == "New note" or a == "1":
    new_note()
  elif a == "View notes" or a == "2":
    view_notes()
  elif a == "Delete note" or a == "3":
    delete_note()
  else:
    print("Sorry, didnt understand you :<")
    main()
    return

main()

