def pitch(ear,file,change):
    import librosa
    import numpy as np
    import soundfile as sf

    y, sr = librosa.load('./data/audio/'+ file,mono=False)

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
        sf.write('./data/audio/pitch_overwrite.wav', y_shifted, sr, format='WAV')
    elif ear=="right":
        right_shifted = librosa.effects.pitch_shift(right_np, sr=sr, n_steps=change, bins_per_octave=12)
        # Combine the shifted left channel and the right channel to create the final stereo signal
        y_shifted = np.vstack((left, right_shifted)).T
        sf.write('./data/audio/pitch_overwrite.wav', y_shifted, sr, format='WAV')
    #else:
    #    y_shifted = librosa.effects.pitch_shift(y, sr=sr, n_steps=change, bins_per_octave=12)
    #    sf.write('./data/audio/pitch_overwrite.wav', y_shifted, sr, format='WAV')
    return(y_shifted)
