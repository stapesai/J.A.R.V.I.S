from os import makedirs

from TTS_generator.utils.TTS_generator_class import TTSGenerator
from TTS_generator.utils.basic_file_operations_class import BasicFileOperations


def wakeword_generator_flow(wakeword_model_name):
    TTS_generator_instance = TTSGenerator()
    TTS_generated_directory = 'TTS_generated'
    TTS_utterances, WAKEWORD_PATH, NOT_WAKEWORD_PATH = TTS_generator_instance.load_wakeword_config(
        TTS_generated_directory)

    makedirs(WAKEWORD_PATH, exist_ok=True)
    makedirs(NOT_WAKEWORD_PATH, exist_ok=True)


    TTS_generator_instance.scrape_tts_engines(
        utterances=TTS_utterances, wakeword_scraping=True)

    source_directories = [
        WAKEWORD_PATH,
        NOT_WAKEWORD_PATH,
    ]


    destination_directories = [
        './out/TTS_generated_converted/wake-word/TTS/',
        './out/TTS_generated_converted/not-wake-word/TTS/',
    ]

    for source_directory, destination_directory in zip(source_directories, destination_directories):
        TTS_generator_instance.convert_audio_files(
        source_directory, destination_directory)

    BasicFileOperations.delete_directory('./out/' + TTS_generated_directory + '/')

    print(f'{wakeword_model_name} TTS generated')