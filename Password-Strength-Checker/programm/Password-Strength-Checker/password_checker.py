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
print("\n========== Password Analysis ==========")
print("Password Length      :", len(password))
print("Contains Uppercase   :", has_upper)
print("Contains Lowercase   :", has_lower)
print("Contains Digit       :", has_digit)
print("Contains Special Char:", has_special)
print("Score                :", score)
print("=======================================")

if score <= 2:
    print("🔴 Password Strength : Weak")
elif score <= 4:
    print("🟡 Password Strength : Medium")
else:
    print("🟢 Password Strength : Strong")
    print("\nSuggestions:")

if score == 5:
    print("\nGreat! Your password meets all the basic security requirements.")
else:
    print("\nSuggestions:")

    if not has_upper:
        print("- Add at least one uppercase letter.")

    if not has_lower:
        print("- Add at least one lowercase letter.")

    if not has_digit:
        print("- Add at least one digit.")

    if not has_special:
        print("- Add at least one special character.")

    if len(password) < 8:
        print("- Password should be at least 8 characters long.")