% FSK Signal Generation
fs = 1000;
t = 0:1/fs:1;
f1 = 10;
f2 = 20;
A = 1;

% Generate FSK signal
fsk_signal = A*cos(2*pi*f1*t) + A*cos(2*pi*f2*t);

% BPSK Signal Generation
bits = randi([0,1],1,length(t)); 
bpsk_signal = A*cos(2*pi*f1*t + pi*bits);

% Plotting the signals
subplot(2,1,1);
plot(t, fsk_signal);
title('FSK Signal');
xlabel('Time (s)');
ylabel('Amplitude');

subplot(2,1,2);
plot(t, bpsk_signal);
title('BPSK Signal');
xlabel('Time (s)');
ylabel('Amplitude');

% Analysis of FSK and BPSK signals

% Compute the spectrum of the FSK signal
N = length(fsk_signal);
f = (-fs/2:fs/N:fs/2-fs/N);
fsk_spectrum = fftshift(abs(fft(fsk_signal))/N);

% Compute the spectrum of the BPSK signal
bpsk_spectrum = fftshift(abs(fft(bpsk_signal))/N);

% Plot the spectra
figure;
subplot(2,1,1);
plot(f, fsk_spectrum);
xlabel('Frequency (Hz)');
ylabel('Magnitude');
title('FSK Signal Spectrum');

subplot(2,1,2);
plot(f, bpsk_spectrum);
xlabel('Frequency (Hz)');
ylabel('Magnitude');
title('BPSK Signal Spectrum');
