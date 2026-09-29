def display_members(members):
    
    if members == []:
        return ""
    if len(members) == 1:
        return members[0]
    if len(members) == 2:
        return ' & '.join(members)

    


    return f"{', '.join(members[:-1])} & {members[-1]}"


