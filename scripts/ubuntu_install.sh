# System-wide Dependecies and tools
sudo apt-get install git python3 ipython3 ipython3-notebook gettext

# Get the Poireau source
git clone https://github.com/ewjoachim/poireau.git

# Create a virtualenv with python3
# This would be th normal way :
# python3 -m venv poireau

# But on Ubuntu 14.04 (trusty), a bug forces to do it like in 2 steps :
# https://bugs.launchpad.net/ubuntu/+source/python3.4/+bug/1290847
python3 -m venv --without-pip ~/Envs/poireau
curl -L https://bootstrap.pypa.io/get-pip.py | ~/Envs/poireau/bin/python

# Install the python requirements
cd poireau/
~/Envs/poireau/bin/pip install -r requirements.txt
