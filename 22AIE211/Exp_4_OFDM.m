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

% Study the effects of multipath and noise on the OFDM signal.

% Multipath channel parameters
num_paths = 3; % Number of paths
delay_spread = 5; % Delay spread in samples

% Generate random channel taps
channel_taps = randn(num_paths, 1) + 1i*randn(num_paths, 1);

% Apply the channel to the signal
rx_signal = conv(tx_signal, channel_taps);

% Add AWGN
SNR_dB = 10;
rx_signal_noisy = awgn(rx_signal, SNR_dB, 'measured');

% Plot the received signal
figure;
plot(real(rx_signal_noisy));
title('Received OFDM Signal');
xlabel('Time');
ylabel('Amplitude');