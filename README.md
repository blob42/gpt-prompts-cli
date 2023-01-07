# Awesome ChatGPT Prompts CLI

This is a command line tool that allows you to select a prompt to use with
ChatGPT from the [Awesome ChatGPT
Prompts](https://raw.githubusercontent.com/f/awesome-chatgpt-prompts) or define
your own custom prompts.

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
`brew install fzf`
then
`/usr/local/opt/fzf/install`


## Usage

To use this program, run:

`./cgpt.py [COMMAND]` 


Or print the help with:

`./chpt.py --help` 

If no command is provided, it will present you with a list
of prompts that you can choose from. Use the up and down
arrow keys to navigate the list and the Enter key to
select a prompt.

You can also use the following commands:

- `update`: Update the list of prompts from the remote repository.
- `add`: Add a custom prompt to the list.
- `my`: List my custom prompts.
- `pr`: Helper to create a pull request to add a custom prompt to awesome-chatgpt-prompts repo.  


## Features

- [x] Update the list of prompts from the remote repository.
- [x] Add your own custom prompts
- [ ] Create a pull request to add custom prompts to the
  remote repository.
- [ ] Delete a custom prompt.
- [ ] macOS and Windows support

## Credits
The prompts in this tool are taken from the [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) repository.

## I am Using GitHub Under Protest

This project is currently hosted on my [personal
forge](https://git.blob42.xyz/sp4ke/gpt-prompts-cli) and mirrored on GitHub.
This is not ideal; GitHub is a proprietary, trade-secret system that is not
Free and Open Souce Software (FOSS).  I am deeply concerned about using a
proprietary system like GitHub. I urge you to read about the [Give up
GitHub](https://GiveUpGitHub.org) campaign from [the Software Freedom
Conservancy](https://sfconservancy.org) to understand some of the reasons why
GitHub is not a good place to host FOSS projects.

Any use of this project's code by GitHub Copilot, past or present, is done
without our permission.  We object to GitHub using the code from this project
in Copilot. Given that this program is connected to ChatGPT, which utilizes
GPT-3 from OpenAI like Copilot, you would consider this to be hypocritical. We
do not have a choice, though; companies like Microsoft and OpenAI restricted
their models with private barriers after training their models using
open-source knowledge from humans. All people should have access to this
technology, but until then we must adapt to and make use of these tools
that offer those who utilize them an unfair advantage over those who don't.
