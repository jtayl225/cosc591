def volume(ear, file, scaling_factor):
    import soundfile as sf
    import numpy as np
    import sounddevice as sd
    y, sr = sf.read('./data/hrir/'+ file)

    if ear=="left":
        # Apply the scaling factor to the left channel
        left_scaled = y[:, 0] * scaling_factor

        # Combine the scaled left channel and the right channel
        y_scaled = np.vstack((left_scaled, y[:, 1])).T
    else:
        right_scaled = y[:, 1] * scaling_factor
        y_scaled = np.vstack((y[:,0], right_scaled)).T
    return(y_scaled)

    """
    temporarily commenting out working/testing
    # Load the audio file with soundfile
    #audio_path = 'F:/UNE/COSC591/github_branches/rewrite_functions/data/audio/stereo_drums_96k.wav'
    audio_path = 'F:/UNE/COSC591/github_branches/rewrite_functions/data/audio/stereo_singer_96k.wav'
    #audio_path = 'F:/UNE/COSC591/github_branches/rewrite_functions/data/audio/stereo_thunder_96k.wav'
    y, sr = sf.read(audio_path)

    # Set the scaling factor for the left channel
    left_scaling_factor = 2

    # Apply the scaling factor to the left channel
    left_scaled = y[:, 0] * left_scaling_factor

    # Combine the scaled left channel and the right channel
    y_scaled = np.vstack((left_scaled, y[:, 1])).T

    # Save the scaled signal to a new file
    sf.write('path/to/output/file.wav', y_scaled, sr, format='WAV')

    sd.play(y_scaled, sr)

    """