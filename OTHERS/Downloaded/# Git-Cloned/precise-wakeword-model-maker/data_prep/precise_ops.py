from os import mkdir


import subprocess

import numpy as np
from data_prep.fs_ops import BasicFileOperations

from os.path import isdir
from data_prep.model_analytics import ModelAnalytics
from data_prep.model_ops import TrainTestSplit

# TODO: split up the classes into separate files
# TODO: refactor classes


class PreciseModelingOperations:
    def __init__(self):
        self.model_analytics_instance = ModelAnalytics()
        self.models = self.model_analytics_instance.models

    @staticmethod
    def run_precise_train(model_name, epochs=None, source_directory=None):
        # TODO: better code for subprocess? What about closing when done? Should I use 'with'?

        if source_directory is None:
            if not isdir("out"):  # TODO: find out if this **should** fail
                mkdir("out")

            source_directory = "out/" + model_name + "/"

        if epochs is None:
            # TODO: Maybe 50 is a good number? Last one was 60.
            # TODO: change over to optimizing the training set first, then perhaps once the collection for test builds enough, use that.
            # Use the normal loss for the experiments and the first model after that.
            # Use '-sb', '-mm', 'val_loss' after generation(?) to optimize the test set.
            training_output = subprocess.Popen(
                [
                    "precise-train",
                    "-e",
                    "50",
                    "-s",
                    "0.215",
                    "-b",
                    "100",
                    "-sb",
                    "out/" + model_name + ".net",
                    source_directory,
                ],
                stdout=subprocess.PIPE,
            )
        else:
            training_output = subprocess.Popen(
                [
                    "precise-train",
                    "-e",
                    epochs,
                    "-s",
                    "0.215",
                    "-b",
                    "100",
                    "-sb",
                    "out/" + model_name + ".net",
                    source_directory,
                ],
                stdout=subprocess.PIPE,
            )
            # training_output = subprocess.Popen(['precise-train', '-e', epochs, '-b', '100', '-sb', model_name + '.net', source_directory], stdout=subprocess.PIPE)

        stdout = training_output.communicate()
        return stdout[0].decode("utf-8").split("\n")

    def get_model_info(self, model_name, training_run):
        self.model_analytics_instance.add_model(model_name, training_run)

    # TODO: re-factor:
    # get_max_difference
    # remove_model_with_max_difference,
    # get_max_testing_accuracy
    # get_max_train_accuracy

    def run_experimental_training(self, model_names):
        for model_name in model_names:
            # TODO: add optional parameter for sb to precise_train
            training_run = self.run_precise_train(model_name)
            self.model_analytics_instance.add_model(model_name, training_run)
        return self.model_analytics_instance.models

    def get_optimal_training_model_analytics(self):
        """This is a function that shows the average accuracy for training and test values by the best minimum loss of each model"""
        (
            average_acc_for_min_loss_models,
            stdev_acc_for_min_loss_models,
            average_val_acc_for_min_loss_models,
            stdev_val_acc_for_min_loss_models,
            average_acc_for_min_val_loss_models,
            stdev_acc_for_min_val_loss_models,
            average_val_acc_for_min_val_loss_models,
            stdev_val_acc_for_min_val_loss_models,
        ) = self.model_analytics_instance.get_model_analytics()
        return (
            average_acc_for_min_loss_models,
            stdev_acc_for_min_loss_models,
            average_val_acc_for_min_loss_models,
            stdev_val_acc_for_min_loss_models,
        )

    def get_max_difference(self):
        # TODO: follow up, this is disabled for now
        difference_list = []

        for item in self.models.items():
            difference = item[1]["difference"]
            difference_list.append(difference)
        return max(difference_list)

    def remove_model_with_max_difference(self):
        """returns dictionary without max difference model"""
        # TODO: follow up, this is diabled for now
        best_models = {}
        difference_max = self.get_max_difference()

        for item in self.models.items():
            model_name = item[0]
            difference = item[1]["difference"]
            acc = item[1]["acc"]
            val_acc = item[1]["val_acc"]
            if difference is not difference_max:
                best_model_accuracy = {}
                best_model_accuracy["acc"] = acc
                best_model_accuracy["val_acc"] = val_acc
                best_model_accuracy["difference"] = difference
                best_models[model_name] = best_model_accuracy
        return best_models

    def get_max_testing_accuracy(self, models):
        val_acc_list = []

        for item in models.items():
            val_acc = item[1]["val_acc"]
            val_acc_list.append(val_acc)
        return max(val_acc_list)

    def get_max_training_accuracy(self, models):
        acc_list = []

        for item in models.items():
            acc = item[1]["acc"]
            acc_list.append(acc)
        return max(acc_list)

    def get_best_loss_model(self):
        (
            best_model_loss_name,
            best_val_loss_name,
        ) = self.model_analytics_instance.get_best_model_names()
        return best_model_loss_name, self.models[best_model_loss_name]

    def delete_experiment_directories(self, selected_model_name):
        """get all directories,
        remove if not best model directory"""
        basic_file_operations_instance = BasicFileOperations()
        for model in self.models:
            if model is not selected_model_name:
                model_directory = "out/" + model + "/"
                basic_file_operations_instance.delete_directory(model_directory)

    def delete_model(self, model):
        basic_file_operations_instance = BasicFileOperations()
        model_extensions = [".logs", ".net", ".epoch", ".net.params", ".trained.txt"]
        for extension in model_extensions:
            file_to_delete = "out/" + model + extension
            print(file_to_delete)
            if extension is ".logs":
                basic_file_operations_instance.delete_directory(file_to_delete)
            elif extension is ".net":
                if isdir(file_to_delete):
                    basic_file_operations_instance.delete_directory(file_to_delete)
                else:
                    basic_file_operations_instance.delete_file(file_to_delete)

            else:
                basic_file_operations_instance.delete_file(file_to_delete)

    def delete_generated_directories(self, model_name):
        source_directories = [
            "out/" + model_name + "/not-wake-word/generated/",
            "out/" + model_name + "/test/not-wake-word/generated/",
        ]
        basic_file_operations_instance = BasicFileOperations()
        for directory in source_directories:
            basic_file_operations_instance.delete_directory(directory)

    def delete_experiment_models(self, selected_model_name):
        for model in self.models:
            if model is not selected_model_name:
                self.delete_model(model)

    def rename_model(self, model_name, selected_model_name):
        basic_file_operations_instance = BasicFileOperations()
        model_extensions = [".net", ".epoch", ".net.params", ".trained.txt", ".logs"]

        for extension in model_extensions:
            # NOTE: in future refactor this may be where we shift from
            # tmp dir to out dir (intended byproduces)
            file_to_rename = "out/" + model_name + extension
            new_file_name = "out/" + selected_model_name + extension
            if extension is ".logs":
                basic_file_operations_instance.rename_directory(
                    file_to_rename + "/", new_file_name + "/"
                )
            else:
                basic_file_operations_instance.rename_file(
                    file_to_rename, new_file_name
                )

    def copy_model(self, model_name):
        basic_file_operations_instance = BasicFileOperations()
        # I removed .training.txt from copying as there is none for this model since it only runs with normal training
        # TODO: Should I save the .trained.txt file from the incremental training?
        model_extensions = [
            ".net",
            ".epoch",
            ".net.params",
        ]

        for extension in model_extensions:
            # NOTE: renamed copy should be tmp in future
            file_to_copy = "out/" + model_name + extension
            renamed_copy = "out/" + model_name + "_tmp_copy" + extension
            basic_file_operations_instance.backup_file(file_to_copy, renamed_copy)
        return model_name + "_tmp_copy"

    def incremental_training(self, model_name, incremental_data_directory):
        # TODO: cool idea: number of files done, number remaining?
        source_directory = "out/" + model_name + "/"
        # copy model to same path as model_name + '_tmp_copy'
        temporary_model_name = self.copy_model(model_name)
        training_output = subprocess.Popen(
            [
                "precise-train-incremental",
                "out/" + temporary_model_name + ".net",
                source_directory,
                "-r",
                incremental_data_directory,
            ],
            stdout=subprocess.PIPE,
        )
        stdout = training_output.communicate()
        return stdout[0].decode("utf-8").split("\n")

    def multi_incremental_training(self, model_name, incremental_data_directories):
        train_test_split_instance = TrainTestSplit()
        epochs = "50"
        for incremental_data_directory in incremental_data_directories:
            print(f"Incremental training on {incremental_data_directory}")
            self.incremental_training(model_name, incremental_data_directory)
            train_test_split_instance.split_incremental_results(model_name)
            self.delete_generated_directories(model_name)
            self.delete_model(model_name)
            print(f"Training fresh model for {model_name}")
            self.run_precise_train(model_name, epochs)

    @staticmethod
    def add_background_noise(model_name, noise_directory):
        basic_file_operations_instance = BasicFileOperations()
        model_directory = "out/" + model_name + "/"
        destination_directory = model_directory + "background_noise/"
        basic_file_operations_instance.make_directory(destination_directory)
        noise_generation_output = subprocess.Popen(
            [
                "precise-add-noise",
                "-if",
                "5",
                model_directory,
                noise_directory,
                destination_directory,
            ],
            stdout=subprocess.PIPE,
        )
        stdout = noise_generation_output.communicate()
        noise_generation_output = stdout[0].decode("utf-8").split("\n")
        return noise_generation_output

    def move_noise_directories(
        self, model_name, source_directories, destination_directories
    ):
        # should this be in the basic file operations?
        basic_file_operations_instance = BasicFileOperations()
        model_directory = "out/" + model_name + "/"
        for source, destination in zip(source_directories, destination_directories):
            source = model_directory + source
            destination = model_directory + destination
            files = basic_file_operations_instance.get_files(source)
            basic_file_operations_instance.copy_directory(files, source, destination)
        basic_file_operations_instance.delete_directory(
            model_directory + "background_noise/"
        )

    def listen(self):
        """I have so far decided against running the listen function of precise, but if anyone ever wants, here's where I would put it"""
        pass


