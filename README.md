# Awesome ChatGPT Prompts CLI

This is a command line tool that allows you to select a prompt to use with
ChatGPT from the [Awesome ChatGPT
Prompts](https://raw.githubusercontent.com/f/awesome-chatgpt-prompts)

<img src="https://i.imgur.com/hSgIZHp.jpeg" width="600">


## Installation

To install the dependencies needed to run this program, run:

`pip install -r requirements.txt`

The remote and custom prompts are installed under
`$XDG_DATA_HOME/chatgpt-prompts`

You will also need to have `fzf` locally installed. If you
don't have it already, you can install it by running:

### Debian, Ubuntu, etc
`sudo apt install fzf`

### CentOS, Fedora, etc
`sudo yum install fzf`

### macOS
TODO


## Usage

To use this program, run:

`cgpt.py [COMMAND]`

If no command is provided, it will present you with a list
of prompts that you can choose from. Use the up and down
arrow keys to navigate the list and the Enter key to
select a prompt.

You can also use the following commands:

- `update`: Update the list of prompts from the remote repository.
- `add`: Add a custom prompt to the list.


## Features

- [x] Update the list of prompts from the remote repository.
- [x] Add your own custom prompts
- [ ] Create a pull request to add custom prompts to the
  remote repository.
- [ ] Delete a custom prompt.
- [ ] macOS and Windows support

## Credits
The prompts in this tool are taken from the [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) repository.



