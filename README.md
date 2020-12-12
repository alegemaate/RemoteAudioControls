# Remote Audio Controls

Created for the sole purpose of allowing another computer to be able to adjust music controls on a Windows machine.

## Packages

Required packages include `pypiwin32`
Install using:

```sh
pip install pypiwin32
```

## Running

First, start the server using:

```sh
python server.py
```

Then, run the client with a given ip and command:

```sh
python client.py <ip> <command>
```

## Commands

### toggle / play

Simulates play or pause media key on the host machine.

### up / down

Simulates the volume up or down media key on the host machine.

### next / skip, previous / prev

Simulates the next, previous media keys on the host machine.
