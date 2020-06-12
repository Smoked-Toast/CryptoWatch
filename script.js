var chart = new cryptowatch.Embed('bitfinex', 'btcusd', {
	timePeriod: '1d',
    width: 650,
    presetColorScheme: 'delek'
});
chart.mount('#chart-container');