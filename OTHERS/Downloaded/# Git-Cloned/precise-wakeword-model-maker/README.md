![Secret Sauce AI](https://github.com/secretsauceai/secret_sauce_ai/blob/main/SSAI_logo_2.3_compressed_cropped.png?raw=true)
# Precise Wakeword Model Maker
![Wake word](https://github.com/secretsauceai/secret_sauce_ai/blob/main/SSAI_wakeword_scene_compressed.png?raw=true)
## Do you want your own personal wake word?

The Precise Wakeword Model Maker takes a sparse amount of data and creates a production quality wakeword model with [Mycroft Precise](https://github.com/MycroftAI/mycroft-precise). It's part of the Secret Sauce AI [Wakeword Project](https://github.com/secretsauceai/secret_sauce_ai/wiki/Wakeword-Project). 

The Precise Wakeword Model Maker pulls out all of the tricks in AI to turn a very sparse data set into a production quality model.

* [How does it work?](https://github.com/secretsauceai/precise-wakeword-model-maker#how-does-it-work)
* [Installation](https://github.com/secretsauceai/precise-wakeword-model-maker#installation)
* [Configuration](https://github.com/secretsauceai/precise-wakeword-model-maker#configuration)
* [Usage](https://github.com/secretsauceai/precise-wakeword-model-maker#usage)
* [Data](https://github.com/secretsauceai/precise-wakeword-model-maker#data)
* [Running your wakeword model](https://github.com/secretsauceai/precise-wakeword-model-maker#running-your-wakeword-model)
* [Secret Sauce AI](https://github.com/secretsauceai/precise-wakeword-model-maker#secret-sauce-ai)

# How does it work?
## A user follows a data collection recipe
![data collection recipe](https://github.com/secretsauceai/secret_sauce_ai/blob/main/SSAI_ww_recipe_01.png)
It all starts with a user data collection for the wakeword and not-wakeword categories.
A user can use the [Wakeword Data Collector](https://github.com/secretsauceai/wakeword-data-collector)

## Precise Wakeword Model Maker recipes
### TTS voice data generation
![TTS voices recipe](https://github.com/secretsauceai/secret_sauce_ai/blob/main/SSAI_ww_recipe_02.png)
When you don't have enough data to train a model, generate it. TTS engines are scraped similar to the data collection recipe using TTS plugins from [OpenVoiceOS](https://openvoiceos.com/). The more the better! 

### Best model selection
![best model selection recipe](https://github.com/secretsauceai/secret_sauce_ai/blob/main/SSAI_ww_recipe_03.jpg)
How do you know if your test-training distibution yields the best model? When it comes to big data sets, randomly splitting it once (ie 80/20%) is usually good enough. However, when dealing with sparse data sets the initial test-training split becomes more important. By splitting the data set many times and training experimental models, the best initial data distribution can be found. This step can boost the model by as much as ~10% performance on the training set. 


### Incremental and curriculum learning
![learning recipe](https://github.com/secretsauceai/secret_sauce_ai/blob/main/SSAI_ww_recipe_04.jpg)
Only add false positives(*) to the training/test set. Why add a bunch of files that the model can classify correctly, when you can give the model lessons where it needs to improve.

Speaking of lessons, you don't learn by reading pages of a text book in a totally random order, do you? Why should a machine learning model be subjected to this added difficulty in learning? Let the machine learn with an ordered curriculum of data. This usually boosts the model's performance over the shotgun approach by 5%-10%. Not bad!

(*)NOTE: This actually worsens the raw score of the model, because it only trains and tests on hard to learn examples, instead of giving the model an easy A. But honestly, if you are getting 98% on your test and/or training set and it doesn't actually work correctly in the real world, you really need to reconsider your machine learning strategy. ;) 

### Noise generation recipes
![noise generation recipe](https://github.com/secretsauceai/secret_sauce_ai/blob/main/SSAI_ww_recipe_05.png)
Gaussian noise (static) is mixed into the pre-existing audio recordings, this helps make the model more robust and helps with generalization of the model.

A user can use other noisy data sets (ie [pdsounds](http://pdsounds.tuxfamily.org/)) to generate background noise into existing audio files, further ensuring a robust model that can wake up even in noisy environments.


# Installation
## Manually installing with Python
Precise requires Python 3.7 (for tensorflow 1.13 support)
* System dependencies: you can `apt-get install` these
    * python3-pip (`setup.sh` will install this for ubuntu)
    * libopenblas-dev (`setup.sh` will install this for ubuntu)
    * python3-scipy (`setup.sh` will install this for ubuntu)
    * cython (`setup.sh` will install this for ubuntu)
    * libhdf5-dev (`setup.sh` will install this for ubuntu)
    * python3-h5py (`setup.sh` will install this for ubuntu)
    * portaudio19-dev (`setup.sh` will install this for ubuntu)
    * ffmpeg
    * libttspico0
    * libttspico-utils
* Run the setup script: `./setup.sh`
* activate your venv: `source .venv/bin/activate`
* `pip install -r requirements_data_prep.txt --force-reinstall` (there seems to currently be an issue with some of the requirements from the original precise not working with current versions of certain packages).
* `pip install -r TTS_generator_requirements.txt`

## Docker
* Build the image from the dockerfile
	* Get the dockerfile from this repo 
	* build it, for example: `docker build -t precise-wakeword-model-maker .`
* Or [pull the image from dockerhub](https://hub.docker.com/repository/docker/bartmoss/precise-wakeword-model-maker/): `docker pull bartmoss/precise-wakeword-model-maker`
* You can run the container with such a command:

```
docker run -it \
  -v "local_directory_for_model_output:/app/out" \
  -v "local_collected_audio_directory:/data" \
  -v "local_directory_path_for_config/:/app/config" \
  bartmoss/precise-wakeword-model-maker
  ```

# Configuration
* configure the `config/data_prep_user_configuration.json` with the paths: 
	* `audio_source_directory` (the main directory for the recordings from `wakeword_recorder`, 
	* `wakeword_model_name` the name you want to give the wakeword model,
    * `pdsounds_directory` the directory to the mp3 (or wav) files: [pdsounds](http://pdsounds.tuxfamily.org/),
	* `extra_audio_directories_to_process`, which are all of the extra audio datasets you have downloaded besides pdsounds (see Data below)
* configure the `config/TTS_wakeword_config.json` with your wakeword and the individual syllables of your wakeword,
* configure the `config/TTS_engine_config.json` with your TTS settings. By default the `larynx_host` is `null`, this will use the server from [Neon AI](https://neon.ai/), you can run [Larynx](https://github.com/rhasspy/larynx) yourself and update the `larynx_host` to the correct host and port (ie `http://127.0.0.1:5002`)


# Usage
Note: don't forget to activate your venv `source .venv/bin/activate`

Run `python data_prep` to start the Precise Wakeword Model Maker, or run in the command line with arguments:
* `-h` or `--help`
* `-t` or `--tts-generation`
* `-b` or `--base-model`
* `-g` or `--generate-data`
* `-e` or `--generate-extra`
* `-a` or `--all`

![Precise Wakeword Model Maker menu](https://github.com/secretsauceai/secret_sauce_ai/blob/main/precise_wakeword_model_maker_menu.png)

### tl;dr If you're sure you [installed](https://github.com/secretsauceai/precise-wakeword-model-maker#installation) and configured everything correctly, and got all of the [data](https://github.com/secretsauceai/precise-wakeword-model-maker#data) you need, then go ahead and run through the steps or `5. Do it all`. 
Just make sure you know: it will take A LONG time to run everything. 


## 1. Generate TTS wakeword data
The wakeword and wakeword syllables in `config/TTS_wakeword_config.json` are used to scrape the TTS voices in `config/TTS_engine_config.json`. The results will be in `out/TTS_generated_converted/`. 

There are three types of resulting files:
* wakeword audio from the TTS engines: `out/TTS_generated_converted/wake-word/TTS/`
* not-wakeword audio from the TTS engines: `out/TTS_generated_converted/not-wake-word/TTS/`
	* individual syllables of the wakeword, ie 'hey', 'jar', 'vis'
	* sequential permutations of the wakeword syllables, ie 'hey jar' or 'javis' 

The syllables and sequential permutations are vital to ensure that the model doesn't get lazy and focus on parts of the wakeword, but the whole wakeword.

IMPORTANT: check each wakeword file in `out/TTS_generated_converted/wake-word/TTS/` and discard any samples where the wakeword is mispronounced before moving on to any other steps. 

## 2. Optimally split and create a base model from wake-word-recorder data
For effective machine learning, we need to have a good training and test set. This step uses the audio collected from `audio_source_directory` in `config/data_prep_user_configuration.json` and generated by TTS (see above) to create 10 different distributions between the test and training set, then trains an experimental model for each and finally keeps the one with the lowest loss (the model with the highest training set accuracy) renaming the model and its ditectory of data to your `wakeword_model_name` in `config/data_prep_user_configuration.json`, `out/wakeword_model_name/`. 

The experimental directories and models are temporarily stored in `out/` as `experiment_n` where n is the number of the experiment. 

The data is split in different ways, depending on the kind of data. This can be configured in `config/data_prep_system_configuration.json`. Unless you are using another source to collect data than [Wakeword Data Collector](https://github.com/secretsauceai/wakeword-data-collector), these settings should work fine. 
* `random_split_directories`: 80/20% totally randomly
* `even_odd_split_directories`: 50/50% even-odd splitting
* `three_four_split_directories`: 3/4th splitting

The TTS generated data is split 80/20%. 

Finally, the model will be incrementally trained to find false-positives from the random recordings (ie TV and natural conversations) in `audio_source_directory/random/user_collected/` where `audio_source_directory` is configured in `config/data_prep_user_configuration.json` and benchmarked. 

## 3. Generate extra data
Gaussian and background noise (ie [pdsounds](http://pdsounds.tuxfamily.org/)) is mixed is mixed into the audio files to produce further audio files. 

The list of directories for both are in  `config/data_prep_system_configuration.json`:
* Background audio is mixed in using `pdsounds_directory`in `config/data_prep_user_configuration.json`, each file mixed produces 5 files with random portions of audio mixed into the background. The `source_directories` are where the files are temporarily generated and the `destination_directories` are where they are added into the model's data directories. This uses Precise's `precise-add-noise` feature.
*  Gaussian noise is mixed in, each file produces 4 additional files with the following levels of Gaussian noise: 15%, 30%, 50%, 60%. 

Finally, the model is trained on this data and benchmarked.

## 4. Generate further data from other data sets
Although a lot of training and testing has gone on by now, the model has not yet reached production quality. It is very important to incrementally test and train it on as much not-wakeword data as possible to find potential false wake ups. 

You should download at least one very large data set (at least 50,000 random utterances of many people speaking into different mics), such as common voice. This data set can be in mp3 or wav format, all non-user-collected data sets are automatically converted from mp3 or even wav to wav with `16000` sample rate. Please read Data below for more information about these data sets and where to download them. 

These data sets can be added into `config/data_prep_user_configuration.json` where `extra_audio_directories_to_process` is the list of the directories where the data sets sources are (it is important to configure the directories directly to where the mp3 or wav files can be found) and `extra_audio_directories_labels` are the labels (sub directories) they will be stored into (ie `non-utterances`, `utterances`, etc. in `out/wakeword_model_name/random/`. Each directory must have a label. 

## 5. Do it all
You can do it all!

## 6. Exit
Always know your escape route.


#  Data
It is important to note that downloading a lot of data is vital to producing a bullet proof wake word model. In addition, it is important to note that data prep does not walk through sub directories of sound files. It only processes the top level directory. It is best to just dump audio files in the top level directory. The files can be in mp3 or wav format, data prep will convert them to wav with the the sample rate of `16000`.
* [pdsounds](http://pdsounds.tuxfamily.org/)
* [Precise community data](https://github.com/MycroftAI/Precise-Community-Data)
* [Open Path Music Data](https://archive.org/download/OpenPathMusic44V5/OpenPathMusic44V5.zip)
* [Common Voice](https://commonvoice.mozilla.org/en/datasets/) or from the [Kagle Common Voice](https://www.kaggle.com/mozillaorg/common-voice) dataset
* TTS data set of [most popular EN-US words spoken by multiple TTS voices](http://downloads.openvoiceos.com/datasets/8kwordstts_en_0.1.tar.gz)


# Running your wakeword model
The resulting model will be a TensorFlow 1.13 precise wakeword model. It can be easily run with `precise-listen wakeword_model_name.net`, [configured to be run in Mycroft](https://mycroft-ai.gitbook.io/docs/using-mycroft-ai/customizations/wake-word#configuring-your-precise-wake-word) or even converted to TensorFlow lite and be run by the [TensorFlow lite runner](https://github.com/OpenVoiceOS/precise-lite).


# Secret Sauce AI
* [Secret Sauce AI Overview](https://github.com/secretsauceai/secret_sauce_ai)
* [Wakeword Project](https://github.com/secretsauceai/secret_sauce_ai/wiki/Wakeword-Project)
    * [Wakeword Data Collector](https://github.com/AmateurAcademic/wakeword-recorder-py)
    * [Precise TensorFlow Lite Engine](https://github.com/OpenVoiceOS/precise_lite_runner)
    * [Precise Rust Engine](https://github.com/sheosi/precise-rs)
    * [SpeechPy MFCC in Rust](https://github.com/secretsauceai/mfcc-rust)

## Special thanks and dedication 
Although Secret Sauce AI is always about collaboration and community, special thanks should go to [Joshua Ferguson](https://github.com/skewballfox) for doing so much testing and code refactoring. We also extend a very warm thanks to the folks over at [Mycroft](https://mycroft.ai/), without whom there would be no FOSS tensorflow wakeword engine. 

### In loving memory of Heinz Sieber
-Bartmoss
