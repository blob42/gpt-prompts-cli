# Awesome ChatGPT Prompts CLI

This is a command line tool that allows you to select a prompt to use with
ChatGPT from the [Awesome ChatGPT
Prompts](https://raw.githubusercontent.com/f/awesome-chatgpt-prompts)


## Installation

To install the dependencies needed to run this program, run:

`pip install -r requirements.txt`

You will also need to have `fzf` locally installed.

## Usage

To use this program, run:

`cgpt.py [COMMAND]`

If no command is provided, it will present you with a list of prompts that you
can choose from. Use the up and down arrow keys to navigate the list and the
Enter key to select a prompt.

You can also use the following commands:

- `add`: Add a custom prompt to the list.
- `delete`: Delete a custom prompt from the list.
- `update`: Update the list of prompts from the remote repository.

## Features/TODO

- [x] Update the list of prompts from the remote repository.
- [x] Add support for custom prompts
- [ ] Create a pull request to add custom prompts to the
  remote repository.

## Credits
The prompts in this tool are taken from the [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) repository.



