import os
from TTS_generator.TTS_generator_flow import wakeword_generator_flow
from data_prep.dialog_handler import DialogHandler
from data_prep.precise_ops import (
    BasicFileOperations,
    TrainTestSplit,
    PreciseModelingOperations,
    GaussianNoiseHandler,
)
from data_prep.get_base_model_flow import get_base_model_flow
from data_prep.data_generation_flow import data_generation_flow
from data_prep.further_data_generation_flow import further_data_generation_flow


import sys
import json
import getopt


# source_directory = str(input("Please enter the relative path to the wakeword recordings directory (ie audio/):\n"))

# wakeword_model_name = str(input("Please enter the name you want to give the wakeword model (ie. 'wakeword_model'):\n"))

# TODO: write data requirements for each flow (include urls)
with open(
    os.getcwd() + "/config/data_prep_user_configuration.json",
    "r",
) as file:
    user_configuration_dictionary = json.load(file)

source_directory = user_configuration_dictionary["audio_source_directory"]
wakeword_model_name = user_configuration_dictionary["wakeword_model_name"]
pdsounds_directory = user_configuration_dictionary["pdsounds_directory"]
directories_to_process = user_configuration_dictionary[
    "extra_audio_directories_to_process"
]
extra_audio_directories_labels = user_configuration_dictionary[
    "extra_audio_directories_labels"
]
max_files_from_source_directory = user_configuration_dictionary[
    "max_files_from_source_directory"
]
max_files_per_destination_directory = user_configuration_dictionary[
    "max_files_per_destination_directory"
]

with open(
    os.getcwd() + "/config/data_prep_system_configuration.json",
    "r",
) as file:
    system_configuration_dictionary = json.load(file)

random_split_directories = system_configuration_dictionary["random_split_directories"]
even_odd_split_directories = system_configuration_dictionary[
    "even_odd_split_directories"
]
three_four_split_directories = system_configuration_dictionary[
    "three_four_split_directories"
]
root_model_name = system_configuration_dictionary["root_model_name"]
source_directories = system_configuration_dictionary["source_directories"]
destination_directories = system_configuration_dictionary["destination_directories"]
directories_to_gauss = system_configuration_dictionary["directories_to_gauss"]


def do_all():
    wakeword_generator_flow(wakeword_model_name)

    get_base_model_flow(
        source_directory,
        random_split_directories,
        even_odd_split_directories,
        three_four_split_directories,
        root_model_name,
        wakeword_model_name
    )
    data_generation_flow(
        wakeword_model_name,
        source_directories,
        destination_directories,
        directories_to_gauss,
        pdsounds_directory,
    )
    further_data_generation_flow(
        directories_to_process,
        extra_audio_directories_labels,
        max_files_from_source_directory,
        max_files_per_destination_directory,
        wakeword_model_name,
    )


def interactive():
    dialog_handler_instance = DialogHandler("dialog.json", "main_menu_dialog")

    while True:
        cli_choice = input(
            dialog_handler_instance.render_template("input-numbered-main_choice")
        )

        if cli_choice == "1":
            wakeword_generator_flow(wakeword_model_name)

        if cli_choice == "2":
            base_model_info = get_base_model_flow(
                source_directory,
                random_split_directories,
                even_odd_split_directories,
                three_four_split_directories,
                root_model_name,
                wakeword_model_name,

            )

        elif cli_choice == "3":
            # TODO: fix base_model_info, it doesn't show up in the flow
            try:
                data_generation_flow(
                    wakeword_model_name,
                    source_directories,
                    destination_directories,
                    directories_to_gauss,
                    pdsounds_directory,
                    base_model_info,
                )
            except:
                data_generation_flow(
                    wakeword_model_name,
                    source_directories,
                    destination_directories,
                    directories_to_gauss,
                    pdsounds_directory,
                    base_model_info=None,
                )

        elif cli_choice == "4":
            further_data_generation_flow(
                directories_to_process,
                extra_audio_directories_labels,
                max_files_from_source_directory,
                max_files_per_destination_directory,
                wakeword_model_name,
            )

        elif cli_choice == "5":
            do_all()
            sys.exit()

        elif cli_choice == "6":
            sys.exit()


def cli(arg_list):
    # TODO add more options to override configs
    short_options = "htbgea"
    long_options = ["help", "tts-generation" "base-model", "generate-data", "generate-extra", "all"]
    args, _ = getopt.getopt(arg_list, short_options, long_options)
    print(args)
    for arg, _ in args:
        print(arg)
        if arg in ("-h", "--help"):
            print("unimplented, please try again later")
        elif arg in ("-t", "--tts-generation"):
            wakeword_generator_flow(wakeword_model_name)

        elif arg in ("-b", "--base-model"):

            base_model_info = get_base_model_flow(
                source_directory,
                random_split_directories,
                even_odd_split_directories,
                three_four_split_directories,
                root_model_name,
                wakeword_model_name,

            )
        elif arg in ("-g", "--generate-data"):
            try:
                data_generation_flow(
                    wakeword_model_name,
                    source_directories,
                    destination_directories,
                    directories_to_gauss,
                    pdsounds_directory,
                    base_model_info,
                )
            except:
                data_generation_flow(
                    wakeword_model_name,
                    source_directories,
                    destination_directories,
                    directories_to_gauss,
                    pdsounds_directory,
                    base_model_info=None,
                )
        elif arg in ("-e", "--generate-extra"):
            further_data_generation_flow(
                directories_to_process,
                extra_audio_directories_labels,
                max_files_from_source_directory,
                max_files_per_destination_directory,
                wakeword_model_name,
            )
        elif arg in ("-a", "--all"):
            do_all()
            print("done")
            sys.exit()


"""
Flow B:
Requires:
* Flow A
* Background noise sound files: 
    * link: http://pdsounds.tuxfamily.org/
    * source directory path
    * convert dataset?

Performs:
* Data generation: generates both gaussian noise and mixes background noises into samples
"""

"""
Flow C:
Requires:
* Flow A
* Incremental 'not-wake-word' test-training datasets: (links) source directory path
    * TODO: sample and split dataset (common voice dataset)
    * TODO: import: https://archive.org/download/OpenPathMusic44V5/OpenPathMusic44V5.zip
    * TODO: convert dataset (mp3 to wav with correct sample rate)

Performs:
* Incremental test-traing: 
    * tests the current model against random recordings
    * if a recording triggers the classifier as 'wake-word' it is chopped into pieces and added into the test and training test (80/20 random split)
    * the current model is deleted and a new model with the new generated training and test data is trained
    * the process repeats until all of the incremental 'not-wake-word' test-training datasets have been run.

Output:
Final production model to be used with the Precise engine. 
Note: Currently just the tf1 model is used. In the next version, the tf1 model will be converted to tf2 (tflite).

"""
