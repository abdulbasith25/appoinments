from passlib.context import CryptContext

# Create a password context with bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Your password (short example)
password = "Ba"

# Hash the password (truncated to 72 bytes just to be safe)
hashed_pw = pwd_context.hash(password[:72])

# Print the hashed password
print(hashed_pw)
