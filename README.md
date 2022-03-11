# Happy Assisant
---
## Description
An open-source solution as opposed to Google Assistant or Alexa. This project is currently being developed by one individual.
---
## Installation
```bash
cd Happy_Assistant/
pip3 install -r requirements.txt
python3 main.py
```
---
## Commands
### Startup
```bash
happy
```
This starts up the assistant, which allows you to give a second command.

### Secondary
```bash
play [song]
```
Downloads and plays a song of your choice, completely automatic.

```bash
download [song]
```
Only downloads a song, and stores it afterwards for later use.

```bash
time
```
Returns the current time.

```bash
wikipedia [who is|what is] [subject]
```
Returns a summary of the subject you want information about. 'Who is' gives you information about a person, while 'What is' gives you information about an object.

```bash
qr code for|qr codes for [song]
```
Convert a URL to QR code format and saves it afterwards.

```bash
search [subject]
```
Returns a search result of your desired subject.

```bash
calculate [number1] [number2] -> [add|substract|multiply|divide]
```
Calculates a mathematical operation fot you, then returns it.