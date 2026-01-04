login_count = {}

for log in logs:
    parts = log.split()
    user = parts[1]

    login_count[user] = login_count.get(user, 0) + 1

most_user = None
most_count = 0

for user, count in login_count.items():
    if count > most_count:
        most_user = user
        most_count = count

print("Login counts:")
for user, count in login_count.items():
    print(user, "->", count)

print("\nMost active user:", most_user, "with", most_count, "logins")
