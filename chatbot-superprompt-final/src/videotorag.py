from openai import OpenAI
from moviepy.editor import VideoFileClip
import os

import ragscrap
import createvdb
import config


DATA_PATH = "data"
VIDEO_FILE_PATH = os.path.join(DATA_PATH, "files") 


def whisper_request(file_name):
    """
    Effectue une requête pour transcrire un fichier audio en utilisant le modèle de transcription "whisper-1" de OpenAI.
    Args:
        file_name (str): Le nom du fichier audio à transcrire.
    Returns:
        str: Le texte transcrit du fichier audio.
    """
    client = OpenAI()

    audio_file = open(file_name, "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file
    )
    # print("whisper_request(): ", transcription.text)
    return transcription.text


def convert_mp4_to_mp3(file_name):
    """Pas utilisé"""
    file_format = file_name.split(".")[-1]
    file_name = file_name.replace(file_format, "")

    mp4_file = file_name + "mp4"
    mp3_file = file_name + "mp3"

    video_clip = VideoFileClip(mp4_file)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(mp3_file)
    audio_clip.close()
    video_clip.close()

    return mp3_file


def split_video(input_file):
    """
    Divise une vidéo en plusieurs segments.
    Args:
        input_file (str): Le chemin du fichier vidéo à diviser.
    Returns:
        list(str): Retourne une liste des noms des parties du fichier divisé.
    """
    print("split_video(): ")
    clip = VideoFileClip(input_file)
    ten_minutes = 6 * 60 # 6 minutes en secondes
    duration = clip.duration
    start_time = 0
    end_time = ten_minutes 

    result = []

    if duration <= ten_minutes + 1:
        result.append(input_file)
        return result

    output_folder = input_file.replace(".mp4", "")
    
    part = 1
    while end_time <= duration:
        sub_clip = clip.subclip(start_time, end_time)
        sub_clip.write_videofile(f"{output_folder}_part{part}.mp4", codec="libx264")
        result.append(f"{output_folder}_part{part}.mp4")
        start_time = end_time
        end_time += ten_minutes
        part += 1
    
    # Si la dernière partie est plus courte que 6 minutes, on enregistre le reste
    if start_time < duration:
        sub_clip = clip.subclip(start_time, duration)
        sub_clip.write_videofile(f"{output_folder}_part{part}.mp4", codec="libx264")
        result.append(f"{output_folder}_part{part}.mp4")

    return result


def video_to_text(file_name, file_format=".mp4"):
    """
    Convertit une vidéo en texte en utilisant la transcription audio à l'aide du modèle de transcription "whisper-1" de OpenAI.
    Args:
        file_name (str): Le nom du fichier vidéo à transcrire.
        file_format (str, optional): Le format du fichier vidéo. Par défaut, ".mp4".
    Returns:
        str: Le texte transcrit de la vidéo.
    """
    title = file_name.replace(file_format, "")
    content = title+"\n\n"
    splited_files = None
    
    if "mp4" in file_format:
        splited_files = split_video(file_name)
    for file in splited_files:
        content += (whisper_request(file) + "\n\n")
    return content.strip()


def extract_info(apikey="", file_format=".mp4"):
    """
    Extrait des informations à partir de fichiers vidéo en les transcrivant en texte et en les enregistrant dans des fichiers Markdown.
    Args:
        apikey (str, optional): La clé API pour l'accès à OpenAI. Par défaut, une chaîne vide.
        file_format (str, optional): Le format des fichiers vidéo à traiter. Par défaut, ".mp4".
    Returns:
        True: Si l'extraction des informations a réussi.
    """
    if apikey != "":
        openai.api_key = apikey

    folder = VIDEO_FILE_PATH

    for file in os.listdir(VIDEO_FILE_PATH):
        file_path = os.path.join(VIDEO_FILE_PATH, file)
        if os.path.isfile(file_path) and file_path.endswith(file_format):
            print("extract_info(): "+file_path)
            content = video_to_text(file_path, file_format)
            file_name = file.replace(file_format, "")
            file_name = ragscrap.create_filename(file_name)

            writer_path = os.path.join(DATA_PATH, file_name+".md")
            with open(writer_path, 'w', encoding='utf-8') as mdfile:
                mdfile.write(content)

            createvdb.add_to_vectorstores(file_name)
            os.remove(file_path)

    return True


if __name__ == '__main__':
    extract_info()