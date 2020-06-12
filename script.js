var chart = new cryptowatch.Embed('bitfinex', 'btcusd', {
	timePeriod: '1d',
    presetColorScheme: 'delek'
});
chart.mount('#chart-container');