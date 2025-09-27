Password Generator
A simple Python script that generates secure random passwords.
Usage
python password_gen.py <length> [count]
Examples

#Generate one 12-character password (Default)
python password_gen.py

# Generate one 16-character password
python password_gen.py 16

# Generate 5 passwords of 20 characters each
python password_gen.py 20 5


#Features

Uses cryptographically secure random generation
Includes letters, numbers, and symbols
Excludes confusing characters (I, l, 1, O, 0)
Ensures each password has at least one character from each type

#Requirements

Python 3.6+

#How It Works
The script uses Python's **secrets** module which provides cryptographically strong random numbers suitable for managing passwords, account authentication, and security tokens.