class GaussianNoiseHandler:
    def add_gaussian_noise(self, file, directory):
        basic_file_operations_instance = BasicFileOperations()
        sample_frequency, wave_data = basic_file_operations_instance.read_wave_file(
            directory + file
        )
        gauss_directory = directory + "gauss/"
        basic_file_operations_instance.make_directory(gauss_directory)
        # TODO: pull noise level out and put into data_prep_user_configuration
        for noise_level in [15, 30, 50, 60]:
            noisy_data = wave_data + noise_level * np.random.randn(len(wave_data))
            noisy_data = noisy_data.astype("int16")
            gauss_file_name = file.replace(".wav", "") + "_" + str(noise_level) + ".wav"
            basic_file_operations_instance.write_wave_file(
                gauss_directory + gauss_file_name, sample_frequency, noisy_data
            )

    def add_gaussian_noise_to_directory(self, model_name, directory):
        basic_file_operations_instance = BasicFileOperations()
        source_directory = "out/" + model_name + "/" + directory
        files = basic_file_operations_instance.get_files(source_directory)
        for file in files:
            self.add_gaussian_noise(file, source_directory)

    def add_gaussian_noise_to_directories(self, model_name, directories_to_gauss):
        for directory in directories_to_gauss:
            self.add_gaussian_noise_to_directory(model_name, directory)
