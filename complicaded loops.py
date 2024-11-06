# 1.
# will do as homework

# 2.
votes_for = []
votes_against = []
votes_impossible = []
votes_veto = []
while len(votes_for) + len(votes_against) + len(votes_impossible) + len(votes_veto) < 44:
    try:

        vote_select = int(input("Enter your vote : 1:for , 2:against , 3:impossible , 4:veto"))
        if vote_select == 1:
            votes_for.append(vote_select)
        elif vote_select == 2:
            votes_against.append(vote_select)
        elif vote_select == 3:
            votes_impossible.append(vote_select)
        elif vote_select == 4:
            votes_veto.append(vote_select)
        else:
            continue
    except ValueError:
        print("put in correct number")
        continue
print(f"sum votes for: {len(votes_for)}")
print(f"sum votes against: {len(votes_against)}")
print(f"sum votes impossible: {len(votes_impossible)}")
if votes_veto:
    print("the country that vote veto: ")
    for country in votes_veto:
        print(f"number country {country}")
