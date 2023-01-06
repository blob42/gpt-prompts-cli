#!/usr/bin/env python3


import os
import sys
import requests
import csv

# We will need to import the `click` package to build the CLI.
import click

# We will also need to import the `fzf` package to use the `fzf` command.
from pyfzf.pyfzf import FzfPrompt as Fzf

XDG_DATA_HOME = os.environ.get('XDG_DATA_HOME', os.path.expanduser('~/.local/share'))
PROMPTS_URL = "https://raw.githubusercontent.com/f/awesome-chatgpt-prompts/main/prompts.csv"
CACHE_LOCATION = os.path.join(XDG_DATA_HOME, "chatgpt-prompts", "prompts.csv")
PROMPTS_REPO_URL = "https://github.com/f/awesome-chatgpt-prompts"
REPO_PROMPTS_RELPATH = "prompts.csv"

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

# select and return a tuple (act, prompt)
def choose_prompt(custom_only=False):
    prompts = load_prompts(custom_only)

    # load custom prompts

    chooser = Fzf()
    header = "'Select an act'"

    # preview the prompt of the selected act
    preview = f"'cat {CACHE_LOCATION} | grep {{1}} | cut -d, -f 2'"

    preview_window = "right:50%,wrap"
    act = chooser.prompt(prompts.keys(), '--header={} --preview-window={} --preview {}'.format(header, preview_window, preview,))
    prompt = prompts.get(act[0])

    return (act[0], prompt)

def show_prompts():
    act, prompt = choose_prompt()
    print(prompt)


# update refreshes the prompts from the remote repo
@click.command()
def update():
    cache_prompts(update=True)

# We will create a function called `pr` that will be executed when the `pr`
# command is provided.
@click.command()
def pr():
    print("[TODO] Opening a PR to add your prompt to the prompts repo")



# The add command allows the user to define a new prompt by providing the act and the prompt
@click.command()
def add():
    act = input("Enter the act title: ")
    prompt = input("Enter the prompt: ")
    save_prompt(act, prompt)


# We will add the `add`, `update`, and `pr` functions to the `show_prompts`
# function.
cli.add_command(add)
cli.add_command(update)
cli.add_command(pr)

# We will execute the `show_prompts` function if the script is executed directly
# without any command provided
if __name__ == "__main__":
    # if no command provided call show_prompts
    if len(sys.argv) == 1:
        show_prompts()

    else:
        cli()

