fs = 1000;
T = 1;
t = 0:1/fs:T-1/fs;

f1 = 10;
f2 = 5;
A = 1;
m = square(2*pi*f2*t);

ask_signal = A*(1 + m).*cos(2*pi*f1*t);

figure;
subplot(2,1,1);
plot(t, ask_signal);
xlabel('Time (s)');
ylabel('Amplitude');
title('ASK Signal Waveform');

N = length(ask_signal);
f = (-fs/2:fs/N:fs/2-fs/N);
ask_spectrum = fftshift(abs(fft(ask_signal))/N);

subplot(2,1,2);
plot(f, ask_spectrum);
xlabel('Frequency (Hz)');
ylabel('Magnitude');
title('ASK Signal Spectrum');