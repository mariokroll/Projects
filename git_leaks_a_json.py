from git import Repo
import json


def extract():
    # Set the repository link and the words to search
    directory, words = './skale-manager/', ['user', 'username', 'password', 'key', 'keys']

    # Get the repository
    repository = Repo(directory)

    # Get a list of every commit in the repository
    commits = list(repository.iter_commits('develop'))
    return commits, words
    

if __name__ == '__main__':
    # Get the commits, and the key words to look for
    commits, words = extract()

    # Create a dictionary where we will save the commits found
    dict_with_commits = {'Commits': {}}
    found = 0
    # Iterate for every commit
    for c in commits:
        # We look for the key words in the commits
        for word in words:
            if word.lower() in c.message.lower():
                found += 1
                dict_with_commits['Commits']['Commit '+str(found)] =  f'{c.hexsha} -> {c.message}'
    with open('git_leaks.json', 'w') as f:
        json.dump(dict_with_commits, f, indent=4)