#!/usr/bin/env python3
"""
MP3 to WAV Converter and Splitter

This script takes a single MP3 audio file, converts it to WAV format,
and splits it into 10-second clips saved in a new folder.

Usage:
    python mp3_to_wav_splitter.py input_file.mp3 [--output-dir output_folder] [--clip-duration 10]

Dependencies:
    - librosa
    - soundfile 
    - numpy
    - tqdm
    - pathlib
"""

import os
import argparse
import numpy as np
import librosa
import soundfile as sf
from pathlib import Path
from tqdm import tqdm


def convert_mp3_to_wav_clips(input_file, output_dir="output_clips", clip_duration=10, sample_rate=16000):
    """
    Convert MP3 file to WAV and split into clips of specified duration.
    
    Args:
        input_file (str): Path to input MP3 file
        output_dir (str): Output directory for WAV clips
        clip_duration (int): Duration of each clip in seconds
        sample_rate (int): Target sample rate for output files
    
    Returns:
        list: List of created clip file paths
    """
    
    # Validate input file
    input_path = Path(input_file)
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")
    
    if input_path.suffix.lower() not in ['.mp3']:
        raise ValueError(f"Input file must be MP3 format, got: {input_path.suffix}")
    
    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    print(f"Loading audio file: {input_file}")
    # Load audio file with librosa (automatically handles MP3)
    audio_data, orig_sr = librosa.load(input_file, sr=sample_rate, mono=True)
    
    print(f"Original sample rate: {orig_sr}, Target sample rate: {sample_rate}")
    print(f"Audio duration: {len(audio_data) / sample_rate:.2f} seconds")
    print(f"Audio shape: {audio_data.shape}")
    
    # Calculate number of samples per clip
    samples_per_clip = int(clip_duration * sample_rate)
    total_samples = len(audio_data)
    
    # Calculate number of clips
    num_clips = int(np.ceil(total_samples / samples_per_clip))
    
    print(f"Splitting into {num_clips} clips of {clip_duration} seconds each")
    
    # Generate base filename for clips
    base_filename = input_path.stem
    created_files = []
    
    # Split audio into clips
    for i in tqdm(range(num_clips), desc="Creating clips"):
        start_sample = i * samples_per_clip
        end_sample = min((i + 1) * samples_per_clip, total_samples)
        
        # Extract clip
        clip_data = audio_data[start_sample:end_sample]
        
        # Pad last clip if it's shorter than expected
        if len(clip_data) < samples_per_clip:
            padding_length = samples_per_clip - len(clip_data)
            clip_data = np.pad(clip_data, (0, padding_length), mode='constant', constant_values=0)
        
        # Generate output filename
        clip_filename = f"{base_filename}_clip_{i+1:03d}.wav"
        clip_path = output_path / clip_filename
        
        # Save clip as WAV file
        sf.write(str(clip_path), clip_data, sample_rate)
        created_files.append(str(clip_path))
        
        # Print clip info
        clip_duration_actual = len(clip_data) / sample_rate
        print(f"  Created: {clip_filename} (duration: {clip_duration_actual:.2f}s)")
    
    return created_files


def main():
    parser = argparse.ArgumentParser(
        description="Convert MP3 to WAV and split into clips",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python mp3_to_wav_splitter.py audio.mp3
    python mp3_to_wav_splitter.py audio.mp3 --output-dir my_clips
    python mp3_to_wav_splitter.py audio.mp3 --clip-duration 5 --sample-rate 22050
        """
    )
    
    parser.add_argument(
        'input_file',
        type=str,
        help='Path to input MP3 file'
    )
    
    parser.add_argument(
        '--output-dir',
        type=str,
        default='output_clips',
        help='Output directory for WAV clips (default: output_clips)'
    )
    
    parser.add_argument(
        '--clip-duration',
        type=int,
        default=10,
        help='Duration of each clip in seconds (default: 10)'
    )
    
    parser.add_argument(
        '--sample-rate',
        type=int,
        default=16000,
        help='Target sample rate for output files (default: 16000)'
    )
    
    args = parser.parse_args()
    
    try:
        created_files = convert_mp3_to_wav_clips(
            input_file=args.input_file,
            output_dir=args.output_dir,
            clip_duration=args.clip_duration,
            sample_rate=args.sample_rate
        )
        
        print(f"\n✅ Success! Created {len(created_files)} WAV clips in '{args.output_dir}'")
        print(f"📁 Output directory: {os.path.abspath(args.output_dir)}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())