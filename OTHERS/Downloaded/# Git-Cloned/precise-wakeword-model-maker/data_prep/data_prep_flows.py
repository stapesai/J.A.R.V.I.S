from data_prep.precise_ops import (
    BasicFileOperations,
    TrainTestSplit,
    PreciseModelingOperations,
    GaussianNoiseHandler,
)


train_test_split_instance = TrainTestSplit()
precise_modeling_operations_instance = PreciseModelingOperations()
basic_file_operations = BasicFileOperations()
gaussian_handler_instance = GaussianNoiseHandler()

# TODO: The flows will be used in a CLI, where the varibles can be given in the command line


# TODO: Where do I put in the functions for cleaning up after

# TODO: Where does incremental training (and precise listen, precise test) come in? Is it in another class?
# this final flow!
# A model is trained from the 'base' data
# precise test, listen (5 times in a row wake word)
# Incremental training is run over the 'random' user_collected data
# The model is deleted
# The generated files (directories?) are combined and randomly split (into training and test directories)
# A model is trained with the 'base' and the 'generated' data
# precise test, listen (5 times in a row wake word, 3 times each sub-wake-words [syllables or parts])
# Incremental training is run over the 'random' 'other' 'non-utterance' data
# The model is deleted
# The NEW generated files (directories?) are combined and randomly split (into training and test directories)
# A model is trained with the 'base' and the 'generated' data
# precise test, listen (5 times in a row wake word, 3 times each sub-wake-words [syllables or parts])
# Incremental training is run over the 'random' 'other' 'common-voice' data (only a part? If so, how much?)
# ... And hopefully after common-voice is done, the last retrained model will be dope during the test and listen!


"""
#Flow A: 
# User inputs
# Note: user gives source directory
#source_directory = 'jarvis_S_B_remixed/'

# Note: user either selects default directories or can add their own directories
random_split_directories = [
    'wake-word/',
    'not-wake-word/background/',
]

even_odd_split_directories = [
    'wake-word/variations/',
]

three_four_split_directories = [
    'not-wake-word/parts/'
]

# Note: user can change base name of model or the path of the model experiment (in the same directory as the script) is the default (since they will be deleted anyway!)
root_model_name = 'experiment'

source_directory = 'jarvis_S_B_remixed/'

model_names = train_test_split_instance.experimental_splits(source_directory, random_split_directories, even_odd_split_directories, three_four_split_directories, root_model_name)


precise_modeling_operations_instance.run_experimental_training(model_names)

#print(precise_modeling_operations_instance.models)

# Pick best model
average_val_acc, standard_deviation_val_acc, average_acc, standard_deviation_acc = precise_modeling_operations_instance.get_models_analytics()

print(f'average test set accuracy: {average_val_acc} \u00B1 {standard_deviation_val_acc}')
print(f'average training set accuracy: {average_acc} \u00B1 {standard_deviation_acc}')

selected_model_name, selected_model_results = precise_modeling_operations_instance.pick_best_model()

print(f'{selected_model_name} produces the best results with {selected_model_results}')

# Delete experiment directories (except the best one!)
precise_modeling_operations_instance.delete_experiment_directories(selected_model_name)

# Incremental training of selected_model_name (FLOW B)

# When done with incremental, delete all the models, keep name/directory of selected_model_name, remix generated data, re-train
#precise_modeling_operations_instance.delete_experiment_models()
"""

# Delete model files:
"""
precise_modeling_operations_instance = PreciseModelingOperations()
precise_modeling_operations_instance.delete_model('experiment_1')
"""

"""
# Flow B: incremental over random
# Before gaussian noise, run an incremental over the random recordings (TV and conversation)
# Sub flow: combine the test and training from the random directory results
# run experimental_training on this to find the optimal test-train split (only splitting the random directory!)

random_user_recordings_directory = 'jarvis_S_B_remixed/random/user_collected/'

stdout = precise_modeling_operations_instance.incremental_training(selected_model_name, random_user_recordings_directory)
print('Incremental training complete')

# Sub flow: mix generated test and training and random split 80/20
train_test_split_instance.split_incremental_results(selected_model_name)

# delete test, training generated dir
precise_modeling_operations_instance.delete_generated_directories(selected_model_name)

# delete all experiment models
precise_modeling_operations_instance.delete_experiment_models()


# rename experiment to real model name
model_name = 'auto_generated_jarvis'
basic_file_operations.rename_directory(selected_model_name, model_name)
print(f'changed {selected_model_name} to {model_name}')


# Flow C: Background noise
# Sub flow: add recorded background noise to some directories files

model_name = 'auto_generated_jarvis'

noise_directory = 'jarvis_S_B_remixed/random/other/non-utterances/pdsounds_march2009/'

#precise_modeling_operations_instance.add_background_noise(model_name, noise_directory)

source_directories = [
            'background_noise/wake-word/',
            'background_noise/wake-word/variations/',
            'background_noise/test/wake-word/',
            'background_noise/test/wake-word/variations/',   
        ]

destination_directories = [
        'wake-word/background_noise/',
        'wake-word/background_noise/variations/',
        'test/wake-word/background_noise/',
        'test/wake-word/background_noise/variations/',
    ]
precise_modeling_operations_instance.move_noise_directories(model_name, source_directories, destination_directories)
"""
# Flow D: Gauss
"""
model_name = 'auto_generated_jarvis'

directories_to_gauss = [
    model_name + '/wake-word/',
    model_name + '/wake-word/variations/',
    model_name + '/not-wake-word/background/',
    model_name + '/not-wake-word/parts/',
    model_name + '/test/wake-word/',
    model_name + '/test/wake-word/variations/',
    model_name + '/test/not-wake-word/background/',
    model_name + '/test/not-wake-word/parts/'
]

gaussian_handler_instance.add_gaussian_noise_to_directories(directories_to_gauss)
"""

