% Creating an unperiodic wave
t1 = 0:0.01:2*pi; % Time vector
unperiodic_wave = rand(size(t1)); % Generating random values
subplot(2, 1, 1); % Creating a subplot for unperiodic wave
plot(t1, unperiodic_wave);
title('Unperiodic Wave');
xlabel('Time');
ylabel('Amplitude');

% Creating a sine wave
t2 = 0:0.01:20*pi; % Time vector
sine_wave = sin(t2); % Generating sine values
subplot(2, 1, 2); % Creating a subplot for sine wave
plot(t2, sine_wave);
title('Sine Wave');
xlabel('Time');
ylabel('Amplitude');

% Adjusting subplot spacing
sgtitle('Comparison of Unperiodic Wave and Periodic(Sine) Wave');