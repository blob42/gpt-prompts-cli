#!/usr/bin/env python3


import os
import sys
import requests
import csv
import uuid

# We will need to import the `click` package to build the CLI.
import click

from github import Github

# We will also need to import the `fzf` package to use the `fzf` command.
from pyfzf.pyfzf import FzfPrompt as Fzf

XDG_CONFIG_HOME = os.environ.get("XDG_CONFIG_HOME", os.path.expanduser("~/.config"))
CONFIG_DIR = os.path.join(XDG_CONFIG_HOME, "cgpt")
XDG_DATA_HOME = os.environ.get('XDG_DATA_HOME', os.path.expanduser('~/.local/share'))
PROMPTS_URL = "https://raw.githubusercontent.com/f/awesome-chatgpt-prompts/main/prompts.csv"
CACHE_LOCATION = os.path.join(XDG_DATA_HOME, "chatgpt-prompts", "prompts.csv")
PROMPTS_REPO_URL = "https://github.com/f/awesome-chatgpt-prompts"
REPO_PROMPTS_RELPATH = "prompts.csv"
TOKEN_FILE = os.path.join(CONFIG_DIR, "token")

PR_HELP = """
helper to create a PR from a custom prompt. The output can be appended to the prompts.csv file in the prompts repo. You can
pipe the output of this command to pbcopy or xclip to copy it to your
clipboard.

For example: `./cgpt.py pr | xclip -selection cliboard`

"""

# save custom prompts to my-prompts.csv
CUSTOM_PROMPTS = os.path.join(XDG_DATA_HOME, "chatgpt-prompts", "my-prompts.csv")

def cache_prompts(update=False):
    '''
    if the prompts are not cached, download them and cache them locally
    '''
    if not os.path.exists(CACHE_LOCATION) or update:
        print("Downloading remote prompts...")
        os.makedirs(os.path.dirname(CACHE_LOCATION), exist_ok=True)
        with open(CACHE_LOCATION, "w") as f:
            f.write(requests.get(PROMPTS_URL).text)
            f.close()

    # init custom prompts if not exists
    if not os.path.exists(CUSTOM_PROMPTS):
        with open(CUSTOM_PROMPTS, "w") as f:
            header = '"act","prompt"\n'
            f.write(header)
            f.close()

def init_config():
    if not os.path.exists(CONFIG_DIR):
        os.makedirs(CONFIG_DIR)


def load_prompts(custom_only=False):
    '''
    Loads the prompts from the cache. if the cache is empty, download the prompts.
    The prompts csv contains two columns separated by a comma in the form "act", "prompt"
    Returns the list of prompts as tuples
    '''

    cache_prompts()
    prompts = {}

    if not custom_only:
        with open(CACHE_LOCATION, "r") as f:
            prompts = f.readlines()
            
            # load the prompts into a list of tuples
            prompts = [tuple(prompt.strip().split(",")) for prompt in prompts]

            # transform into a dict of acts keys and prompt values
            prompts = {prompt[0]: prompt[1] for prompt in prompts[1:]}

            f.close()

    with open(CUSTOM_PROMPTS, "r") as f:
        custom_prompts = f.readlines()
        custom_prompts = [tuple(prompt.strip().split(",")) for prompt in custom_prompts]
        custom_prompts = {prompt[0]: prompt[1] for prompt in custom_prompts[1:]}
        prompts.update(custom_prompts)
        f.close()
    

    return prompts



# save custom prompts to CUSTOM_PROMPTS
def save_prompt(act, prompt):

    with open(CUSTOM_PROMPTS, "a") as f:
        f.write(f'"{act}","{prompt}"\n')
        f.close()


@click.group()
def cli():
    pass

class Fzfer:
    def __init__(self, prompts):
        self.act_prompt = prompts
        self.fzf = Fzf()
        self.header = "act,prompt"
        self.preview = f"'cat {CACHE_LOCATION} | grep {{1}} | cut -d, -f 2'"
        self.preview_window = "right:50%,wrap"

    def show(self):
        return self.fzf.prompt(self.act_prompt, '--header={} --preview-window={} --preview {}'.format(self.header, self.preview_window, self.preview))


# select and return a tuple (act, prompt)
def choose_prompt(custom_only=False):
    prompts = load_prompts(custom_only)
    f = Fzfer(prompts)
    act = f.show()
    prompt = prompts.get(act[0])
    return (act[0], prompt)

def show_prompts():
    act, prompt = choose_prompt()
    print(prompt)

# update refreshes the prompts from the remote repo
@click.command(help="update the prompts from the remote repo")
def update():
    cache_prompts(update=True)

def load_token():
    token = None
    if not os.path.exists(TOKEN_FILE):
        token = input("Please enter your GitHub token: ")
        with open(TOKEN_FILE, "w") as f:
            f.write(token)
            f.close()
    else:
        with open(TOKEN_FILE, "r") as f:
            token = f.readline().strip()
            f.close()

    return token

@click.command(help=PR_HELP)
def pr():
    '''
    Helper to create a PR from a custom prompt
    '''
    # select a custom prompt
    act, prompt = choose_prompt(custom_only=True)
    prompt = f'{act},{prompt}'
    print(prompt)

@click.command()
def add():
    act = input("Enter the act title: ")
    prompt = input("Enter the prompt: ")
    save_prompt(act, prompt)

@click.command(help="Show my custom prompts")
def my():
    '''
    Pick custom prompts
    '''
    prompts = load_prompts(custom_only=True)
    f = Fzfer(prompts)
    act = f.show()
    prompt = prompts.get(act[0])
    print(prompt)



cli.add_command(add)
cli.add_command(update)
cli.add_command(pr)
cli.add_command(my)

if __name__ == "__main__":
    # if no command provided call show_prompts
    if len(sys.argv) == 1:
        show_prompts()

    else:
        cli()

