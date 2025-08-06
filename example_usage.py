#!/usr/bin/env python3
"""
Example usage of the MP3 to WAV splitter script.

This demonstrates how to use the mp3_to_wav_splitter.py script programmatically.
"""

import os
from mp3_to_wav_splitter import convert_mp3_to_wav_clips


def example_usage():
    """Example of how to use the MP3 to WAV splitter function."""
    
    # Example 1: Basic usage with default settings
    try:
        input_file = "example_audio.mp3"  # Replace with your MP3 file path
        
        # Check if example file exists
        if not os.path.exists(input_file):
            print(f"⚠️  Example file '{input_file}' not found.")
            print("Please provide a valid MP3 file path.")
            return
        
        print("Example 1: Basic usage (10-second clips, 16kHz)")
        created_files = convert_mp3_to_wav_clips(
            input_file=input_file,
            output_dir="clips_basic",
            clip_duration=10,
            sample_rate=16000
        )
        print(f"Created {len(created_files)} clips in 'clips_basic' directory\n")
        
    except Exception as e:
        print(f"Example 1 failed: {e}\n")
    
    # Example 2: Custom settings
    try:
        input_file = "example_audio.mp3"  # Replace with your MP3 file path
        
        if os.path.exists(input_file):
            print("Example 2: Custom settings (5-second clips, 22kHz)")
            created_files = convert_mp3_to_wav_clips(
                input_file=input_file,
                output_dir="clips_custom",
                clip_duration=5,
                sample_rate=22050
            )
            print(f"Created {len(created_files)} clips in 'clips_custom' directory\n")
        
    except Exception as e:
        print(f"Example 2 failed: {e}\n")


def create_sample_instructions():
    """Print instructions for testing the script."""
    print("=" * 60)
    print("MP3 to WAV Splitter - Testing Instructions")
    print("=" * 60)
    print()
    print("1. Command line usage:")
    print("   python mp3_to_wav_splitter.py your_audio.mp3")
    print("   python mp3_to_wav_splitter.py your_audio.mp3 --output-dir my_clips")
    print("   python mp3_to_wav_splitter.py your_audio.mp3 --clip-duration 5")
    print()
    print("2. Programmatic usage:")
    print("   from mp3_to_wav_splitter import convert_mp3_to_wav_clips")
    print("   files = convert_mp3_to_wav_clips('audio.mp3', 'output_dir')")
    print()
    print("3. Test with sample audio:")
    print("   - Place any MP3 file in this directory")
    print("   - Rename it to 'example_audio.mp3' or update the path in example_usage()")
    print("   - Run: python example_usage.py")
    print()
    print("4. Dependencies required:")
    print("   - librosa (for MP3 loading)")
    print("   - soundfile (for WAV saving)")
    print("   - numpy (for array operations)")
    print("   - tqdm (for progress bars)")
    print()
    print("   Install with: pip install librosa soundfile numpy tqdm")
    print()


if __name__ == "__main__":
    create_sample_instructions()
    example_usage()