% OFDM parameters
N = 64; % Number of subcarriers
cp_len = 16; % Length of cyclic prefix
num_symbols = 10; % Number of OFDM symbols

% Generate random data symbols
data_symbols = randi([0, 1], N, num_symbols);

% Perform IFFT on each symbol
time_symbols = ifft(data_symbols);

% Add cyclic prefix
time_symbols_cp = [time_symbols(end-cp_len+1:end, :); time_symbols];

% Convert to serial stream
tx_signal = time_symbols_cp(:);

% Plot the OFDM signal
% figure;
% plot(real(tx_signal));
% title('OFDM Signal');
% xlabel('Time');
% ylabel('Amplitude');

% Analyse the signal in the time and frequency domain

% Time domain
% figure;
% plot(abs(tx_signal));
% title('OFDM Signal in Time Domain');
% xlabel('Time');
% ylabel('Amplitude');

% Frequency domain
frequency_symbols = fft(data_symbols);
figure;
plot(abs(frequency_symbols));
title('OFDM Signal in Frequency Domain');
xlabel('Frequency');
ylabel('Amplitude');