# Flow E: The final flow
# train a fresh model from the data (450 epochs? -> add epoch parameter in training method)
# Should the number of epochs grow with the number of files?
# This code will need to be more flexible to collect the directories from any user
model_name = "auto_generated_jarvis"
"""epochs = '450'
print('Training new model from collected data')
precise_modeling_operations_instance.run_precise_train(model_name, epochs)

datasets_root_directory = 'jarvis_S_B_remixed/random/other/'

incremental_data_directories = [
   datasets_root_directory + 'non-utterances/',
   datasets_root_directory + 'mycroft_not_wake_es/',
   datasets_root_directory + 'mycroft_not_wake_en/',
   datasets_root_directory + 'common_voice/'

]

# incremental on directories, re-split generated, delete old model, and retrain model 
precise_modeling_operations_instance.multi_incremental_training(model_name, incremental_data_directories)
"""
"""
print('Training final model')
epochs = '800'
precise_modeling_operations_instance.run_precise_train(model_name, epochs)
"""
# precise-listen, precise test ?
# TODO: add in feature for precise-test and parse the output (remove any gauss or added background noise from %)
# repeat until all directories done
# TODO: add in flows for sound data wrangling
# getting a max amount of files from a huge directory, break them down into directories with max files per directory
# converting mp3s to wav files in a directory


# From this point is copy-pasta of the basic functions (to be deleted once I am done here)

# Flow 1: get files and copy them to a directory
# turn into function?
"""
source_directory = "jarvis_S_B_remixed/jarvis_S_B_data_prepped/not-wake-word/parts/"
destination_directory = 'jarvis_S_B_remixed/jarvis_S_B_data_prepped/not-wake-word/dummy/'

basic_file_operations_instance = BasicFileOperations(source_directory)
files = basic_file_operations_instance.get_files()
basic_file_operations_instance.copy_directory(files, destination_directory)
"""

# Flow 2: combine files from several (2 or more) directories and copy them to a directory
# function?
"""
source_directories = ["jarvis_S_B_remixed/jarvis_S_B_data_prepped/not-wake-word/generated/", "jarvis_S_B_remixed/jarvis_S_B_data_prepped/test/not-wake-word/generated/"]
destination_directory = 'jarvis_S_B_remixed/generated/'
for source_directory in source_directories:
    basic_file_operations_instance = BasicFileOperations(source_directory)
    files = basic_file_operations_instance.get_files()
    basic_file_operations_instance.copy_directory(files, destination_directory)
"""

# Flow 3: train test split random
"""
source_directory = "jarvis_S_B_remixed/generated/"
training_directory = "jarvis_S_B_remixed/generated/training/"
testing_directory = "jarvis_S_B_remixed/generated/testing/"
dataset_percent_size = float(0.8)

basic_file_operations_instance = BasicFileOperations(source_directory)
files = basic_file_operations_instance.get_files()
train_test_split_instance = TrainTestSplit()
random_selected_training_files, random_selected_testing_files = train_test_split_instance.random_training_test_split(files, dataset_percent_size)
basic_file_operations_instance.copy_directory(random_selected_training_files, training_directory)
basic_file_operations_instance.copy_directory(random_selected_testing_files, testing_directory)
"""

# Flow 4: train test split even-odd
"""
source_directory = "jarvis_S_B_remixed/not-wake-word/parts/"
training_directory = "jarvis_S_B_remixed/not-wake-word/parts/training/"
testing_directory = "jarvis_S_B_remixed/not-wake-word/parts/testing/"

basic_file_operations_instance = BasicFileOperations(source_directory)
files = basic_file_operations_instance.get_files()
train_test_split_instance = TrainTestSplit()

selected_training_files, selected_testing_files = train_test_split_instance.even_odd_training_test_split(files)
basic_file_operations_instance.copy_directory(selected_training_files, training_directory)
basic_file_operations_instance.copy_directory(selected_testing_files, testing_directory)
"""

# Flow 5: split_directory (by type)
"""
source_directory = 'jarvis_S_B_remixed/not-wake-word/parts/'
training_directory = source_directory+'training/'
testing_directory = source_directory+'testing/'
split_type = 'even-odd'

train_test_split_instance = TrainTestSplit()
train_test_split_instance.split_directory(source_directory, training_directory, testing_directory, split_type)
"""

# Flow 6: split_multiple_directories:
"""
model_name = 'experiment'
source_directory = 'jarvis_S_B_remixed/'

sub_directories = [
    'wake-word/',
    'wake-word/variations/',
    'not-wake-word/background/',
    'not-wake-word/parts/'
    ]

random_split_directories = [
    'wake-word/',
    'not-wake-word/background/'
]

even_odd_split_directories = [
    'wake-word/variations/',
    'not-wake-word/parts/'
]

train_test_split_instance = TrainTestSplit()
train_test_split_instance.split_multiple_directories(model_name)
"""
# Flow 7: precise train
"""
# sub directories don't work so well here yet! Just use 1 directory
model_name = 'experiment_1'
training_run = precise_modeling_operations_instance.run_precise_train(model_name)
precise_modeling_operations_instance.get_last_epoch_model_info(model_name, training_run)
print(precise_modeling_operations_instance.models)
"""

# TEST STUFF

source_directory = "jarvis_S_B_remixed/"

# Note: user either selects default directories or can add their own directories
random_split_directory = "not-wake-word/test/"

train_test_split_instance.split_directory(
    source_directory + random_split_directory,
    source_directory + "test_train/",
    source_directory + "test_test/",
    "three_four",
)
