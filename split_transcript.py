from pathlib import Path
from tqdm import tqdm
import shutil

def split_tux100h():
    with Path("datasets_root/tux100h-cvcorpus/metadata.csv").open("r", encoding="utf8") as metadata_file:
        metadata = [line.split("|") for line in metadata_file]
        texts = [item[1] for item in metadata]
        text_filenames = ["datasets_root/tux100h-cvcorpus/valid/spanish/tux-100h_new/utterance-" + item[0] + ".txt" for item in metadata]
        
        for i in tqdm(range(len(text_filenames))):
            with Path(text_filenames[i]).open("w", encoding="utf8") as output_file:
                output_file.write(texts[i])

def split_cvcorpus():
    with Path("cv-corpus-7.0-2021-07-21/es/validated.txt").open("r", encoding="utf8") as metadata_file:
        metadata = [line.split("\t") for line in metadata_file]
        texts = [item[2] for item in metadata]
        audio_filenames = ["cv-corpus-7.0-2021-07-21_validated/" + item[1] + ".txt" for item in metadata]
        
        for i in tqdm(range(len(audio_filenames))):
            with Path(audio_filenames[i]).open("w", encoding="utf8") as output_file:
                if audio_filenames[i] != "path":
                    output_file.write(texts[i])
        
        for name in audio_filenames:
            shutil.copyfile(
                'cv-corpus-7.0-2021-07-21/es/clips/'+name+'.mp3',
                'cv-corpus-7.0-2021-07-21_validated/'+name+'.mp3'
            )

def split_pespa(gender):
     with Path("datasets_root/PeruvianSpanish/train/peruvianvoices/es_pe_"+gender+"/line_index.tsv").open("r", encoding="utf8") as metadata_file:
        metadata = [line.split("\t") for line in metadata_file]
        texts = [item[1] for item in metadata]
        audio_filenames = ["datasets_root/PeruvianSpanish/train/peruvianvoices/es_pe_"+gender+"/" + item[0] + ".txt" for item in metadata]
        
        for i in tqdm(range(len(audio_filenames))):
            with Path(audio_filenames[i]).open("w", encoding="utf8") as output_file:
                output_file.write(texts[i])


if __name__=="__main__":
    #for i in range(52408):
    #    shutil.copyfile(
    #            'datasets_root/tux100h-cvcorpus/valid/spanish/tux-100h/'+str(i)+'.wav',
    #            'datasets_root/tux100h-cvcorpus/valid/spanish/tux-100h_new/utterance-'+str(i)+'.wav'
    #        )
    #split_tux100h()
    split_pespa("female")
    split_pespa("male")