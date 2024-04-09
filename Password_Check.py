
import requests
import hashlib
import sys

def request_api_data(query_character):
    url = 'https://api.pwnedpasswords.com/range/' + query_character
    res = requests.get(url)
    #Just to raise an error in case of any issuesRe
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check API and try again')
    return res


def get_password_leaks_count(hashes, hash_to_check):
    #Our API response returns in a series of lines, formatted like so > hashedpass : count
    #So what we do is create a generator for each line (hashed password, count)
    hashes = (line.split(':') for line in hashes.text.splitlines())
    #So we then unpack the items in this generator, and check if any of them equal our
    #password we want to check. If so, we return the count, else 0
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

def pwned_API_check(password):
    #Here we convert the password to bytes using utf8 encoding. We then create a hash
    #object from this. We then use the hexdigest method to convert it to hexadecimal string
    #then to uppercase
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    #Split the hashed password into first 5 digits, and the tail
    first_5_characters, tail = sha1password[:5], sha1password[5:]
    #We then use the first 5 hashed digits of the password to get a response from the API
    #Having this response on our own machine is more secure than sending the entire
    #hashed password
    response = request_api_data(first_5_characters)
    return get_password_leaks_count(response, tail)

#Here we define the main() function, our driver function. We pass args to it to allow
#us to check multiple passwords at once
def main(args):
    for password in args:
        count = pwned_API_check(password)
        if count:
            print(f'{password} was found {count} times, you should probably change your password!')
        else:
             print(f'{password} was not found, carry on')
    return 'done!'


#Voila
main(sys.argv[1:])
