import hashlib


def crack_sha1_hash(hash, use_salts=False):
  passwords_arr = []
  read_and_add_to_arr("top-10000-passwords.txt", passwords_arr)

  #If use_salts = True append and prepend known-salts to each top-10000-passwords
  if use_salts:
    top_salt_passwords = {}
    top_salts = []
    read_and_add_to_arr("known-salts.txt", top_salts)
    for bsalt in top_salts:
      for bpassword in passwords_arr:
        prepended = hashlib.sha1(bsalt + bpassword).hexdigest()
        appended = hashlib.sha1(bpassword + bsalt).hexdigest()
        top_salt_passwords[prepended] = bpassword.decode("utf-8")
        top_salt_passwords[appended] = bpassword.decode("utf-8")

    if hash in top_salt_passwords:
      return top_salt_passwords[hash]

  #Hashlib passwords_arr into hashes and compare to the hash that is passed in
  passwords_dict = {}
  for p in passwords_arr:
    hash_line = hashlib.sha1(p).hexdigest()
    passwords_dict[hash_line] = p.decode("utf-8")

  if hash in passwords_dict:
    return passwords_dict[hash]
    
  return "PASSWORD NOT IN DATABASE"

def read_and_add_to_arr(file_name, arr):
  #Read file wth passwords
  #rb = what sha-1 takes as an arguement
  #strip endline of \n
  #append all the passwords to array
  with open(file_name, "rb") as f:
    line = f.readline().strip()
    while line:
      arr.append(line)
      line = f.readline().strip()