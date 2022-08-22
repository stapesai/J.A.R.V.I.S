FROM python:3.7.12

# Install Packages via apt and pip
RUN apt-get update
RUN apt-get install git libopenblas-dev python3-scipy libhdf5-dev python3-h5py portaudio19-dev ffmpeg -y --force-yes
#RUN apt-get install git-buildpackage -y
#RUN apt-get install libttspico-utils libttspico0
RUN pip install --upgrade pip
RUN pip install Cython

# Because of course, you can't just apt-get install libttspico0 libttspico-utils
RUN apt-get install libpopt-dev -y
RUN mkdir /picotts
RUN git clone https://github.com/naggety/picotts.git
WORKDIR /picotts/pico
RUN ./autogen.sh
RUN ./configure
RUN make install

# Clone Precise Wakeword Model Maker from Secret Sauce AI git repo
RUN mkdir /app 
WORKDIR /app
RUN git clone https://github.com/secretsauceai/precise-wakeword-model-maker.git .

# remove stuff that would break the setup from setup.sh (the default installation script from Precise uses sudo, while the container is already run in root, also we installed Cython above)
RUN sed -i -e 's/sudo //g' /app/setup.sh
RUN sed -i -e 's/cython //g' /app/setup.sh

# run modified setup.sh and install other requirements
RUN chmod u+x setup.sh
RUN ./setup.sh

# Create directories
RUN mkdir /data
RUN mkdir /app/out

# Pip Install additional dependencies in venv
RUN /app/.venv/bin/pip install h5py==2.10.0
RUN /app/.venv/bin/pip install pydub
RUN /app/.venv/bin/pip install -U ovos-plugin-manager
RUN /app/.venv/bin/pip install ovos-utils
RUN /app/.venv/bin/pip install ovos-tts-plugin-google-tx==0.0.2 ovos-tts-plugin-mimic2==0.1.3 ovos-tts-plugin-pico ovos-tts-plugin-responsivevoice==0.1.1 neon-tts-plugin-larynx_server

#If the larynx plugin ever messes around again, use this stable commit over the pip package: git+https://github.com/NeonGeckoCom/neon-tts-plugin-larynx_server@bd1efb57d5#egg=neon-tts-plugin-larynx_server

# I would love to start the container and it opens in the terminal in the venv with this script running, then a user can select which option they want, but it doesn't seem to work.
#CMD "/app/.venv/bin/python" "/app/wake_word_data_prep_ide.py"

# So we start it with bash, a user types 'source .venv/bin/activate' and then runs the script "python -m data_prep"
CMD bash