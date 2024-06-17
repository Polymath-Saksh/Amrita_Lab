t = 0:0.01:2*pi;
f = 1;
y = sin(2*pi*f*t);

square_wave = 0.5*square(2*pi*f*t);

triangular_wave = 2*sawtooth(2*pi*f*t, 0.5);

figure;
subplot(3,1,1);
plot(t, y);
xlabel('Time');
ylabel('Amplitude');
title('Sine Wave');

subplot(3,1,2);
plot(t, square_wave);
xlabel('Time');
ylabel('Amplitude');
title('Square Wave');

subplot(3,1,3);
plot(t, triangular_wave);
xlabel('Time');
ylabel('Amplitude');
title('Triangular Wave');

amplitude_y = max(y);

[pks, locs] = findpeaks(y);
time_period = t(locs(end)) - t(locs(1));
num_cycles = length(pks) - 1;
frequency_y = num_cycles / time_period;

fprintf('Sine Wave: Amplitude = %f \t Frequency = %f Hz\n', amplitude_y, frequency_y);

amplitude_square = max(square_wave);

[pks, locs] = findpeaks(square_wave);
time_period = t(locs(end)) - t(locs(1));
num_cycles = length(pks) - 1;
frequency_square = num_cycles / time_period;

fprintf('Square Wave: Amplitude = %f \t Frequency = %f Hz\n', amplitude_square, frequency_square);

amplitude_triangular = max(triangular_wave);

[pks, locs] = findpeaks(triangular_wave);
time_period = t(locs(end)) - t(locs(1));
num_cycles = length(pks) - 1;
frequency_triangular = num_cycles / time_period;

fprintf('Triangular Wave: Amplitude = %f \t Frequency = %f Hz\n', amplitude_triangular, frequency_triangular);