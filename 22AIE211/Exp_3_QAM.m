% QAM modulation parameters
M = 16;
k = log2(M);

% Generate random binary data
data = randi([0 1], 1, k*1000);

% Perform QAM modulation
modulated_data = qammod(data, M);

% Add AWGN (Additive White Gaussian Noise)
SNR_dB = 10;
received_data = awgn(modulated_data, SNR_dB, 'measured');

% Perform QAM demodulation
demodulated_data = qamdemod(received_data, M);

% Calculate bit error rate (BER)
ber = biterr(data, demodulated_data) / numel(data);

% Display results
disp(['Bit Error Rate (BER): ' num2str(ber)]);

% Plot figure
figure;
plot(real(received_data), imag(received_data), 'o');
title('QAM Constellation Diagram');
xlabel('In-phase');
ylabel('Quadrature');