fs = 1000;
fc = 100;
t = 0:1/fs:1;
carrier = cos(2*pi*fc*t);

fm = 10;
modulating = sin(2*pi*fm*t);

amplitude_modulated = (1 + modulating) .* carrier;

subplot(2,1,1);
plot(t, amplitude_modulated);
xlabel('Time (s)');
ylabel('Amplitude');
title('Amplitude Modulated Signal (Time Domain)');

