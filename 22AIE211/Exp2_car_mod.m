fs = 1000;
fc = 100;
t = 0:1/fs:1;
carrier = cos(2*pi*fc*t);

fm = 10;
modulating = sin(2*pi*fm*t);

subplot(2,1,1);
plot(t, carrier);
xlabel('Time (s)');
ylabel('Amplitude');
title('Carrier Signal');

subplot(2,1,2);
plot(t, modulating);
xlabel('Time (s)');
ylabel('Amplitude');
title('Modulating Signal');