from pathlib import Path
from tqdm import tqdm
import shutil
import os
import argparse
from utils.argutils import print_args

def split_tux100h():
    with Path("datasets_root/tux100h-cvcorpus/metadata.csv").open("r", encoding="utf8") as metadata_file:
        metadata = [line.split("|") for line in metadata_file]
        texts = [item[1] for item in metadata]
        text_filenames = ["datasets_root/tux100h-cvcorpus/valid/spanish/tux-100h_new/utterance-" + item[0] + ".txt" for item in metadata]
        
        for i in tqdm(range(len(text_filenames))):
            with Path(text_filenames[i]).open("w", encoding="utf8") as output_file:
                output_file.write(texts[i])

def split_cvcorpus(transcript_dir,dataset_dir):
    dataset_dir.mkdir(exist_ok=True)
    with Path(os.path.join(transcript_dir,"train.tsv")).open("r", encoding="utf8") as metadata_file:
        metadata = [line.split("\t") for line in metadata_file]
        texts = [item[2] for item in metadata[1:]]
        audio_filenames = [item[1] for item in metadata[1:]]
        filename_parts = [filename.split(".") for filename in audio_filenames]
        names = [part[0] for part in filename_parts]
        text_filenames = [os.path.join(dataset_dir, name) + ".txt" for name in names]
        
        for i in tqdm(range(len(audio_filenames))):
            with Path(text_filenames[i]).open("w", encoding="utf8") as output_file:
                output_file.write(texts[i])
        
        for name in names:
            shutil.copyfile(
                    os.path.join(transcript_dir,"clips",name)+".mp3",
                    os.path.join(dataset_dir,name)+".mp3"
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
    parser = argparse.ArgumentParser()
    parser.add_argument("transcript_dir", type=Path, help= \
        "Path to the transcript directory that contains the transcript with the information of, "
        "the audios and the texts.")
    parser.add_argument("-o", "--dataset_dir", type=Path, default="datasets_root/cvcorpus/train/spanish/cv-corpus/", help=\
        "Path to the output directory that will contain the dataset formatted in the required structure.")
    args = parser.parse_args()
    print_args(args, parser)
    split_cvcorpus(**vars(args))