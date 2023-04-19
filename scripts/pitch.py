def pitch(ear,file,change):
    import librosa
    import numpy as np

    y, sr = librosa.load('./data/hrir/'+ file,mono=False)

    # Extract the left and right channels
    left = y[0]
    right = y[1]
    left_np = np.array(left)
    right_np = np.array(left)

    if ear == "left":
        # Shift the pitch of the left channel up by 2 semitones
        left_shifted = librosa.effects.pitch_shift(left_np, sr=sr, n_steps=change, bins_per_octave=12)
        # Combine the shifted left channel and the right channel to create the final stereo signal
        y_shifted = np.vstack((left_shifted, right)).T
    elif ear=="right":
        right_shifted = librosa.effects.pitch_shift(right_np, sr=sr, n_steps=change, bins_per_octave=12)
        # Combine the shifted left channel and the right channel to create the final stereo signal
        y_shifted = np.vstack((left, right_shifted)).T
    else:
        y_shifted = librosa.effects.pitch_shift(y, sr=sr, n_steps=change, bins_per_octave=12)
    return(y_shifted)


    """
    Temporarily comment out working/testing
    import librosa
    import numpy as np
    import sounddevice as sd

    # Load the audio file
    #audio_path = 'F:/UNE/COSC591/github_branches/rewrite_functions/data/audio/stereo_drums_96k.wav'
    audio_path = 'F:/UNE/COSC591/github_branches/rewrite_functions/data/audio/stereo_singer_96k.wav'
    #audio_path = 'F:/UNE/COSC591/github_branches/rewrite_functions/data/audio/stereo_thunder_96k.wav'

    y, sr = librosa.load(audio_path,mono=False)

    # Shift the pitch up by 2 semitones
    # Extract the left and right channels
    left = y[0]
    right = y[1]
    left = np.array(left)


    # Shift the pitch of the left channel up by 2 semitones
    left_shifted = librosa.effects.pitch_shift(left, sr=sr, n_steps=-10, bins_per_octave=12)

    # Combine the shifted left channel and the right channel to create the final stereo signal
    y_shifted = np.vstack((left_shifted, right)).T


    # Save the shifted audio file
    #librosa.output.write_wav('path/to/output/file.wav', y_shifted, sr)
    sd.play(y_shifted, sr)

    """