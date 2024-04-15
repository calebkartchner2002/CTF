import hashlib

# this is for getting the encrypted password to be
# given to participants

def hash_password(password):
    hasher = hashlib.sha256()
    hasher.update(password.encode('utf-8'))
    return hasher.hexdigest()

def main():
    password = 'passw0rd'
    hashed = hash_password(password)
    print(f"Hashed password: {hashed}")

main()