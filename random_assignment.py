import secrets


AMOUNT_PARTICIPANTS = 18  # Choose an even number.

participants = []

for x in range(int(AMOUNT_PARTICIPANTS/2)):
    participants.append(1)
    participants.append(0)

print(participants)

input()
for x in range(AMOUNT_PARTICIPANTS):
    participant = secrets.choice(participants)
    print(participant)
    participants.remove(participant)
    input()