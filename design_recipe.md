## 1 problem - user story
```
As a member of a group chat,
I want the chat's participants shown as a single readable line,
so that I can see at a glance who's in the conversation.

Acceptance criteria:

No participants: the line is empty.
[] => ""

One participant: just their name.
["Bart"] => "Bart"

Two participants: joined with an ampersand.
["Bart", "Lisa"] => "Bart & Lisa"

Three or more participants: commas between names, with an ampersand before the last one.
["Bart", "Lisa", "Maggie"] => "Bart, Lisa & Maggie"

Order is kept: names appear in the same order they were given.
```
## 2 function signature
```python
# Parameters:
# - to have one parameter which is a list
# Return type:
# - string of names
# Side Effects:
# - none
def display_members():
    pass
```

## 3 exampples
```python
# scenario 1 - display members when list is empty 

# scenario 2 - display when there is a single participant

# scenario 3 - when there's 2 an joined with an ampersand

# scenario 4 - when there's 3 joined with a comma and an ampersand
```