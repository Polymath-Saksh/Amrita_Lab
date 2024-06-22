% FM signal parameters
fc = 1000; % carrier frequency in Hz
fm = 100; % modulation frequency in Hz
beta = 5; % modulation index

% Time specifications
fs = 110; % sample rate in Hz
t = 0:1/(10*fs):1; % time vector with lower resolution

% Generate FM signal
x = cos(2*pi*fc*t + beta*sin(2*pi*fm*t));

% Plot the FM signal
plot(t, x);
xlabel('Time (s)');
ylabel('Amplitude');
title('Frequency Modulated (FM) Signal');

% Compute the spectrogram of the FM signal
window = hamming(256); % window function
noverlap = 128; % number of samples to overlap
nfft = 512; % number of FFT points
[S, f, t] = spectrogram(x, window, noverlap, nfft, fs);

% Plot the spectrogram
figure;
imagesc(t, f, 20*log10(abs(S)));
axis xy;
colorbar;
xlabel('Time (s)');
ylabel('Frequency (Hz)');
title('Spectrogram of FM Signal');