password = input("Enter your password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

score = 0

# Check each character
for ch in password:
    if ch.isupper():
        has_upper = True

    if ch.islower():
        has_lower = True

    if ch.isdigit():
        has_digit = True

    if not ch.isupper() and not ch.islower() and not ch.isdigit():
        has_special = True

# Calculate score
if has_upper:
    score = score + 1

if has_lower:
    score = score + 1

if has_digit:
    score = score + 1

if has_special:
    score = score + 1

# Check password length
if len(password) >= 8:
    score = score + 1

# Display password strength
if score <= 2:
    print("\n🔴 Password Strength: Weak")
elif score <= 4:
    print("\n🟡 Password Strength: Medium")
else:
    print("\n🟢 Password Strength: Strong")

# Show details
print("\nPassword Analysis")
print("-----------------")
print("Length:", len(password))
print("Contains Uppercase:", has_upper)
print("Contains Lowercase:", has_lower)
print("Contains Digit:", has_digit)
print("Contains Special Character:", has_special)
print("Score:", score)