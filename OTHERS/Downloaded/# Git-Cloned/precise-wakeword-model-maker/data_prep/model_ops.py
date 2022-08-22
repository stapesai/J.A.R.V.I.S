import random

from data_prep.fs_ops import BasicFileOperations
from numpy.lib.function_base import copy
from os.path import isdir
from os import mkdir
from os.path import exists

# TODO: wrap this class around the data
# and directories associated with each expiremental model
class Model:
    pass


class TrainTestSplit:
    @staticmethod
    def random_training_test_split(files, dataset_percent_size):
        random_selected_training_files = random.sample(
            files, int(len(files) * dataset_percent_size)
        )
        random_selected_testing_files = [
            file for file in files if file not in random_selected_training_files
        ]
        return random_selected_training_files, random_selected_testing_files

    @staticmethod
    def even_odd_training_test_split(files):
        selected_training_files = []
        selected_testing_files = []
        for file in files:
            file_number = int(file.split("_")[-1].replace(".wav", ""))
            if (file_number % 2) == 0:
                selected_training_files.append(file)
            else:
                selected_testing_files.append(file)
        return selected_training_files, selected_testing_files

    @staticmethod
    def three_four_training_test_split(files):
        selected_training_files = []
        selected_testing_files = []
        count = 0
        for file in files:
            # TODO: add in this instead for final version file_number = int(file.split('_')[-1].replace('.wav', '')), and test it
            if count < 3:
                selected_training_files.append(file)
                count = count + 1
            else:
                selected_testing_files.append(file)
                count = 0
        return selected_training_files, selected_testing_files

    def split_directory(
        self, source_directory, training_directory, testing_directory, split_type
    ):
        """Function to split one directory and output the test and training directories
        pass split_type to use either random or even_odd"""
        dataset_percent_size = float(0.8)
        basic_file_operations_instance = BasicFileOperations()
        files = basic_file_operations_instance.get_files(source_directory)
        if split_type is "random":
            (
                random_selected_training_files,
                random_selected_testing_files,
            ) = self.random_training_test_split(files, dataset_percent_size)
            basic_file_operations_instance.copy_directory(
                random_selected_training_files, source_directory, training_directory
            )
            basic_file_operations_instance.copy_directory(
                random_selected_testing_files, source_directory, testing_directory
            )
        if split_type is "even_odd":
            (
                random_selected_training_files,
                random_selected_testing_files,
            ) = self.even_odd_training_test_split(files)
            basic_file_operations_instance.copy_directory(
                random_selected_training_files, source_directory, training_directory
            )
            basic_file_operations_instance.copy_directory(
                random_selected_testing_files, source_directory, testing_directory
            )
        if split_type is "three_four":
            (
                random_selected_training_files,
                random_selected_testing_files,
            ) = self.three_four_training_test_split(files)
            basic_file_operations_instance.copy_directory(
                random_selected_training_files, source_directory, training_directory
            )
            basic_file_operations_instance.copy_directory(
                random_selected_testing_files, source_directory, testing_directory
            )

    def split_multiple_directories(
        self,
        source_directory,
        destination_directory,
        random_split_directories,
        even_odd_split_directories,
        three_four_split_directories,
    ):
        sub_directories = (
            random_split_directories
            + even_odd_split_directories
            + three_four_split_directories
        )
        for sub_directory in sub_directories:
            training_directory = destination_directory + sub_directory
            testing_directory = destination_directory + "test/" + sub_directory
            for random_split_directory in random_split_directories:
                if sub_directory is random_split_directory:
                    split_type = "random"
                    self.split_directory(
                        source_directory + sub_directory,
                        training_directory,
                        testing_directory,
                        split_type,
                    )
            for even_odd_split_directory in even_odd_split_directories:
                if sub_directory is even_odd_split_directory:
                    split_type = "even_odd"
                    self.split_directory(
                        source_directory + sub_directory,
                        training_directory,
                        testing_directory,
                        split_type,
                    )
            for three_four_split_directory in three_four_split_directories:
                if sub_directory is three_four_split_directory:
                    split_type = "three_four"
                    self.split_directory(
                        source_directory + sub_directory,
                        training_directory,
                        testing_directory,
                        split_type,
                    )

    def experimental_splits(
        self,
        source_directory,
        random_split_directories,
        even_odd_split_directories,
        three_four_split_directories,
        root_model_name,
    ):
        """This will run when the user selects the default action to randomly perform"""
        model_names = [root_model_name + "_" + str(i + 1) for i in range(10)]
        if not isdir("out"):
            mkdir("out")

        TTS_path = "./out/TTS_generated_converted/"

        for model in model_names:
            destination_directory = "out/" + model + "/"
            self.split_multiple_directories(
                source_directory,
                destination_directory,
                random_split_directories,
                even_odd_split_directories,
                three_four_split_directories,
            )
            if exists(TTS_path):
                self.split_directory(
                    source_directory=TTS_path + 'wake-word/TTS/', training_directory=destination_directory + 'wake-word/TTS/', testing_directory=destination_directory + 'test/wake-word/TTS/', split_type='random')
                self.split_directory(
                    source_directory=TTS_path + 'not-wake-word/TTS/', training_directory=destination_directory +
                                     'not-wake-word/TTS/', testing_directory=destination_directory + 'test/not-wake-word/TTS/', split_type='random')

        return model_names

    def split_incremental_results(self, model_name):
        # TODO: This really needs to be split up!

        files = []
        dataset_percent_size = float(0.8)
        source_directories = [
            "out/" + model_name + "/not-wake-word/generated/",
            "out/" + model_name + "/test/not-wake-word/generated/",
        ]

        training_directory = "out/" + model_name + "/not-wake-word/random/"
        testing_directory = "out/" + model_name + "/test/not-wake-word/random/"

        basic_file_operations_instance = BasicFileOperations()

        for source_directory in source_directories:
            files += basic_file_operations_instance.get_files(source_directory)
        (
            random_selected_training_files,
            random_selected_testing_files,
        ) = self.random_training_test_split(files, dataset_percent_size)
        for source_directory in source_directories:
            basic_file_operations_instance.copy_directory(
                random_selected_training_files, source_directory, training_directory
            )
            basic_file_operations_instance.copy_directory(
                random_selected_testing_files, source_directory, testing_directory
            )

        print(
            "Finished spliting all files in generated test and training to random test and training directories"
        )
