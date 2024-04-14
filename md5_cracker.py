import hashlib
import sys

def md5_hash(word):
    """Convert a given word to its MD5 hash."""
    hasher = hashlib.md5()
    hasher.update(word.encode('utf-8'))
    return hasher.hexdigest()

def crack_password(wordlist, target_hash):
    """Attempt to crack the provided MD5 hash using the given wordlist."""
    try:
        with open(wordlist, 'r') as file:
            for word in file:
                word = word.strip()
                if md5_hash(word) == target_hash:
                    return f"Password cracked: {word}"
        return "Password cannot be cracked."
    except FileNotFoundError:
        return "Wordlist file not found."

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <wordlist> <md5_hash>")
    else:
        wordlist_path = sys.argv[1]
        md5_hash_input = sys.argv[2]
        result = crack_password(wordlist_path, md5_hash_input)
        print(result)