def delay(ear, file, delay_time):
    import soundfile as sf
    import numpy as np
    import sounddevice as sd
    import librosa
    y, sr = sf.read('./data/audio/'+ file)


    #quick catch for the bug caused by no delay
    if delay_time == 0.0:
        return(y)
    sf.write('./data/audio/delay_overwrite.wav', y, sr, format='WAV')
    # Convert the delay time from seconds to samples
    delay_samples = int(delay_time * sr)

    # Create an empty array to hold the delayed signal
    left = y[:, 0]
    right = y[:, 1]

    # Apply the delay line algorithm to the left channel
    blank_section = np.zeros(delay_samples)
    if ear == "left":
        after_1_second = left[:-delay_samples]
        concatenated_array = np.concatenate((blank_section, after_1_second), axis=0)
        # Combine the delayed left channel and the right channel
        y_delayed = np.vstack((concatenated_array, right)).T
        sf.write('./data/audio/delay_overwrite.wav', y_delayed, sr, format='WAV')

    else:
        after_1_second = right[:-delay_samples]
        concatenated_array = np.concatenate((blank_section, after_1_second), axis=0)

        # Combine the delayed left channel and the right channel
        y_delayed = np.vstack((left,concatenated_array)).T
        sf.write('./data/audio/delay_overwrite.wav', y_delayed, sr, format='WAV')

    return(y_delayed)

