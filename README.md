# Real-Time Voice Cloning in Spanish
This repository is a fork of [Real Time Voice Cloning](https://github.com/CorentinJ/Real-Time-Voice-Cloning) (RTVC) with a synthesizer that works for the Spanish language. You can listen to the demo audios from all the Spanish models we trained (and a sample from RacoonML's trained model, too) [here](https://alexstevechungalvarez.github.io/Real-Time-Voice-Cloning-Spanish/).

### Papers implemented (by CorentinJ)
| URL | Designation | Title | Implementation source |
| --- | ----------- | ----- | --------------------- |
|[**1806.04558**](https://arxiv.org/pdf/1806.04558.pdf) | **SV2TTS** | **Transfer Learning from Speaker Verification to Multispeaker Text-To-Speech Synthesis** | This repo |
|[1802.08435](https://arxiv.org/pdf/1802.08435.pdf) | WaveRNN (vocoder) | Efficient Neural Audio Synthesis | [fatchord/WaveRNN](https://github.com/fatchord/WaveRNN) |
|[1703.10135](https://arxiv.org/pdf/1703.10135.pdf) | Tacotron (synthesizer) | Tacotron: Towards End-to-End Speech Synthesis | [fatchord/WaveRNN](https://github.com/fatchord/WaveRNN)
|[1710.10467](https://arxiv.org/pdf/1710.10467.pdf) | GE2E (encoder)| Generalized End-To-End Loss for Speaker Verification | This repo |

### Dataset used
[Mozilla's Common Voice Spanish dataset](https://commonvoice.mozilla.org/es/datasets)

## Setup

### 1. Install Requirements

**Python 3.6 or 3.7** is needed to run the toolbox.

* Install [PyTorch](https://pytorch.org/get-started/locally/) (>=1.1.0).
* Install [ffmpeg](https://ffmpeg.org/download.html#get-packages).
* Run `pip install -r requirements.txt` to install the remaining necessary packages.

### 2. Download Pretrained Models
Download the latest [here](https://drive.google.com/drive/folders/1lb-LlS8Sx9RqcGzuV6GxvKHk-PC9TqQx?usp=sharing).

### 3. Try the demo CLI

`python demo_cli.py`

If all tests pass, you're good to go.

### 4. Launch the Toolbox
You can then try the toolbox:
`python demo_toolbox.py`  
