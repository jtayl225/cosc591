def volume(ear, file, scaling_factor):
    import soundfile as sf
    import numpy as np
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

