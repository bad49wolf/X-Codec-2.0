# MP3 to WAV Splitter

A Python script to convert MP3 audio files to WAV format and split them into smaller clips of specified duration.

## Features

- Convert MP3 files to WAV format
- Split audio into clips of configurable duration (default: 10 seconds)
- Configurable sample rate (default: 16kHz to match X-Codec-2.0)
- Automatic padding for the last clip if needed
- Progress bar showing conversion progress
- Handles mono audio conversion automatically

## Dependencies

The script uses the same audio processing libraries as the X-Codec-2.0 project:
- `librosa` - for loading MP3 files
- `soundfile` - for saving WAV files  
- `numpy` - for audio data manipulation
- `tqdm` - for progress bars
- `pathlib` - for file path handling

All dependencies are already included in the project's `requirements.txt`.

## Usage

### Command Line Interface

```bash
# Basic usage - creates 10-second clips at 16kHz
python mp3_to_wav_splitter.py input_audio.mp3

# Specify custom output directory
python mp3_to_wav_splitter.py input_audio.mp3 --output-dir my_clips

# Custom clip duration (5 seconds)
python mp3_to_wav_splitter.py input_audio.mp3 --clip-duration 5

# Custom sample rate (22kHz)
python mp3_to_wav_splitter.py input_audio.mp3 --sample-rate 22050

# All options combined
python mp3_to_wav_splitter.py input_audio.mp3 --output-dir clips --clip-duration 15 --sample-rate 16000
```

### Programmatic Usage

```python
from mp3_to_wav_splitter import convert_mp3_to_wav_clips

# Basic usage
created_files = convert_mp3_to_wav_clips(
    input_file="audio.mp3",
    output_dir="output_clips",
    clip_duration=10,
    sample_rate=16000
)

print(f"Created {len(created_files)} audio clips")
```

## Arguments

- `input_file` (required): Path to the input MP3 file
- `--output-dir`: Output directory for WAV clips (default: "output_clips")
- `--clip-duration`: Duration of each clip in seconds (default: 10)
- `--sample-rate`: Target sample rate for output files (default: 16000)

## Output

The script creates:
- A new directory with the specified name (or "output_clips" by default)
- WAV files named as: `{original_filename}_clip_001.wav`, `{original_filename}_clip_002.wav`, etc.
- Progress information printed to console
- Summary of created files

## Example Output

```
Loading audio file: example.mp3
Original sample rate: 44100, Target sample rate: 16000
Audio duration: 45.23 seconds
Audio shape: (724736,)
Splitting into 5 clips of 10 seconds each
Creating clips: 100%|██████████| 5/5 [00:01<00:00,  3.21it/s]
  Created: example_clip_001.wav (duration: 10.00s)
  Created: example_clip_002.wav (duration: 10.00s)
  Created: example_clip_003.wav (duration: 10.00s)
  Created: example_clip_004.wav (duration: 10.00s)
  Created: example_clip_005.wav (duration: 5.23s)

✅ Success! Created 5 WAV clips in 'output_clips'
📁 Output directory: /path/to/output_clips
```

## Testing

Run the example script to see usage demonstrations:

```bash
python example_usage.py
```

## Integration with X-Codec-2.0

The generated WAV files are compatible with the X-Codec-2.0 inference pipeline:
- Default 16kHz sample rate matches the project requirements
- Mono audio format
- WAV format is supported by the existing `inference.py` script

You can use the generated clips directly with the X-Codec-2.0 inference:

```bash
# First, split your MP3
python mp3_to_wav_splitter.py your_audio.mp3 --output-dir input_clips

# Then run X-Codec-2.0 inference on the clips
python inference.py --input-dir input_clips --output-dir reconstructed_clips
```